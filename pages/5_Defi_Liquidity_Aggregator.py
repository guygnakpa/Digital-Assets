import streamlit as st
from streamlit_option_menu import option_menu
import requests as r
import babel.numbers
from PIL import Image
from sklearn.impute import KNNImputer
import streamlit.components.v1 as components
import pandas_datareader as pdr
import pandas as pd
import numpy as np
import plotly.express as px
import yfinance as yf
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import statsmodels.api as sm
# import webbrowser
import openpyxl as xls
import datetime
import hashlib
import json
import os
import time
from pathlib import Path

from Utilities.Navigation import render_sidebar, hide_streamlit_nav

# --- CoinGecko / offline resilience (paths relative to Digital Assets project root) ---
_DATA_ROOT = Path(__file__).resolve().parent.parent / "data"
_CACHE_DIR = _DATA_ROOT / "cache"
_MARKETS_SNAPSHOT = _CACHE_DIR / "coingecko_defi_markets.json"
_CATEGORIES_SNAPSHOT = _CACHE_DIR / "coingecko_categories.json"
_FALLBACK_MARKETS_CSV = _DATA_ROOT / "defi_coingecko_markets_fallback.csv"
_FALLBACK_CATEGORIES_CSV = _DATA_ROOT / "defi_coingecko_categories_fallback.csv"


def _coingecko_key_and_pro() -> tuple[str, bool]:
    key = (os.environ.get("COINGECKO_API_KEY") or "").strip()
    pro = str(os.environ.get("COINGECKO_PRO", "")).lower() in ("1", "true", "yes")
    if not key:
        try:
            key = (st.secrets.get("COINGECKO_API_KEY", "") or "").strip()
            pro = str(st.secrets.get("COINGECKO_PRO", "false")).lower() in ("1", "true", "yes")
        except Exception:
            pass
    return key, pro


def _coingecko_key_sig() -> str:
    key, pro = _coingecko_key_and_pro()
    return hashlib.sha256(f"{key}:{pro}".encode()).hexdigest()[:16]


def _coingecko_base_and_headers() -> tuple[str, dict[str, str]]:
    key, pro = _coingecko_key_and_pro()
    if key:
        if pro:
            return "https://pro-api.coingecko.com/api/v3", {"x-cg-pro-api-key": key}
        return "https://api.coingecko.com/api/v3", {"x-cg-demo-api-key": key}
    return "https://api.coingecko.com/api/v3", {}


def _http_get_json(url: str, headers: dict[str, str], max_attempts: int = 6):
    """GET JSON with exponential backoff on rate-limit / transient errors."""
    merged = {**headers, "Accept": "application/json"}
    for attempt in range(max_attempts):
        try:
            resp = r.get(url, headers=merged, timeout=40)
            if resp.status_code == 200:
                return resp.json()
            if resp.status_code in (429, 418, 503, 502, 504):
                time.sleep(min(45.0, 1.85 ** attempt))
                continue
            # Other 4xx/5xx: brief backoff then fail out
            if 400 <= resp.status_code < 500:
                return None
            resp.raise_for_status()
        except r.exceptions.RequestException:
            time.sleep(min(25.0, 1.6 ** attempt))
    return None


def _normalize_markets_rows(rows: list) -> pd.DataFrame:
    if not rows:
        return pd.DataFrame()
    df = pd.json_normalize(rows)
    df = pd.DataFrame(df)
    return df.drop(columns=["id", "symbol", "image", "roi", "last_updated"], errors="ignore")


def _load_json_list(path: Path) -> list | None:
    try:
        if not path.is_file():
            return None
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else None
    except Exception:
        return None


def _save_json_list(path: Path, rows: list) -> None:
    try:
        _CACHE_DIR.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(rows), encoding="utf-8")
    except Exception:
        pass


