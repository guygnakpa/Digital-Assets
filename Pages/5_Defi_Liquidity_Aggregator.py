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

def defi_His_API():
    Chart_response = r.get("https://api.llama.fi/charts")
    Defi_His_DF = Chart_response.json()
    Defi_His_DF = pd.DataFrame(Defi_His_DF)
    return Defi_His_DF


Defi_His_DF = defi_His_API()
Defi_His_DF["date"] = pd.to_datetime(Defi_His_DF["date"], unit="s").dt.date


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


def Categories_API():
    cg = CoinGeckoAPI()
    DeFi_Categ = cg.get_coins_categories()
    DeFi_Categ0 = pd.DataFrame(DeFi_Categ)
    return DeFi_Categ0


DeFi_categ0 = Categories_API()
Defi_MrkCap = pd.DataFrame(DeFi_categ0[["name", "market_cap", "market_cap_change_24h", "volume_24h"]])
Defi_Metric = Defi_MrkCap.loc[[13], :]


def Defi_Categories_API():
    DeFi_Categ_response = r.get(
        "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=decentralized-finance-defi&order=market_cap_desc&per_page=200&page=1&sparkline=false")
    DeFi_Categ3 = DeFi_Categ_response.json()
    DeFi_Categ3_Norm = pd.json_normalize(DeFi_Categ3)
    DeFi_Categ3_Norm = pd.DataFrame(DeFi_Categ3)
    DeFi_Categ3_Norm = DeFi_Categ3_Norm.drop(columns=["id", "symbol", "image", "roi", "last_updated"])
    return DeFi_Categ3_Norm


DeFi_Categ3_Norm = Defi_Categories_API()
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
AlgoStable_output = Protocol_response_Df2.loc[Protocol_response_Df2["category"] == "Algo-Stables"]
Bridge_output = Protocol_response_Df2.loc[Protocol_response_Df2["category"] == "Bridge"]
CDP_output = Protocol_response_Df2.loc[Protocol_response_Df2["category"] == "CDP"]
Chain_output = Protocol_response_Df2.loc[Protocol_response_Df2["category"] == "Chain"]
CrossChain_output = Protocol_response_Df2.loc[Protocol_response_Df2["category"] == "Cross Chain"]
Derivatives_output = Protocol_response_Df2.loc[Protocol_response_Df2["category"] == "Derivatives"]
Dexes_output = Protocol_response_Df2.loc[Protocol_response_Df2["category"] == "Dexes"]
Insurance_output = Protocol_response_Df2.loc[Protocol_response_Df2["category"] == "Insurance"]
Lending_output = Protocol_response_Df2.loc[Protocol_response_Df2["category"] == "Lending"]
LiquidStaking_output = Protocol_response_Df2.loc[Protocol_response_Df2["category"] == "Liquid Staking"]
Options_output = Protocol_response_Df2.loc[Protocol_response_Df2["category"] == "Options"]
Payment_output = Protocol_response_Df2.loc[Protocol_response_Df2["category"] == "Payment_output"]
Privacy_output = Protocol_response_Df2.loc[Protocol_response_Df2["category"] == "Privacy"]
ReserveCurrency_output = Protocol_response_Df2.loc[Protocol_response_Df2["category"] == "Reserve Currency"]
Services_output = Protocol_response_Df2.loc[Protocol_response_Df2["category"] == "Services"]
Synthetics_output = Protocol_response_Df2.loc[Protocol_response_Df2["category"] == "Synthetics"]
Yield_output = Protocol_response_Df2.loc[Protocol_response_Df2["category"] == "Yield"]
YieldAggregator_output = Protocol_response_Df2.loc[Protocol_response_Df2["category"] == "Yield Aggregator"]
# _________________________________________network output________________________________________________________________
Algo_Plot = px.bar(data_frame=AlgoStable_output, x="name", y=["tvl", "mcap"],
                   title="Algorithmic Stablecoins Category: TVL vs. MarktCap", )
Algo_Plot.update_layout(legend_title="Features",
                        plot_bgcolor='rgba(0,0,0,0)')  # width=1300, height=450, title_x=0.5, title_y=.85,
Algo_Plot.update_xaxes(showgrid=False, title="Protocols")
Algo_Plot.update_yaxes(showgrid=False, title="MarktCap/TVL (USD)")
# categRes=st.plotly_chart(Algo_Plot)
Bridge_Plot = px.bar(data_frame=Bridge_output, x="name", y=["tvl", "mcap"],
                     title="Bridge Category: TVL vs. MarktCap")
