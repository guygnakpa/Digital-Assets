import streamlit as st
from streamlit_option_menu import option_menu
import requests as r
import babel.numbers
from PIL import Image
from sklearn.impute import KNNImputer
from Utilities.Navigation import render_sidebar
from pycoingecko import CoinGeckoAPI
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
from Utilities.Navigation import render_sidebar, hide_streamlit_nav
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
@st.cache_data(ttl=86400)  # cache for 24 hours
def DeFi_Data_API():
    cg = CoinGeckoAPI()

    # --- 1) Categories (CoinGecko client) ---
    try:
        DeFi_Categ = cg.get_coins_categories()
        DeFi_categ0 = pd.DataFrame(DeFi_Categ)
    except Exception as e:
        st.warning("CoinGecko Categories request was rate-limited or temporarily unavailable.")
        DeFi_categ0 = pd.DataFrame()

    # --- 2) DeFi coins/markets (HTTP request) ---
    try:
        DeFi_Categ_response = r.get(
            "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=decentralized-finance-defi&order=market_cap_desc&per_page=200&page=1&sparkline=false",
            timeout=20
        )
        DeFi_Categ_response.raise_for_status()
        DeFi_Categ3 = DeFi_Categ_response.json()

        DeFi_Categ3_Norm = pd.json_normalize(DeFi_Categ3)
        DeFi_Categ3_Norm = pd.DataFrame(DeFi_Categ3_Norm)
        DeFi_Categ3_Norm = DeFi_Categ3_Norm.drop(
            columns=["id", "symbol", "image", "roi", "last_updated"],
            errors="ignore"
        )
    except Exception as e:
        st.warning("CoinGecko DeFi markets request was rate-limited or temporarily unavailable.")
        DeFi_Categ3_Norm = pd.DataFrame()

    return DeFi_categ0, DeFi_Categ3_Norm


# Call once
DeFi_categ0, DeFi_Categ3_Norm = DeFi_Data_API()


# ---- keep your existing downstream logic ----

if not DeFi_categ0.empty:
    Defi_MrkCap = pd.DataFrame(
        DeFi_categ0[["name", "market_cap", "market_cap_change_24h", "volume_24h"]]
    )
    # keep your row selection, but guard index
    Defi_Metric = Defi_MrkCap.loc[[13], :] if 13 in Defi_MrkCap.index else pd.DataFrame()
else:
    Defi_MrkCap = pd.DataFrame()
    Defi_Metric = pd.DataFrame()


# Guard before plotting to prevent: Expected one of [] but received: name
if DeFi_Categ3_Norm.empty or "name" not in DeFi_Categ3_Norm.columns:
    st.warning("DeFi market data is unavailable (rate-limited/cached empty). Try again later.")
    st.stop()
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
Defi_MRKCAP_Metric = Defi_Metric[["market_cap"]].sum()
Defi_MRKCAP_MetricUSD = babel.numbers.format_currency(float(Defi_MRKCAP_Metric), "USD", locale="en_US")
ETH_Ratio_Metric = ETH_Ratio[["tvl"]].sum()

TVL_col2, HR24_Change_col, ChainDominance_col1, Defi_ETH_Ratio_col = st.columns(4)
with TVL_col2:
    TVL_col2.metric("TOTAL VALUE LOCKED OF ALL CHAINS (USD)", TVL_MetricUSD)
with HR24_Change_col:
    st.metric("DeFi TOTAL MARKETCAP", Defi_MRKCAP_MetricUSD)
with ChainDominance_col1:
    ratio_metric = format((Defi_MRKCAP_Metric[0] / TVL_Metric[0]), ".2f")
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
ETH_plot = px.bar(data_frame=Defi_MrkCap, x="name", y=["market_cap", "volume_24h"],
                  title="ETHEREUM & OTHER ECOSYSTEMS: MARKTCAP vs. VOLUME_24HR", )
ETH_plot.update_layout(legend_title="Features", width=1300, height=600,
                       plot_bgcolor='rgba(0,0,0,0)')  # width=1300, height=450, title_x=0.5, title_y=.85,
ETH_plot.update_xaxes(showgrid=False, title="Ecosystems")
ETH_plot.update_yaxes(showgrid=False, title="MarktCap/Volume 24hr (USD)")
st.plotly_chart(ETH_plot)

DeFi_Categ3_plot = px.line(data_frame=DeFi_Categ3_Norm, x="name",
                           y=["current_price", "market_cap", "total_volume", "circulating_supply", "total_supply"],
                           title="DeFi TOKENS: LIQUIDITY vs. SUPPLY", )
DeFi_Categ3_plot.update_layout(legend_title="Features", width=1300, height=600,
                               plot_bgcolor='rgba(0,0,0,0)')  # width=1300, height=450, title_x=0.5, title_y=.85,
DeFi_Categ3_plot.update_xaxes(showgrid=False, title="DeFi Tokens")
DeFi_Categ3_plot.update_yaxes(showgrid=False, title="Value in (USD)")
st.plotly_chart(DeFi_Categ3_plot)
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