def _surrogate_markets_from_llama_protocols(protocol_df: pd.DataFrame) -> pd.DataFrame:
    """When CoinGecko is unavailable, approximate token-style series from DefiLlama protocols."""
    if protocol_df is None or protocol_df.empty or "name" not in protocol_df.columns:
        return pd.DataFrame()
    ll = protocol_df.copy()
    if "tvl" not in ll.columns:
        return pd.DataFrame()
    ll = ll.sort_values("tvl", ascending=False).head(50)
    out = pd.DataFrame(
        {
            "name": ll["name"],
            "current_price": np.nan,
            "market_cap": ll["mcap"] if "mcap" in ll.columns else np.nan,
            "total_volume": ll["tvl"],
            "circulating_supply": np.nan,
            "total_supply": np.nan,
        }
    )
    return out.fillna(0.0)
# _____________________________________________________________
st.set_page_config(page_title=" Digital Assets | Defi Liquidity Aggregator", layout="wide")
hide_streamlit_nav()
# _____________________________________________________________
# Optional: hide Streamlit chrome
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

render_sidebar("DeFi Liquidity Aggregator")
# _____________________________________________________________

# ______________________________________________#insert logo/title_______________________________________________________
st.markdown("<h1 style='text-align: center; color: white; font-size: 500%'>""Definomics ☕""</h1>",
            unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white; font-size: 200%'>""DeFi💧Aggregator ""</h1>",
            unsafe_allow_html=True)
## st.info(
   ### "-----------------------------------------------------------------------------------------------------------------💧------------------------------------------------------------------------------------------------------------------------------------")


# _________________________________________Call API & Set Dataframes_____________________________________________________

@st.cache_data(ttl=86400)  # cache for 6 hours to reduce 429 rate-limit errors
def defi_His_API():
    Chart_response = r.get("https://api.llama.fi/charts")
    Defi_His_DF = Chart_response.json()
    Defi_His_DF = pd.DataFrame(Defi_His_DF)
    return Defi_His_DF


Defi_His_DF = defi_His_API()
Defi_His_DF["date"] = pd.to_datetime(Defi_His_DF["date"], unit="s").dt.date


@st.cache_data(ttl=86400)  # cache for 6 hours to reduce 429 rate-limit errors
def defi_API():
    Chains_response = r.get("https://api.llama.fi/chains")
    Defi_Chains_Df = Chains_response.json()
    Defi_Chains_Df = pd.DataFrame(Defi_Chains_Df)
    return Defi_Chains_Df


Defi_Chains_Df = defi_API()
ETH_Ratio = Defi_Chains_Df[["name", "tvl"]]
ETH_Ratio = ETH_Ratio.loc[ETH_Ratio["name"] == "Ethereum"]

Defi_Agr_Data0 = pd.DataFrame(Defi_Chains_Df)
Defi_Agr_Data1 = Defi_Agr_Data0.loc[[0, 1, 3, 4, 5, 9, 23], ["name", "tvl"]]


@st.cache_data(ttl=86400)  # cache for 6 hours to reduce 429 rate-limit errors
def Protocol_API():
    Protocol_response = r.get("https://api.llama.fi/protocols")
    Protocol_response_Df = Protocol_response.json()
    Protocol_response_Df = Protocol_response_Df[0:100]
    Protocol_response_Df2 = pd.json_normalize(Protocol_response_Df)
    Protocol_response_Df2 = pd.DataFrame(Protocol_response_Df2[
                                             ["name", "chain", "category", "tvl", "change_1h", "change_1d",
                                              "change_7d", "mcap", "chains"]])
    return Protocol_response_Df2


Protocol_response_Df2 = Protocol_API()