Bridge_Plot.update_layout(legend_title="Features", width=1300,
                          plot_bgcolor='rgba(0,0,0,0)')  # width=1300, height=450, title_x=0.5, title_y=.85,
Bridge_Plot.update_xaxes(showgrid=False, title="Protocols")
Bridge_Plot.update_yaxes(showgrid=False, title="MarktCap/TVL (USD)")
# categRes=st.plotly_chart(Bridge_Plot)
CDP_Plot = px.bar(data_frame=CDP_output, x="name", y=["tvl", "mcap"],
                  title="Collateralized Debt Position Category: TVL vs. MarktCap", )
CDP_Plot.update_layout(legend_title="Features", width=1300,
                       plot_bgcolor='rgba(0,0,0,0)')  # width=1300, height=450, title_x=0.5, title_y=.85,
CDP_Plot.update_xaxes(showgrid=False, title="Protocols")
CDP_Plot.update_yaxes(showgrid=False, title="MarktCap/TVL (USD)")
# categRes=st.plotly_chart(CDP_Plot)
Chain_plot = px.bar(data_frame=Chain_output, x="name", y=["tvl", "mcap"],
                    title="Chain Category: TVL vs. MarktCap", )
Chain_plot.update_layout(legend_title="Features", width=1300,
                         plot_bgcolor='rgba(0,0,0,0)')  # width=1300, height=450, title_x=0.5, title_y=.85,
Chain_plot.update_xaxes(showgrid=False, title="Protocols")
Chain_plot.update_yaxes(showgrid=False, title="MarktCap/TVL (USD)")
# categRes=st.plotly_chart(Chain_plot)
CrossChain_plot = px.bar(data_frame=CrossChain_output, x="name", y=["tvl", "mcap"],
                         title="Cross Chain Category: TVL vs. MarktCap", )
CrossChain_plot.update_layout(legend_title="Features", width=1300,
                              plot_bgcolor='rgba(0,0,0,0)')  # width=1300, height=450, title_x=0.5, title_y=.85,
CrossChain_plot.update_xaxes(showgrid=False, title="Protocols")
CrossChain_plot.update_yaxes(showgrid=False, title="MarktCap/TVL (USD)")
# categRes=st.plotly_chart(CrossChain_plot)
Derivatives_plot = px.bar(data_frame=Derivatives_output, x="name", y=["tvl", "mcap"],
                          title="Derivatives Category: TVL vs. MarktCap", )
Derivatives_plot.update_layout(legend_title="Features", width=1300,
                               plot_bgcolor='rgba(0,0,0,0)')  # width=1300, height=450, title_x=0.5, title_y=.85,
Derivatives_plot.update_xaxes(showgrid=False, title="Protocols")
Derivatives_plot.update_yaxes(showgrid=False, title="MarktCap/TVL (USD)")
# categRes=st.plotly_chart(Derivatives_plot)
Dexes_plot = px.bar(data_frame=Dexes_output, x="name", y=["tvl", "mcap"],
                    title="Dexes Category: TVL vs. MarktCap", )
Dexes_plot.update_layout(legend_title="Features", width=1300,
                         plot_bgcolor='rgba(0,0,0,0)')  # width=1300, height=450, title_x=0.5, title_y=.85,
Dexes_plot.update_xaxes(showgrid=False, title="Protocols")
Dexes_plot.update_yaxes(showgrid=False, title="MarktCap/TVL (USD)")
# categRes=st.plotly_chart(Dexes_plot)
Insurance_plot = px.bar(data_frame=Insurance_output, x="name", y=["tvl", "mcap"],
                        title="Insurance Category: TVL vs. MarktCap", )
Insurance_plot.update_layout(legend_title="Features", width=1300,
                             plot_bgcolor='rgba(0,0,0,0)')  # width=1300, height=450, title_x=0.5, title_y=.85,
Insurance_plot.update_xaxes(showgrid=False, title="Protocols")
Insurance_plot.update_yaxes(showgrid=False, title="MarktCap/TVL (USD)")
# categRes=st.plotly_chart(Insurance_plot)
Lending_plot = px.bar(data_frame=Lending_output, x="name", y=["tvl", "mcap"],
                      title="Lending Category: TVL vs. MarktCap", )
Lending_plot.update_layout(legend_title="Features", width=1300,
                           plot_bgcolor='rgba(0,0,0,0)')  # width=1300, height=450, title_x=0.5, title_y=.85,
Lending_plot.update_xaxes(showgrid=False, title="Protocols")
Lending_plot.update_yaxes(showgrid=False, title="MarktCap/TVL (USD)")
# categRes=st.plotly_chart(Lending_plot)
LiquidStaking_plot = px.bar(data_frame=LiquidStaking_output, x="name", y=["tvl", "mcap"],
                            title="Liquid Staking Category: TVL vs. MarktCap", )
LiquidStaking_plot.update_layout(legend_title="Features", width=1300,
                                 plot_bgcolor='rgba(0,0,0,0)')  # width=1300, height=450, title_x=0.5, title_y=.85,
LiquidStaking_plot.update_xaxes(showgrid=False, title="Protocols")
LiquidStaking_plot.update_yaxes(showgrid=False, title="MarktCap/TVL (USD)")
# categRes=st.plotly_chart(LiquidStaking_plot)
Options_plot = px.bar(data_frame=Options_output, x="name", y=["tvl", "mcap"],
                      title="Options Category: TVL vs. MarktCap", )
Options_plot.update_layout(legend_title="Features", width=1300,
                           plot_bgcolor='rgba(0,0,0,0)')  # width=1300, height=450, title_x=0.5, title_y=.85,
Options_plot.update_xaxes(showgrid=False, title="Protocols")
Options_plot.update_yaxes(showgrid=False, title="MarktCap/TVL (USD)")
# categRes=st.plotly_chart(Options_plot)
Payment_plot = px.bar(data_frame=Payment_output, x="name", y=["tvl", "mcap"],
                      title="Payment Category: TVL vs. MarktCap", )
Payment_plot.update_layout(legend_title="Features", width=1300,
                           plot_bgcolor='rgba(0,0,0,0)')  # width=1300, height=450, title_x=0.5, title_y=.85,
Payment_plot.update_xaxes(showgrid=False, title="Protocols")
Payment_plot.update_yaxes(showgrid=False, title="MarktCap/TVL (USD)")
# categRes=st.plotly_chart(Payment_plot)
Privacy_plot = px.bar(data_frame=Privacy_output, x="name", y=["tvl", "mcap"],
                      title="Privacy Category: TVL vs. MarktCap", )
Privacy_plot.update_layout(legend_title="Features", width=1300,
                           plot_bgcolor='rgba(0,0,0,0)')  # width=1300, height=450, title_x=0.5, title_y=.85,
Privacy_plot.update_xaxes(showgrid=False, title="Protocols")
Privacy_plot.update_yaxes(showgrid=False, title="MarktCap/TVL (USD)")
# categRes=st.plotly_chart(Privacy_plot)
ReserveCurrency_plot = px.bar(data_frame=ReserveCurrency_output, x="name", y=["tvl", "mcap"],
                              title="Reserve Currency Category: TVL vs. MarktCap", )
ReserveCurrency_plot.update_layout(legend_title="Features", width=1300,
                                   plot_bgcolor='rgba(0,0,0,0)')  # width=1300, height=450, title_x=0.5, title_y=.85,
ReserveCurrency_plot.update_xaxes(showgrid=False, title="Protocols")
ReserveCurrency_plot.update_yaxes(showgrid=False, title="MarktCap/TVL (USD)")
# categRes=st.plotly_chart(ReserveCurrency_plot)
Services_plot = px.bar(data_frame=Services_output, x="name", y=["tvl", "mcap"],
                       title="Services Category: TVL vs. MarktCap", )
Services_plot.update_layout(legend_title="Features", width=1300,
                            plot_bgcolor='rgba(0,0,0,0)')  # width=1300, height=450, title_x=0.5, title_y=.85,
Services_plot.update_xaxes(showgrid=False, title="Protocols")
Services_plot.update_yaxes(showgrid=False, title="MarktCap/TVL (USD)")
# categRes=st.plotly_chart(Services_plot)
Synthetics_plot = px.bar(data_frame=Synthetics_output, x="name", y=["tvl", "mcap"],
                         title="Synthetics Category: TVL vs. MarktCap", )
Synthetics_plot.update_layout(legend_title="Features", width=1300,
                              plot_bgcolor='rgba(0,0,0,0)')  # width=1300, height=450, title_x=0.5, title_y=.85,
Synthetics_plot.update_xaxes(showgrid=False, title="Protocols")
Synthetics_plot.update_yaxes(showgrid=False, title="MarktCap/TVL (USD)")
# categRes=st.plotly_chart(Synthetics_plot)
Yield_plot = px.bar(data_frame=Yield_output, x="name", y=["tvl", "mcap"],
                    title="Yield Category: TVL vs. MarktCap", )