###############################################################################################################
###############################################################################################################
###############################################################################################################
@st.cache_data(ttl=7200)
def _cached_coingecko_defi_bundle(key_sig: str) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    """Categories + DeFi markets from CoinGecko with retries, disk snapshots, and bundled CSV fallbacks (no Streamlit UI)."""
    meta: dict = {
        "categories_live": False,
        "markets_live": False,
        "categories_from": "",
        "markets_from": "",
    }
    base, headers = _coingecko_base_and_headers()

    cat_rows = _http_get_json(f"{base}/coins/categories", headers)
    DeFi_categ0 = pd.DataFrame(cat_rows) if cat_rows else pd.DataFrame()
    if not DeFi_categ0.empty:
        meta["categories_live"] = True
        meta["categories_from"] = "coingecko"
        if isinstance(cat_rows, list):
            _save_json_list(_CATEGORIES_SNAPSHOT, cat_rows)
    else:
        snap = _load_json_list(_CATEGORIES_SNAPSHOT)
        if snap:
            DeFi_categ0 = pd.DataFrame(snap)
            meta["categories_from"] = "disk_snapshot"
        elif _FALLBACK_CATEGORIES_CSV.is_file():
            DeFi_categ0 = pd.read_csv(_FALLBACK_CATEGORIES_CSV)
            meta["categories_from"] = "bundled_csv"

    markets_url = (
        f"{base}/coins/markets?vs_currency=usd&category=decentralized-finance-defi"
        "&order=market_cap_desc&per_page=250&page=1&sparkline=false"
    )
    m_rows = _http_get_json(markets_url, headers)
    DeFi_Categ3_Norm = _normalize_markets_rows(m_rows) if m_rows else pd.DataFrame()
    if not DeFi_Categ3_Norm.empty and "name" in DeFi_Categ3_Norm.columns:
        meta["markets_live"] = True
        meta["markets_from"] = "coingecko"
        if isinstance(m_rows, list):
            _save_json_list(_MARKETS_SNAPSHOT, m_rows)
    else:
        snap = _load_json_list(_MARKETS_SNAPSHOT)
        if snap:
            DeFi_Categ3_Norm = _normalize_markets_rows(snap)
            meta["markets_from"] = "disk_snapshot"
        if (DeFi_Categ3_Norm.empty or "name" not in DeFi_Categ3_Norm.columns) and _FALLBACK_MARKETS_CSV.is_file():
            DeFi_Categ3_Norm = pd.read_csv(_FALLBACK_MARKETS_CSV)
            meta["markets_from"] = "bundled_csv"

    return DeFi_categ0, DeFi_Categ3_Norm, meta


DeFi_categ0, DeFi_Categ3_Norm, _cg_meta = _cached_coingecko_defi_bundle(_coingecko_key_sig())

# Ensure category frame has columns expected by ecosystem chart
_required_cat = {"name", "market_cap", "market_cap_change_24h", "volume_24h"}
if not DeFi_categ0.empty and not _required_cat.issubset(DeFi_categ0.columns):
    DeFi_categ0 = pd.DataFrame()
if DeFi_categ0.empty and _FALLBACK_CATEGORIES_CSV.is_file():
    DeFi_categ0 = pd.read_csv(_FALLBACK_CATEGORIES_CSV)

if _cg_meta.get("markets_from") and _cg_meta["markets_from"] != "coingecko":
    st.info(
        "CoinGecko DeFi markets hit a rate limit or error. Showing **"
        + _cg_meta["markets_from"].replace("_", " ")
        + "** data so charts stay usable. Add **COINGECKO_API_KEY** (optional **COINGECKO_PRO=true** for Pro) in "
        "`.streamlit/secrets.toml` or your environment for higher limits."
    )
elif not _cg_meta.get("markets_live") and not DeFi_Categ3_Norm.empty:
    st.info("Using offline or cached CoinGecko token snapshot. Configure a CoinGecko API key for live data.")

if _cg_meta.get("categories_from") and _cg_meta["categories_from"] != "coingecko" and not DeFi_categ0.empty:
    st.info("Ecosystem category table uses a **cached or offline** CoinGecko snapshot.")

# ---- keep your existing downstream logic ----
if not DeFi_categ0.empty:
    Defi_MrkCap = pd.DataFrame(
        DeFi_categ0[["name", "market_cap", "market_cap_change_24h", "volume_24h"]]
    )
    Defi_Metric = Defi_MrkCap.loc[[13], :] if 13 in Defi_MrkCap.index else pd.DataFrame()
else:
    Defi_MrkCap = pd.DataFrame()
    Defi_Metric = pd.DataFrame()

# Live DefiLlama substitute when CoinGecko token rows are still unavailable
if DeFi_Categ3_Norm.empty or "name" not in DeFi_Categ3_Norm.columns:
    DeFi_Categ3_Norm = _surrogate_markets_from_llama_protocols(Protocol_response_Df2)
    if not DeFi_Categ3_Norm.empty:
        st.info(
            "CoinGecko token series unavailable. Showing **top protocols by TVL** from DefiLlama "
            "(TVL used in place of volume where needed) so the liquidity chart remains available."
        )