Yield_plot.update_layout(legend_title="Features", width=1300,
                         plot_bgcolor='rgba(0,0,0,0)')  # width=1300, height=450, title_x=0.5, title_y=.85,
Yield_plot.update_xaxes(showgrid=False, title="Protocols")
Yield_plot.update_yaxes(showgrid=False, title="MarktCap/TVL (USD)")
# categRes=st.plotly_chart(Yield_plot)
YieldAggregator_plot = px.bar(data_frame=YieldAggregator_output, x="name", y=["tvl", "mcap"],
                              title="Yield Aggregator Category: TVL vs. MarktCap", )
YieldAggregator_plot.update_layout(legend_title="Features", width=1300,
                                   plot_bgcolor='rgba(0,0,0,0)')  # width=1300, height=450, title_x=0.5, title_y=.85,
YieldAggregator_plot.update_xaxes(showgrid=False, title="Protocols")
YieldAggregator_plot.update_yaxes(showgrid=False, title="MarktCap/TVL (USD)")
# categRes=st.plotly_chart(YieldAggregator_plot)

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
Categories = ["Algorithmic Stablecoins", "Bridge", "Collateralized Debt Position(CDP)", "Chain", "Cross Chain",
              "Derivatives", "Dexes", "Insurance",
              "Lending", "Liquid Staking", "Options", "Payments", "Privacy", "Reserve Currency", "Services",
              "Synthetics", "Yield", "Yield Aggregator"]

test0 = st.multiselect("DeFi CATEGORIES 👇", Categories)
if "Algorithmic Stablecoins" in test0:
    st.plotly_chart(Algo_Plot)
if "Bridge" in test0:
    st.plotly_chart(Bridge_Plot)
if "Collateralized Debt Position(CDP)" in test0:
    st.plotly_chart(CDP_Plot)
if "Chain" in test0:
    st.plotly_chart(Chain_plot)
if "Cross Chain" in test0:
    st.plotly_chart(CrossChain_plot)
if "Derivatives" in test0:
    st.plotly_chart(Derivatives_plot)
if "Dexes" in test0:
    st.plotly_chart(Dexes_plot)
if "Insurance" in test0:
    st.plotly_chart(Insurance_plot)
if "Lending" in test0:
    st.plotly_chart(Lending_plot)
if "Liquid Staking" in test0:
    st.plotly_chart(LiquidStaking_plot)
if "Options" in test0:
    st.plotly_chart(Options_plot)
if "Payments" in test0:
    st.plotly_chart(Payment_plot)
if "Privacy" in test0:
    st.plotly_chart(Privacy_plot)
if "Reserve Currency" in test0:
    st.plotly_chart(ReserveCurrency_plot)
if "Services" in test0:
    st.plotly_chart(Services_plot)
if "Synthetics" in test0:
    st.plotly_chart(Synthetics_plot)
if "Yield" in test0:
    st.write(Yield_plot)
if "Yield Aggregator" in test0:
    st.plotly_chart(YieldAggregator_plot)
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
Model0_Expander.image(Model0, use_container_width=True)

Model1 = Image.open("Data_PNG_JPG_Files/CentrTODecentr.png")
Model1_Expander = st.expander(label="FROM CENTRALIZATION TO FULL DECENTRALIZATION")
Model1_Expander.image(Model1, use_container_width=True)

Model2 = Image.open("Data_PNG_JPG_Files/web3OpenDecen.png")
Model2_Expander = st.expander(label="WEB3 MODEL OF OPEN DECENTRALIZATION")
Model2_Expander.image(Model2, use_container_width=True)

Model3 = Image.open("Data_PNG_JPG_Files/WEB3andIntProp.png")
Model3_Expander = st.expander(label="WEB3 MODEL OF OPEN DECENTRALIZATION UTILIZING INTELLECTUAL PROPERTY")
Model3_Expander.image(Model3, use_container_width=True)

Model4 = Image.open("Data_PNG_JPG_Files/WEB3OpenDecenNFT.png")
Model4_Expander = st.expander(label="WEB3 MODEL OF OPEN DECENTRALIZATION FOR NFT")
Model4_Expander.image(Model4, use_container_width=True)

Model5 = Image.open("Data_PNG_JPG_Files/WEB3DecenTPro.png")
Model5_Expander = st.expander(label="WEB3 MODEL OF DECENTRALIZATION FOR TOKENIZATION PROTOCOLS")
Model5_Expander.image(Model5, use_container_width=True)
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