if DeFi_Categ3_Norm.empty or "name" not in DeFi_Categ3_Norm.columns:
    if _FALLBACK_MARKETS_CSV.is_file():
        DeFi_Categ3_Norm = pd.read_csv(_FALLBACK_MARKETS_CSV)

if DeFi_Categ3_Norm.empty or "name" not in DeFi_Categ3_Norm.columns:
    st.warning("DeFi token chart data could not be loaded. Other sections below may still work.")
###############################################################################################################
# @st.cache_data(ttl=86400)  # cache for 6 hours to reduce 429 rate-limit errors
# def Categories_API():
#     cg = CoinGeckoAPI()
#     try:
#         DeFi_Categ = cg.get_coins_categories()
#         DeFi_Categ0 = pd.DataFrame(DeFi_Categ)
#         return DeFi_Categ0
#
#     except Exception as e:
#         st.warning("CoinGecko Categories request was rate-limited or temporarily unavailable.")
#         return pd.DataFrame()  # return empty dataframe to prevent crash
#
# DeFi_categ0 = Categories_API()
#
# if not DeFi_categ0.empty:
#     Defi_MrkCap = pd.DataFrame(
#         DeFi_categ0[["name", "market_cap", "market_cap_change_24h", "volume_24h"]]
#     )
#     Defi_Metric = Defi_MrkCap.loc[[13], :]
# else:
#     Defi_MrkCap = pd.DataFrame()
#     Defi_Metric = pd.DataFrame()
#
#
# @st.cache_data(ttl=86400)  # cache for 6 hours to reduce 429 rate-limit errors
# def Defi_Categories_API():
#     try:
#         DeFi_Categ_response = r.get(
#             "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=decentralized-finance-defi&order=market_cap_desc&per_page=200&page=1&sparkline=false",
#             timeout=20
#         )
#
#         # Raise HTTPError for 4xx/5xx (including 429)
#         DeFi_Categ_response.raise_for_status()
#
#         DeFi_Categ3 = DeFi_Categ_response.json()
#         DeFi_Categ3_Norm = pd.json_normalize(DeFi_Categ3)
#         DeFi_Categ3_Norm = pd.DataFrame(DeFi_Categ3_Norm)
#         DeFi_Categ3_Norm = DeFi_Categ3_Norm.drop(columns=["id", "symbol", "image", "roi", "last_updated"], errors="ignore")
#         return DeFi_Categ3_Norm
#
#     except Exception as e:
#         st.warning("CoinGecko DeFi categories request was rate-limited or temporarily unavailable.")
#         return pd.DataFrame()
#
# DeFi_Categ3_Norm = Defi_Categories_API()
###############################################################################################################
###############################################################################################################
###############################################################################################################

# ___________________________________Insert Hist TVL lineChart___________________________________________________________
Defi_His_LinePlot = px.line(Defi_His_DF, x="date", y="totalLiquidityUSD")
Defi_His_LinePlot.update_layout(legend_title="Digital Assets", width=1300, height=550, plot_bgcolor='rgba(0,0,0,0)')
Defi_His_LinePlot.update_xaxes(showgrid=False)
Defi_His_LinePlot.update_yaxes(showgrid=True)
# ________________________________________________LineChart and buttin title_____________________________________________
TVL_col0, TVL_col2 = st.columns(2)
with TVL_col0:
    Press = st.button("Total TVL (USD)")
with TVL_col2:
    st.write("")
st.plotly_chart(Defi_His_LinePlot)
st.write("---")
# ________________________________________Insert Metrics in three Columns _____________________________________________________
TVL_Metric = Defi_Chains_Df[["tvl"]].sum()
TVL_MetricUSD = babel.numbers.format_currency(float(TVL_Metric), "USD", locale='en_US')
if not Defi_Metric.empty and "market_cap" in Defi_Metric.columns:
    mcap_sum = float(Defi_Metric["market_cap"].sum())
    Defi_MRKCAP_MetricUSD = babel.numbers.format_currency(mcap_sum, "USD", locale="en_US")
else:
    mcap_sum = 0.0
    Defi_MRKCAP_MetricUSD = "N/A (ecosystem data unavailable)"
ETH_Ratio_Metric = ETH_Ratio[["tvl"]].sum()

TVL_col2, HR24_Change_col, ChainDominance_col1, Defi_ETH_Ratio_col = st.columns(4)
with TVL_col2:
    TVL_col2.metric("TOTAL VALUE LOCKED OF ALL CHAINS (USD)", TVL_MetricUSD)
with HR24_Change_col:
    st.metric("DeFi TOTAL MARKETCAP", Defi_MRKCAP_MetricUSD)
with ChainDominance_col1:
    tvl_total = float(TVL_Metric.iloc[0]) if hasattr(TVL_Metric, "iloc") else float(TVL_Metric)
    if tvl_total > 0 and mcap_sum > 0:
        ratio_metric = format(mcap_sum / tvl_total, ".2f")
    else:
        ratio_metric = "N/A"
    st.metric("MARKETCAP / TVL (ratio)", ratio_metric)
with Defi_ETH_Ratio_col:
    ETH_Ratio_Metric = (ETH_Ratio_Metric[0] / TVL_Metric[0])
    ETH_Ratio_Metric = "{:.0%}".format(ETH_Ratio_Metric)
    st.metric("ETHEREUM TVL DOMINANCE", ETH_Ratio_Metric)
st.info(
    "--------------------------------------------------------------------The liquidity charts below are interactive. Selected or unselect features for comparisons----------------------------------------------------------------")
# __________________________________________________Insert Category VS. Networks_________________________________________
def _has_category_chart_data(category_df):
    if category_df.empty:
        return False

    value_columns = [column for column in ["tvl", "mcap"] if column in category_df.columns]
    return bool(value_columns) and category_df[value_columns].notna().any().any()


def _display_category_name(category):
    category_display_names = {
        "CDP": "Collateralized Debt Position (CDP)",
        "Dexs": "Dexes",
    }
    return category_display_names.get(category, category)


def _build_category_plot(category, category_df):
    value_columns = [column for column in ["tvl", "mcap"] if column in category_df.columns and category_df[column].notna().any()]
    category_plot = px.bar(
        data_frame=category_df.sort_values(by=value_columns[0], ascending=False),
        x="name",
        y=value_columns,
        title=f"{_display_category_name(category)} Category: TVL vs. MarketCap",
    )
    category_plot.update_layout(legend_title="Features", width=1300, plot_bgcolor='rgba(0,0,0,0)')
    category_plot.update_xaxes(showgrid=False, title="Protocols")
    category_plot.update_yaxes(showgrid=False, title="MarketCap/TVL (USD)")
    return category_plot


available_category_frames = {}
for category in sorted(Protocol_response_Df2["category"].dropna().unique()):
    category_df = Protocol_response_Df2.loc[Protocol_response_Df2["category"] == category].copy()
    if _has_category_chart_data(category_df):
        available_category_frames[_display_category_name(category)] = (category, category_df)

# _________________________________________ETHEREUM VS OTHER ECOSYSTEMS__________________________________________________
if not Defi_MrkCap.empty:
    ETH_plot = px.bar(
        data_frame=Defi_MrkCap,
        x="name",
        y=["market_cap", "volume_24h"],
        title="ETHEREUM & OTHER ECOSYSTEMS: MARKTCAP vs. VOLUME_24HR",
    )
    ETH_plot.update_layout(legend_title="Features", width=1300, height=600, plot_bgcolor='rgba(0,0,0,0)')
    ETH_plot.update_xaxes(showgrid=False, title="Ecosystems")
    ETH_plot.update_yaxes(showgrid=False, title="MarktCap/Volume 24hr (USD)")
    st.plotly_chart(ETH_plot)
else:
    st.info("Ecosystem market-cap / volume chart skipped (no CoinGecko category snapshot). TVL and protocol charts below still load from DefiLlama.")

_line_y = [c for c in ["current_price", "market_cap", "total_volume", "circulating_supply", "total_supply"] if c in DeFi_Categ3_Norm.columns]
if not DeFi_Categ3_Norm.empty and "name" in DeFi_Categ3_Norm.columns and _line_y:
    DeFi_Categ3_plot = px.line(
        data_frame=DeFi_Categ3_Norm,
        x="name",
        y=_line_y,
        title="DeFi TOKENS: LIQUIDITY vs. SUPPLY",
    )
    DeFi_Categ3_plot.update_layout(legend_title="Features", width=1300, height=600, plot_bgcolor='rgba(0,0,0,0)')
    DeFi_Categ3_plot.update_xaxes(showgrid=False, title="DeFi Tokens")
    DeFi_Categ3_plot.update_yaxes(showgrid=False, title="Value in (USD)")
    st.plotly_chart(DeFi_Categ3_plot)
else:
    st.warning("DeFi token line chart could not be built (missing columns).")
"\n"
"\n"
st.info(
    "-----------------------------------------------------------------Select one or multiple categories for charts to be displayed. Categorical liquidity comparisons-----------------------------------------------------------")

"\n"
"\n"
# ___________________________________________#Category Dropdown________________________________________________________
Categories = list(available_category_frames.keys())

test0 = st.multiselect("DeFi CATEGORIES 👇", Categories)
for selected_category in test0:
    api_category, selected_category_df = available_category_frames[selected_category]
    if _has_category_chart_data(selected_category_df):
        st.plotly_chart(_build_category_plot(api_category, selected_category_df))
"\n"
"\n"
st.info(
    "---------------------------------------------------------------------------------------------------------------TOP 100 PROTOCOLS--------------------------------------------------------------------------------------------------------------")
# insert TOP 100 Protocols
Protocol_response_Df2
st.info(
    "---------------------------------------------------------------------------------------------------------------------DeFi Tokens--------------------------------------------------------------------------------------------------------------------")

DeFi_Categ3_Norm
st.info(
    "-------------------------------------------------------------------------------------------------DECENTRALIZED ARCHITECTURE MODELS----------------------------------------------------------------------------------------------")
# insert Data for Web3 Model
Model0 = Image.open("Data_PNG_JPG_Files/Comp of Decen sys.png")
Model0_Expander = st.expander(label="COMPONENTS OF DECENTRALIZED SYSTEMS")
Model0_Expander.image(Model0, width="stretch")

Model1 = Image.open("Data_PNG_JPG_Files/CentrTODecentr.png")
Model1_Expander = st.expander(label="FROM CENTRALIZATION TO FULL DECENTRALIZATION")
Model1_Expander.image(Model1, width="stretch")

Model2 = Image.open("Data_PNG_JPG_Files/web3OpenDecen.png")
Model2_Expander = st.expander(label="WEB3 MODEL OF OPEN DECENTRALIZATION")
Model2_Expander.image(Model2, width="stretch")

Model3 = Image.open("Data_PNG_JPG_Files/WEB3andIntProp.png")
Model3_Expander = st.expander(label="WEB3 MODEL OF OPEN DECENTRALIZATION UTILIZING INTELLECTUAL PROPERTY")
Model3_Expander.image(Model3, width="stretch")

Model4 = Image.open("Data_PNG_JPG_Files/WEB3OpenDecenNFT.png")
Model4_Expander = st.expander(label="WEB3 MODEL OF OPEN DECENTRALIZATION FOR NFT")
Model4_Expander.image(Model4, width="stretch")

Model5 = Image.open("Data_PNG_JPG_Files/WEB3DecenTPro.png")
Model5_Expander = st.expander(label="WEB3 MODEL OF DECENTRALIZATION FOR TOKENIZATION PROTOCOLS")
Model5_Expander.image(Model5, width="stretch")
st.info(
    "---------------------------------------------------------------------------------------------------------------------------💧-------------------------------------------------------------------------------------------------------------------------")
# insert figure button
Defi_button = st.expander(label="REFERENCES")
Defi_button.write("""

[Coingecko API ]
    (https://www.coingecko.com/en/api/documentation)

[Defi Llama API]
    (https://defillama.com/docs/api)

[future.com, Miles Jennings (2022), "Decentralization for Web3 Builders: Principles, Models, How"]
    (https://future.com/web3-decentralization-models-framework-principles-how-to/)

Technologies: Pycharm, CoingeckoAPI, DefiLlama API, Python;plotly express, pandas, numpy, streamlit
""")
st.write("___")

########################################################################################################################
########################################################################################################################
########################################################################################################################