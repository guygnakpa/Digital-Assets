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
import requests
from Utilities.Navigation import render_sidebar, hide_streamlit_nav

# _____________________________________________________________
st.set_page_config(page_title=" Digital Assets | Capital Markets Analysis", layout="wide")
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

render_sidebar("Capital Markets Analysis")

# _____________________________________________________________

st.markdown("<h1 style='text-align: center; color: white;'>""Capital Markets: Equity and Bond Securities""</h1>",
            unsafe_allow_html=True)
### Name on document
st.markdown("<h1 style='text-align: center; color: white; font-size: 150%'>""Guy Gnakpa""</h1>",
            unsafe_allow_html=True)
# Date of on documents
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>"" January, 2023""</h1>",
            unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>" "</h1>", unsafe_allow_html=True)

# ____________________________________Introduction of Capital Markets____________________________________________________
# what is capital markets and its sub-categories
st.header("Introduction")
st.write("<div style='text-align:justify'> ""\n"
         "Capital markets play a vidal part in the US and global economy. These markets facilitate the free flow of capital in efforts "
         "to allocate funds towards the best ideas and companies. This financial system allows corporations, governments, and individual "
         "investors to raise capital by issuing and selling securities such as stocks(equity) and bonds(debt). All US participants benefit from healthy "
         "capital markets as funds can be utilized to grow businesses, improve technology, finance property investments, and fund infrastructure objectives. "
         "Many of these efforts lead to growth in the market place and influence the creation of jobs while improving national gross domestic product(GDP). "
         "Some fundamental economic functions of capital markets include: "
         , unsafe_allow_html=True)
st.info("""
* Creates a link between investors and savers
* Creates efficient capital utilization
* Provides solution for trading securities
* Provides a hedging(derivatives) solution against market risks
* Improves the effectiveness of capital allocation thus impacting notional GDP
""")

# intro and functions of primary and secondary capital markets
st.header("Sub-categories")
st.subheader("Primary Market:")
st.write("<div style='text-align:justify'> ""\n"
         "The primary market is where securities are issued and sold to the public for the first time, such as an initial "
         "public offering (IPO) of a company's stock. The primary market is where companies and governments raise long-term capital. "
         "Main functions of the primary market include:"
         , unsafe_allow_html=True)
st.info("""
* Origination: focuses on the examination, evaluation and process of new proposals in the primary market.
* Underwriting: investment banks determine the risk and price of particular soon to be issued securities.
* Distribution: refers to brokers and dealers who have the ability to dispense new issued securities to institution and retail investors.
""")
st.subheader("""Secondary Market:""")
st.write("<div style='text-align:justify'> ""\n"
         "The secondary market is where securities that have already been issued are bought and sold among investors. "
         "I.e the stock market, where investors can buy and sell stocks of publicly traded companies. The secondary market allows "
         "securities to be traded providing more leverage and liquidity for investors. "
         "Main functions of the secondary market include: "
         , unsafe_allow_html=True)
st.info("""
* Advise the value of securities
* Offers liquidity to investors for their respective assets
* Provides a marketplace for financial instruments to be traded.
""")
# description of financial instruments in capital markets
st.subheader("""Financial Instruments in Capital Markets:""")
st.info("""
* Equities(stocks): Investment share in a company's total capitalisation; making one a shareholder
* Debt Securities(bonds): Financial assets that enables a stream of interest payments
* Derivatives(futures): Financial instruments who's value are pegged to an underlying asset; i.e, commodities futures, credit default swaps
* Exchange Traded Funds(ETFs-SPY): An instrument that replicated the performance of an underlying index. Funds that are traded on an exchange tracking stocks, bonds etc..
* Foreign Exchange Instruments(FX-USD/EUR): These instruments consist of currencies and derivatives. Mainly currencies that are purchased and sold globally 
  based on their respective exchange rate. 
""")
st.write("___")
st.info("""
There are many factors that can effect capital markets when analysing performance, expected return and risk exposure.
Gross Domestic Product(GDP) is an economic indicator to measure a nation's total productivity level through its products and services.
Federal Fund Rate is one of the most important indicator as it determined the cost of capital for central banks to borrow.
The cost of capital has a ripple effect throughout the rest of the market participants. The 30-year fixed mortgage is a significant indicator as
it correlates with nominal GDP. The housing markets makes up 15-18% of the U.S. GDP. Further, a large volume of fixed-income mortgage securities 
and respective derivatives are traded in capital markets. Lastly, the rate of unemployment determined the state of economic 
conditions, potential exposure to risk for fixed-income and debt issuers. 

Below, there is an interactive dashboard of economic factors that effect the strength of capital markets. In addition,
the dashboard provides Time-Series analysis of equity indices and examples of tech stocks. Bonds make up a large portion 
of capital markets. With that in mind, the dashboard also illustrates the market capitalization of some of largest Bond ETFs. 
""")

st.write("___")
########################################################################################################################
# ----------------------------Crearte Data Visualisation----------------------------
# Import csv and excel files/prep dataframe
# insert qrtly us gdp
qrtly_us_GDP = pd.read_csv("Data_CSV_Files/QRLY_US_GDP.csv")
# st.dataframe(qrtly_us_GDP)
qrtly_us_GDP_fig = px.bar(qrtly_us_GDP, x="DATE", y=["GDP"],
                          title="Gross Domestic Product(GDP): 1947 - 2022 | Billions of Dollars | Quarterly")
qrtly_us_GDP_fig.update_layout(legend_title="Features", width=1300, height=450, title_x=0.5, title_y=.85,
                               plot_bgcolor='rgba(0,0,0,0)')
qrtly_us_GDP_fig.update_xaxes(showgrid=False, title="Date")
qrtly_us_GDP_fig.update_yaxes(showgrid=False, title="Billions of Dollars")
st.plotly_chart(qrtly_us_GDP_fig)

ColA, ColB = st.columns(2)
with ColA:
    # column1
    # insert us funds rate
    US_FundsRate = pd.read_csv("Data_CSV_Files/FEDFUNDS.csv")
    # st.dataframe(US_FundsRate)
    US_FundsRate_fig = px.line(US_FundsRate, x="DATE", y=["FEDFUNDS"],
                               title="Federal Funds Effective Rate(FEDFUNDS): 1954 - 2022 | Percent | Monthly")
    US_FundsRate_fig.update_layout(legend_title="Features", width=1100, height=450, title_x=0.5, title_y=.85,
                                   plot_bgcolor='rgba(0,0,0,0)')
    US_FundsRate_fig.update_xaxes(showgrid=False, title="Date")
    US_FundsRate_fig.update_yaxes(showgrid=False, title="Percent")
    st.plotly_chart(US_FundsRate_fig)
with ColB:
    # insert us 30-year-mortgage
    US_30yr_Mortgage = pd.read_csv("Data_CSV_Files/30yrs_US_Mortgage.csv")
    # st.dataframe(US_FundsRate)
    US_30yr_Mortgage_fig = px.line(US_30yr_Mortgage, x="DATE", y=["MORTGAGE_30YR_US"],
                                   title="US 30-Year Fixed Rate Mortgage Avg : 1971 - 2023 | Percent | Weekly")
    US_30yr_Mortgage_fig.update_layout(legend_title="Features", width=1100, height=450, title_x=0.5, title_y=.85,
                                       plot_bgcolor='rgba(0,0,0,0)')
    US_30yr_Mortgage_fig.update_xaxes(showgrid=False, title="Date")
    US_30yr_Mortgage_fig.update_yaxes(showgrid=False, title="Percent")
    st.plotly_chart(US_30yr_Mortgage_fig)

# insert table for Unemployment rate
st.info(
    "----------------------------------------------------------------------------------------------------------Unemployment Rate: 2012 - 2022---------------------------------------------------------------------------------------------------")
UnemploymentRate = pd.read_csv("Data_CSV_Files/UnemploymentRate.csv")
st.table(UnemploymentRate)

st.write("___")
########################################################################################################################
# ----------------------------GSPC----------------------------
# create a variable storing the strings of specific indicies
# define a function:doownload all indicies of a specific timeframe/return the value
Index_GSPC = ["^GSPC"]  # ,"^IXIC","^DJI"


@st.cache_data
def GSPC_mining(Index_GSPC):
    IndexGSPC_data = yf.download(Index_GSPC, start="1990-01-01", end=None)
    IndexGSPC_data.reset_index(inplace=True)
    IndexGSPC_data.rename(columns={"index": "Date"})
    IndexGSPC_data["Date"] = pd.to_datetime(IndexGSPC_data["Date"], unit="s").dt.date
    return IndexGSPC_data


# using streamlit call and print the function/using plotly, plot line chart incling paremeters
IndexGSPC_data0 = GSPC_mining(Index_GSPC)


def GSPC_chart(IndexGSPC_data0):
    fig_GSPC = px.line(IndexGSPC_data0, x="Date", y=["Adj Close", "Open", "Close", "High", "Low"],
                       title="S&P500 Index: 1990 - Present | Thousands of Dollars | Yearly")
    fig_GSPC.update_layout(legend_title="Features", width=1300, height=450, title_x=0.5, title_y=.85,
                           plot_bgcolor='rgba(0,0,0,0)')
    fig_GSPC.update_xaxes(showgrid=False, title="Date")
    fig_GSPC.update_yaxes(showgrid=True, title="Thousands of Dollars")
    return fig_GSPC
    # ----------------------------IXIC----------------------------


# define a function:doownload all indicies of a specific timeframe/return the value
Index_IXIC = ["^IXIC"]


@st.cache_data
def IXIC_mining(Index_IXIC):
    IndexIXIC_data = yf.download(Index_IXIC, start="1990-01-01", end=None)
    IndexIXIC_data.reset_index(inplace=True)
    IndexIXIC_data.rename(columns={"index": "Date"})
    IndexIXIC_data["Date"] = pd.to_datetime(IndexIXIC_data["Date"], unit="s").dt.date
    return IndexIXIC_data


# using streamlit call and print the function/using plotly, plot line chart incling paremeters
IndexIXIC_data0 = IXIC_mining(Index_IXIC)


def IXIC_chart(IndexIXIC_data0):
    fig_IXIC = px.line(IndexIXIC_data0, x="Date", y=["Adj Close", "Open", "Close", "High", "Low"],
                       title="Nasdaq Index: 1990 - Present | Thousands of Dollars | Yearly")
    fig_IXIC.update_layout(legend_title="Features", width=1300, height=450, title_x=0.5, title_y=.85,
                           plot_bgcolor='rgba(0,0,0,0)')
    fig_IXIC.update_xaxes(showgrid=False, title="Date")
    fig_IXIC.update_yaxes(showgrid=True, title="Thousands of Dollars")
    return fig_IXIC
    # ----------------------------DJI----------------------------


# define a function:doownload all indicies of a specific timeframe/return the value
Index_DJI = ["^DJI"]


@st.cache_data
def DJI_mining(Index_DJI):
    IndexDJI_data = yf.download(Index_DJI, start="1990-01-01", end=None)
    IndexDJI_data.reset_index(inplace=True)
    IndexDJI_data.rename(columns={"index": "Date"})
    IndexDJI_data["Date"] = pd.to_datetime(IndexDJI_data["Date"], unit="s").dt.date
    return IndexDJI_data


# using streamlit call and print the function/using plotly, plot line chart incling paremeters
IndexDJI_data0 = DJI_mining(Index_DJI)


def DJI_chart(IndexDJI_data0):
    fig_DJI = px.line(IndexDJI_data0, x="Date", y=["Adj Close", "Open", "Close", "High", "Low"],
                      title="Dow Jones Index: 1990 - Present | Thousands of Dollars | Yearly")
    fig_DJI.update_layout(legend_title="Features", width=1300, height=450, title_x=0.5, title_y=.85,
                          plot_bgcolor='rgba(0,0,0,0)')
    fig_DJI.update_xaxes(showgrid=False, title="Date")
    fig_DJI.update_yaxes(showgrid=True, title="Thousands of Dollars")

    return fig_DJI


# --------------------------------------------------------Create Top stocks chart----------------------------------------
# ----using yfinance mine the datas for the following tickers["AAPL","MSFT","GOOGL","AMZN","META","TSLA"]-----
AAPL_Stock = ["AAPL"]


@st.cache_data
def AAPL_mining(AAPL_Stock):
    Stock_AAPL_data = yf.download(AAPL_Stock, start="2005-01-01", end=None)
    Stock_AAPL_data.reset_index(inplace=True)
    Stock_AAPL_data.rename(columns={"index": "Date"})
    Stock_AAPL_data["Date"] = pd.to_datetime(Stock_AAPL_data["Date"], unit="s").dt.date
    return Stock_AAPL_data


# using streamlit call and print the function/using plotly, plot line chart incling paremeters
Stock_AAPL_Stock0 = AAPL_mining(AAPL_Stock)


def AAPL_chart(Stock_AAPL_Stock0):
    fig_AAPL = px.line(Stock_AAPL_Stock0, x="Date", y=["Adj Close", "Open", "Close", "High", "Low"],
                       title="Apple: 2005 - Present")
    fig_AAPL.update_layout(legend_title="Features",
                           width=1300, height=450,
                           title_x=0.5, title_y=.85,
                           plot_bgcolor='rgba(0,0,0,0)')
    return fig_AAPL


# Stock_AAPL_Stock0=AAPL_chart(Stock_AAPL_Stock0)
# ------------------------------------Mining data for stock:MICROSOFT------------------------------------------
# using yfinance mine the datas for the following tickers["AAPL","MSFT","GOOGL","AMZN","META","TSLA"]
MSFT_Stock = ["MSFT"]


@st.cache_data
def MSFT_mining(MSFT_Stock):
    Stock_MSFT_data = yf.download(MSFT_Stock, start="2005-01-01", end=None)
    Stock_MSFT_data.reset_index(inplace=True)
    Stock_MSFT_data.rename(columns={"index": "Date"})
    Stock_MSFT_data["Date"] = pd.to_datetime(Stock_MSFT_data["Date"], unit="s").dt.date
    return Stock_MSFT_data


# using streamlit call and print the function/using plotly, plot line chart incling paremeters
Stock_MSFT_Stock0 = MSFT_mining(MSFT_Stock)


def MSFT_chart(Stock_MSFT_Stock0):
    fig_MSFT = px.line(Stock_MSFT_Stock0, x="Date", y=["Adj Close", "Open", "Close", "High", "Low"],
                       title="Microsoft: 2005 - Present")
    fig_MSFT.update_layout(legend_title="Features",
                           width=1300, height=450,
                           title_x=0.5, title_y=.85,
                           plot_bgcolor='rgba(0,0,0,0)')
    return fig_MSFT


# Stock_MSFT_Stock0=MSFT_chart(Stock_MSFT_Stock0)
# ------------------------------------Mining data for stock:GOOGLE------------------------------------------
# using yfinance mine the datas for the following tickers["AAPL","MSFT","GOOGL","AMZN","META","TSLA"]
GOOGL_Stock = ["GOOGL"]


@st.cache_data
def GOOGL_mining(GOOGL_Stock):
    Stock_GOOGL_data = yf.download(GOOGL_Stock, start="2005-01-01", end=None)
    Stock_GOOGL_data.reset_index(inplace=True)
    Stock_GOOGL_data.rename(columns={"index": "Date"})
    Stock_GOOGL_data["Date"] = pd.to_datetime(Stock_GOOGL_data["Date"], unit="s").dt.date
    return Stock_GOOGL_data


# using streamlit call and print the function/using plotly, plot line chart incling paremeters
Stock_GOOGL_Stock0 = GOOGL_mining(GOOGL_Stock)


def GOOGL_chart(Stock_GOOGL_Stock0):
    fig_GOOGL = px.line(Stock_GOOGL_Stock0, x="Date", y=["Adj Close", "Open", "Close", "High", "Low"],
                        title="Google: 2005 - Present")
    fig_GOOGL.update_layout(legend_title="Features",
                            width=1300, height=450,
                            title_x=0.5, title_y=.85,
                            plot_bgcolor='rgba(0,0,0,0)')
    return fig_GOOGL


# st.plotly_chart(GOOGL_chart(Stock_GOOGL_Stock0))
# Stock_GOOGL_Stock0=GOOGL_chart(Stock_GOOGL_Stock0)
# ------------------------------------Mining data for stock:AMAZON------------------------------------------
AMZN_Stock = ["AMZN"]


@st.cache_data
def AMZN_mining(AMZN_Stock):
    Stock_AMZN_data = yf.download(AMZN_Stock, start="2005-01-01", end=None)
    Stock_AMZN_data.reset_index(inplace=True)
    Stock_AMZN_data.rename(columns={"index": "Date"})
    Stock_AMZN_data["Date"] = pd.to_datetime(Stock_AMZN_data["Date"], unit="s").dt.date
    return Stock_AMZN_data


# using streamlit call and print the function/using plotly, plot line chart incling paremeters
Stock_AMZN_Stock0 = AMZN_mining(AMZN_Stock)


def AMZN_chart(Stock_AMZN_Stock0):
    fig_AMZN = px.line(Stock_AMZN_Stock0, x="Date", y=["Adj Close", "Open", "Close", "High", "Low"],
                       title="Amazon: 2005 - Present")
    fig_AMZN.update_layout(legend_title="Features",
                           width=1300, height=450,
                           title_x=0.5, title_y=.85,
                           plot_bgcolor='rgba(0,0,0,0)')
    return fig_AMZN


# Stock_AMZN_Stock0=AMZN_chart(Stock_AMZN_Stock0)
# ------------------------------------Mining data for stock:META------------------------------------------
META_Stock = ["META"]


@st.cache_data
def META_mining(META_Stock):
    Stock_META_data = yf.download(META_Stock, start="2005-01-01", end=None)
    Stock_META_data.reset_index(inplace=True)
    Stock_META_data.rename(columns={"index": "Date"})
    Stock_META_data["Date"] = pd.to_datetime(Stock_META_data["Date"], unit="s").dt.date
    return Stock_META_data


# using streamlit call and print the function/using plotly, plot line chart incling paremeters
Stock_META_Stock0 = META_mining(META_Stock)


def META_chart(Stock_META_Stock0):
    fig_META = px.line(Stock_META_Stock0, x="Date", y=["Adj Close", "Open", "Close", "High", "Low"],
                       title="Meta: 2005 - Present")
    fig_META.update_layout(legend_title="Features",
                           width=1300, height=450,
                           title_x=0.5, title_y=.85,
                           plot_bgcolor='rgba(0,0,0,0)')
    return fig_META


# Stock_META_Stock0=META_chart(Stock_META_Stock0)
# ------------------------------------Mining data for stock:TSLA------------------------------------------
TSLA_Stock = ["TSLA"]


@st.cache_data
def TSLA_mining(TSLA_Stock):
    Stock_TSLA_data = yf.download(TSLA_Stock, start="2005-01-01", end=None)
    Stock_TSLA_data.reset_index(inplace=True)
    Stock_TSLA_data.rename(columns={"index": "Date"})
    Stock_TSLA_data["Date"] = pd.to_datetime(Stock_TSLA_data["Date"], unit="s").dt.date
    return Stock_TSLA_data


# using streamlit call and print the function/using plotly, plot line chart incling paremeters
Stock_TSLA_Stock0 = TSLA_mining(TSLA_Stock)


def TSLA_chart(Stock_TSLA_Stock0):
    fig_TSLA = px.line(Stock_TSLA_Stock0, x="Date", y=["Adj Close", "Open", "Close", "High", "Low"],
                       title="Tesla: 2005 - Present")
    fig_TSLA.update_layout(legend_title="Features",
                           width=1300, height=450,
                           title_x=0.5, title_y=.85,
                           plot_bgcolor='rgba(0,0,0,0)')
    return fig_TSLA


# Stock_TSLA_Stock0=TSLA_chart(Stock_TSLA_Stock0)

# ----------------------------------Create Drop down Buttons for indecies/Index Analysis--------------------------------------------------
# using streamlit module/def function create botton for each index
index_category = ["Dow Jones", "S&P500", "Nasdaq"]
test0 = st.multiselect("Equity Market: select 👇 for Time-series index analysis", index_category)
# insert Dow Jones option
if "Dow Jones" in test0:
    # prep dataframes for metrics
    DowCol_PreviousClosePrice, DowCol_OpenPrice, DowCol_Volume, DowCol_MrkCap = st.columns(4)
    PreviousDow_price = IndexDJI_data0["Adj Close"].tail(1)
    PreviousDow_price0 = PreviousDow_price
    PreviousDow_price = babel.numbers.format_currency(float(PreviousDow_price), "USD", locale='en_US')
    OpenDow_price = IndexDJI_data0["Open"].tail(1)
    OpenDow_price0 = OpenDow_price
    OpenDow_price = babel.numbers.format_currency(float(OpenDow_price), "USD", locale='en_US')
    VolumeDow = IndexDJI_data0["Volume"].tail(1)
    VolumeDow = babel.numbers.format_currency(float(VolumeDow), "USD", locale='en_US')
    DowMarketcap = "$9.67T"

    # PerChngDow=(((PreviousDow_price0-OpenDow_price0)/PreviousDow_price0)*100)->format error

    # Output Metrics
    DowCol_PreviousClosePrice.metric("Previous Close:", PreviousDow_price)
    DowCol_OpenPrice.metric("Open Price:", OpenDow_price)
    DowCol_Volume.metric("Trading Volume:", VolumeDow)
    DowCol_MrkCap.metric("MarketCap as of 2022-31-12", DowMarketcap)
    # DowCol_PerChng.metric(label="∆ in Daily Price(%)",value=PerChngDow)->format error

    # print line chart/analysis
    st.plotly_chart(DJI_chart(IndexDJI_data0))

    st.write("Dow Jones Analysis:")
    # insert dow jones yearyly return
    Dow_Return = pd.read_csv("DowJones_YearlyReturn.csv")
    Dow_Return_fig = px.bar(Dow_Return, x="Year", y="Total Return", color="Total Return",
                            title="Dow Jones Yearly Return : 1893 - 2023 | Percent | Yearly")
    Dow_Return_fig.update_layout(legend_title="Features", width=1250, height=450, title_x=0.5, title_y=.85,
                                 plot_bgcolor='rgba(0,0,0,0)')
    Dow_Return_fig.update_xaxes(showgrid=False, title="Date")
    Dow_Return_fig.update_yaxes(showgrid=False, title="Percent")
    # insert dropdown for data table and stats
    Dow_dropdown_stats = st.expander(label="Dow Jones: Yearly Return and Index Statistics")
    Dow_dropdown_stats.plotly_chart(Dow_Return_fig)
    Dow_dropdown_stats.table(IndexDJI_data0.describe())

    # insert analysis description
    st.info("""
    The Dow Jones Industrial Average, also known as the Dow 30 is the second-oldest equity index in the U.S. The Dow constitutes of 30 
    public blue-chip companies traded on the New York Stock Exchange and the Nasdaq. The index was launched 
    in 1896 by Charles Dow and Edward Jones. The index is well known throughout the world and is utilized by 
    many investors to measure economic performance. The index includes a variety of top companies in numerous industries. 
    Some of the companies include: 
    * American Express 
    * Boeing
    * Cisco Systems
    * Goldman Sachs
    * Johnson & Johnson
    The chart above indicates the Dow Jones has been positively performing since its inception in capital markets.
    The lowest adjusted closing value of the index is 3,136.60 dollars on September 10, 1992. The highest adjusted closing 
    value of the index is 36,799.64 dollars on April 1, 1992. On average the index has an adjusted closing value of 13,644.91 dollars
    based on the available data. It is also important to note 75% of the adjusted closing values from 1992 to present are
    17,388.03 dollars or bellow. This metrics indicates the index has experienced a significant positive moving average since its lowest 
    adjusted value of 3,136.60 dollars in 1992. More specifically, the first dramatic pull-back of the index begin on October 9, 2007 with an 
    adjusted closing value of 14,164.53 dollars and continued until March 9, 2009 with an adjusted closing value of 6,547.05 dollars. From October 9, 2007 
    to March 9 2009, the index experienced a 53.77% retracement. On October 9, 2007, the equity markets, including Dow Jones rallied due to a Fed meeting 
    supporting interest rate cut by the end of the year. This bullish sentiment was short lived according to the data in the chart above. The overrall market conditions 
    during this time period were not favorable for institutions and retail investors. The Great Recession devalued capital markets during this time.
    In those three years, the average 30-years fixed-mortgage rate was approximately 5.80% with 2007 being the highest (6.34%). According to 
    Federal Reserve History, "the value of homes fell by approximately 30% on average from 2006 through mid-2009." Real GDP declined by 4.3% from its peak in 2007 to 
    2009. Lastly unemployment rose from 5% in december 2007 to 10% by October 2009. The Great Recession which started in late 2006, was the biggest influence for the 
    the Dow Jones's contraction from October 9, 2007 to March 9, 2009.
    """)
    # calculation for analysis above/stats
    current = 6547.05
    previous = 14164.53
    percent_change = float(current - previous) / abs(previous) * 100
    # st.write(percent_change)
    Avg_30_fixed = (6.34 + 6.03 + 5.04) / 3
    # st.write(Avg_30_fixed)

    # insert figure button
    DowJones_button = st.expander(label="Figure 1 : Dow Jones Index Time-series Analysis ")
    DowJones_button.write("""
    Datasource: Yahoo Finance
    Technologies: PyCharm, Python; plotly express, pandas, streamlit""")
st.write("---")
# insert S&P500 option
if "S&P500" in test0:
    # create 4 columns
    SPCol_PreviousClosePrice, SPCol_OpenPrice, SPCol_Volume, SPCol_Mrkcap = st.columns(4)
    # prep dataframes for metrics
    PreviousSP_price = IndexGSPC_data0["Close"].tail(1)
    PreviousSP_price0 = PreviousSP_price
    PreviousSP_price = babel.numbers.format_currency(float(PreviousSP_price), "USD", locale='en_US')
    OpenSP_price = IndexGSPC_data0["Open"].tail(1)
    OpenSP_price0 = OpenSP_price
    OpenSP_price = babel.numbers.format_currency(float(OpenSP_price), "USD", locale='en_US')
    VolumeSP = IndexGSPC_data0["Volume"].tail(1)
    VolumeSP = babel.numbers.format_currency(float(VolumeSP), "USD", locale='en_US')
    SPmarketcap = "$33.581T"
    # PerChngDow=(((PreviousDow_price0-OpenDow_price0)/PreviousDow_price0)*100)->format error

    # Output Metrics
    SPCol_PreviousClosePrice.metric("Previous Close:", PreviousSP_price)
    SPCol_OpenPrice.metric("Open Price:", OpenSP_price)
    SPCol_Volume.metric("Trading Volume:", VolumeSP)
    SPCol_Mrkcap.metric("MarketCap as of 2023-01-26:", SPmarketcap)
    # DowCol_PerChng.metric(label="∆ in Daily Price(%)",value=PerChngDow)->format error

    # print line chart/analysis
    st.plotly_chart(GSPC_chart(IndexGSPC_data0))
    # insert title
    st.write("S&P 500 Analysis:")
    # insert dow S&P 500 return
    SP500_Return = pd.read_csv("S&P500_YearlyReturn.csv")
    SP500_Return_fig = px.bar(SP500_Return, x="Year", y="Total Return", color="Total Return",
                              title="S&P 500 Yearly Return : 1927 - 2023 | Percent | Yearly")
    SP500_Return_fig.update_layout(legend_title="Features", width=1250, height=450, title_x=0.5, title_y=.85,
                                   plot_bgcolor='rgba(0,0,0,0)')
    SP500_Return_fig.update_xaxes(showgrid=False, title="Date")
    SP500_Return_fig.update_yaxes(showgrid=False, title="Percent")

    # insert dropdown for data table and stats
    SP500_dropdown_stats = st.expander(label="S&P 500: Yearly Return and Index Statistics")
    SP500_dropdown_stats.plotly_chart(SP500_Return_fig)
    SP500_dropdown_stats.table(IndexGSPC_data0.describe())
    # insert analysis description
    st.info("""
    The Standard and Poor's 500 also known as the S&P 500, is one of the most commonly followed equity indices.
    The S&P 500 is a market-capitalization-weighted index constituted of 500 large companies traded on the American stock exchanges.
    Originally the S&P 500 was The Composite Index 90; representing 90 leading companies in the United States. Later in 1957,
    the index grew to 500 companies. The market capitalization of the index is 33.587 trillion dollars as of 2023. Similar to 
    the Dow Jones, the value of the S&P 500 performance is one of the tools used to gauge U.S. economic conditions and performance. There are many requirements 
    to inter the index; including a market capitalization of 14.6 billion dollars and specified liquidity-based size. Some of the companies include:
    * Warner Bros. Discovery Inc. Series A
    * Carnival Corporation
    * NVIDIA Corporation 
    * United Airlines Holdings Inc.
    * Netflix   
    The chart above showcases the performance of the S&P 500 Index from 1990 to the present time. Similar to the Dow Jones, 
    the S&P 500 has been positively performing since 1957. The lowest adjusted closing value of the index is 295.46 dollars
    on October 11, 1990. The highest adjusted closing value of the index is 4,796.56 dollars on January 3rd, 2022. On average the 
    index has an adjusted closing value of 1,507.09 based on the extracted from yahoo finance. 75% of the adjusted closing prices from 
    1990 to year to day have a value of 1,957.16 dollars or lower. This metrics indicates the index has experienced a significant positive 
    moving average since its lowest adjusted value of 295.46 dollars on October 11, 1990. The line chart displays the most significant devaluation
    of the index from February 19, 2020 with an adjusted closing value of 3,386.15 dollars, to March 23, 2020 with an adjusted closing value of 2,237.40 dollars.
    From February 19, 2020 to March 23, 2020, the index experienced a 33.92% retracement. This significant dilution of the equity index
    was provoked by the Corona Virus crisis of 2019. Capital markets experienced a remarkable liquidity crunch due to lower gross domestic product(GDP) output. 
    The U.S. GDP dropped from 21.92 trillion dollars on February 29, 2020 to 20.74 trillion dollars on March 31st, 2020 and continued to plummet for a few more months.
    GDP fell by 5.33% while unemployment rose from 3.5% in February 2020 to 14.70% by April 2020. This had a significant impact on market conditions and economic output in the 
    United States. The implementation of monetary policy and quantitative easing was imperative for the recovery of capital markets during this health crisis. COVID19 was responsible 
    for the S&P 500's decline from February 19, 2020 to March 23, 2020.             
    """)
    # calculate % change during covid retracement
    current1 = 2237.40
    previous1 = 3386.15
    percent_change1 = float(current1 - previous1) / abs(previous1) * 100
    # st.write(percent_change1)

    # insert figure references button
    SP500_button = st.expander(label="Figure 2.0 references : S&P500 Index Time-series Analysis ")
    SP500_button.write("""
    Datasource: Yahoo Finance
    Technologies: PyCharm, Python; plotly express, pandas, streamlit""")

# insert NAsdaq option
if "Nasdaq" in test0:
    # create 4 columns
    NasdaqCol_PreviousClosePrice, NasdaqCol_OpenPrice, NasdaqCol_Volume, NasdaqCol_Mrkcap = st.columns(4)
    # prep dataframes for metrics
    PreviousNasdaq_price = IndexIXIC_data0["Close"].tail(1)
    PreviousNasdaq_price0 = PreviousNasdaq_price
    PreviousNasdaq_price = babel.numbers.format_currency(float(PreviousNasdaq_price), "USD", locale='en_US')
    OpenNasdaq_price = IndexIXIC_data0["Open"].tail(1)
    OpenNasdaq_price0 = OpenNasdaq_price
    OpenNasdaq_price = babel.numbers.format_currency(float(OpenNasdaq_price), "USD", locale='en_US')
    VolumeNasdaq = IndexIXIC_data0["Volume"].tail(1)
    VolumeNasdaq = babel.numbers.format_currency(float(VolumeNasdaq), "USD", locale='en_US')
    Nasdaqmarketcap = "$16.2T"
    # PerChngDow=(((PreviousDow_price0-OpenDow_price0)/PreviousDow_price0)*100)->format error

    # Output Metrics
    NasdaqCol_PreviousClosePrice.metric("Previous Close:", PreviousNasdaq_price)
    NasdaqCol_OpenPrice.metric("Open Price:", OpenNasdaq_price)
    NasdaqCol_Volume.metric("Trading Volume:", VolumeNasdaq)
    NasdaqCol_Mrkcap.metric("MarketCap as of 2022-01-26:", Nasdaqmarketcap)
    # DowCol_PerChng.metric(label="∆ in Daily Price(%)",value=PerChngDow)->format error
    # print line chart/analysis
    st.plotly_chart(IXIC_chart(IndexIXIC_data0))
    # insert title
    st.write("Nasdaq Analysis:")
    # insert dow S&P 500 return
    Nasda_Return = pd.read_csv("Nadsaq_YearlyReturn.csv")
    Nasda_Return_fig = px.bar(Nasda_Return, x="Year", y="Total Return", color="Total Return",
                              title="Nasday Yearly Return : 1990 - 2023 | Percent | Yearly")
    Nasda_Return_fig.update_layout(legend_title="Features", width=1250, height=450, title_x=0.5, title_y=.85,
                                   plot_bgcolor='rgba(0,0,0,0)')
    Nasda_Return_fig.update_xaxes(showgrid=False, title="Date")
    Nasda_Return_fig.update_yaxes(showgrid=False, title="Percent")

    # insert dropdown for data table and stats
    Nasdaq_dropdown_stats = st.expander(label="Nasdaq: Yearly Return and Index Statistics")
    Nasdaq_dropdown_stats.plotly_chart(Nasda_Return_fig)
    Nasdaq_dropdown_stats.table(IndexIXIC_data0.describe())
    st.info("""
    The Nasdaq Composite Index, also known as The Nasdaq includes 3,642 companies which are listed on the Nasdaq Stock market.
    The index was created in 1971 with a base value of 100. The do-com era boosted the index in terms of net return and increased its popularity.
    The Nasdaq composite tracks domestic and international companies making the index one of the most widely followed market indices.
    The index is heavily weighted towards information technology securities and has a market capitalization of 16.2 trillion dollars 
    as of December 2022. Some of the companies in the index include:
    * Apple
    * Microsoft
    * Amazon
    * Meta
    * Alphabet Class C (Google)
    * Tesla 
    The Chart above illustrates the performance of the Nasdaq Composite Index from 1990 to the present time. The index has 
    experienced a positive return since it's inception similar to the Dow Jones and the S&P 500. The lowest adjusted 
    closing value of the index is 325.40 dollars on October 16, 1990. The highest adjusted closing value of the index is 16,057.44
    dollars on November 19, 2021. The average adjusted closing value since its inception in the capital market is 3,565.03 dollars. 
    75% of the adjusted closing values from 1990 to year to day have a value of 4,564.75 dollars or lower. The Nasdaq has experienced
    several dramatic contraction periods influenced by market conditions of the the do-com bubble (1995-2021), 2008 financial crisis (2006-2009) and the COVID19 Pandemic (2019-2021).
    The effect of these events can be seen on the Time-series chart when zooming closing. During the do-com bubble, the index rallied
    from 1995 with a peak value of 5,048.62 dollars and fell to 1,114.11 dollars on October 9, 2022. Market conditions of the do-come bubble cause the 
    Nasdaq to fall by 77.93%. The next event which effected all capital markets world wide, especially the United States was the 2008 Financial 
    Crisis. The Nasdaq fell from a peak of 2,815.67 dollars on October 31, 2007 to 1,265.52 dollars on March 9, 2009 signifying a 55.05% capital loss of the index. 
    The Nasdaq soon recovered and experienced tremendous growth in price action and market capitalization. However, the COVID19 pandemic was another obstable 
    for capital markets and its respective participants. The Nasdaq Index fell dramatically from a value of 9,817.17 dollars on Feburary 
    19, 2020 to a value of 6,860.67 dollars on March 23, 2020. In 33 days the index fell by 33.11%, nearly one percent a day. Inflation rose 
    above 2% by the end of 2021. The labor market was unfavorable with the unemployment rate rising from 3.5% to 14.7%. The gross domestic product output 
    fell by 5.33% influencing capital loss and social challenges. In order to mitigate the economic downturn from worsening, the Federal Reserve employed monetary policies 
    to stimulate the economy. On March 2020, the federal funds rate decreased to a range of 0% - 0.25% enabling cheap capital and more spending. Interest rates remained 
    near 0 until unemployment rate was optimal for the economy. On March 15, 2020, The Fed announced the utilization of its QE tool to inject large some of liquity throught the purchased of 
    500 billion dollars in Treasury securities and 200 billion dollars in government-guaranteed mortgage-backed securities. The Fed's actions along with the containment of the health crisis 
    led to the recovery of Nasdaq Index and the rest of the equity market. From its last low value of 6,860.67 dollars on March 23, 2020, the index rallied to a peak of 16,057.44 dollars on November 19, 2021.
    The Nasdaq's increase of 134.05% towards value recovery after such economic downturn indicates large volume of Fed liquidity and investor confidence in the capital and equity markets.      
    """)
    # calculate % change during do-com bubble
    current2 = 1114.11
    previous2 = 5048.62
    percent_change2 = float(current2 - previous2) / abs(previous2) * 100
    # st.write(percent_change2)
    # calculate % change during financial crisis
    current3 = 1265.52
    previous3 = 2815.67
    percent_change3 = float(current3 - previous3) / abs(previous3) * 100
    # st.write(percent_change3)
    # calculate % change during COVID19 Pandemic
    current4 = 6860.67
    previous4 = 9817.17
    percent_change4 = float(current4 - previous4) / abs(previous4) * 100
    # st.write(percent_change4)
    # calculate % change of rally after COVID19 Pandemic
    current5 = 16057.44
    previous5 = 6860.67
    percent_change5 = float(current4 - previous5) / abs(previous5) * 100
    # st.write(percent_change4)

    # insert figure references button
    Nasdaq_button = st.expander(label="Figure 3.0 references : Nasdaq Index Time-series Analysis ")
    Nasdaq_button.write("""
    Datasource: Yahoo Finance
    Technologies: PyCharm, Python; plotly express, pandas, streamlit""")

# --------------------------------Create Drop down Buttons for TopTechStock/Index Analysis--------------------------------------------------
TopTechStock_Category = ["Apple", "Microsoft", "Google", "Amazon", "Meta", "Tesla"]
test1 = st.multiselect("Tech Stocks: Select 👇 for a comparison of Time-Series visualization", TopTechStock_Category)
if "Apple" in test1:
    st.plotly_chart(AAPL_chart(Stock_AAPL_Stock0))
if "Microsoft" in test1:
    st.plotly_chart(MSFT_chart(Stock_MSFT_Stock0))
if "Google" in test1:
    st.plotly_chart(GOOGL_chart(Stock_GOOGL_Stock0))
if "Amazon" in test1:
    st.plotly_chart(AMZN_chart(Stock_AMZN_Stock0))
if "Meta" in test1:
    st.plotly_chart(META_chart(Stock_META_Stock0))
if "Tesla" in test1:
    st.plotly_chart(TSLA_chart(Stock_TSLA_Stock0))

st.write("---")


# --------------------------------Create visualisation for Bond ETFs MrkCap-------------------------------
# extract data and prep dataframe
# Define the bond ticker symbol
# ______________________________________Bonds ETFs_______________________
# 1. Use Streamlit caching to prevent frequent hits
@st.cache_data(ttl=3600)
def get_bond_market_caps(tickers):
    caps = {}
    for t in tickers:
        try:
            # Let yfinance handle the session internally (requires curl_cffi installed)
            ticker_obj = yf.Ticker(t)
            caps[t] = ticker_obj.info.get("marketCap")
        except Exception as e:
            st.warning(f"Could not pull data for {t}: {e}")
            caps[t] = None
    return caps


# Variables
bond_etfs = ['AGG', 'HYG', 'LQD', "TLT", "SHY", "IEF"]

#st.title("Bond ETF Market Analysis")

with st.spinner("Fetching data using curl_cffi..."):
    market_cap_dict = get_bond_market_caps(bond_etfs)

# Prep Dataframe
market_cap = pd.Series(market_cap_dict, name="marketCap")
Bond_MrkCap = pd.DataFrame(market_cap).dropna()
Bond_MrkCap = Bond_MrkCap.sort_values(by="marketCap", ascending=False).reset_index()
Bond_MrkCap.columns = ['Ticker', 'marketCap']

# Visualization
if not Bond_MrkCap.empty:
    Bond_MrkCap_fig = px.bar(
        Bond_MrkCap,
        x="Ticker",
        y="marketCap",
        color="Ticker",
        title="Market Capitalization | Bond ETFs",
        template="plotly_white"
    )
    st.plotly_chart(Bond_MrkCap_fig)
else:
    st.error("No data available to display.")


# _______________________________________________________________________
BOND_ETF_COLA, BOND_ETF_COLB = st.columns(2, border=True)
with BOND_ETF_COLA:
    st.write("ishares Core U.S. Aggregate Bond ETF(AGG)")
    st.info("""
       - Offers broad-based exposure to investment grade U.S. Bonds
       - Structured for long-term portfolio strategy
       - Includes hundreds of individual securities with the aim to mitigate illiquid challenges
       """)
    st.write("ishares iboxx $ Investment Grade Corporate Bond ETF(LQD)")
    st.info("""
       - Offers exposure to investment grade corporate bonds 
       - Structured for long-term portfolio strategy
       - Positive yield and low risk due to length of maturity
       """)
    st.write("ishares 1-3 Year Treasury Bond ETF(SHY)")
    st.info("""
       - Offers short-term maturity exposure 
       - Structured for low expected return
       - Offers exposure to securities 1-3 years to maturity
       """)
with BOND_ETF_COLB:
    st.write("ishares iboxx $ High Yield Corporate Bond ETF(HYG)")
    st.info("""
    - Offers exposure to U.S. dollar-denominated high yield liquid corporate bon market
    - High yield with high risk(higher potential for participants to default)
    - Majority of the securities are corporate bonds rated between B and BB
    """)
    st.write("ishares 7-10 Year Treasury Bond ETF(IEF)")
    st.info("""
    - Offers exposure to treasury bonds securities 7-10 years to maturity 
    - Offers higher return then short-term securities
    - Moderate levels of risk
    """)
    st.write("iShares 20+ Year Treasury Bond ETF(TLT)")
    st.info("""
    - Offers exposure to long-dated securities with low credit risk 
    - Offers higher liquidity exposure
    - Efficient and cost effective
    """)
st.write("---")
# ______________________________________Tokenized ETFs_______________________
# 1. Use Streamlit caching to prevent frequent hits
@st.cache_data(ttl=3600)
def get_tokenized_assets_data(tickers):
    data = {}
    for t in tickers:
        try:
            ticker_obj = yf.Ticker(t)
            info = ticker_obj.info

            # Use totalAssets (AUM) as primary for ETFs, marketCap as fallback
            # This is more reliable for funds like IBIT and ETHA
            aum = info.get("totalAssets") or info.get("marketCap")

            # Special handling for BUIDL-USD or similar tokens
            if not aum and t == 'BUIDL-USD':
                # BUIDL often requires supply * price if AUM field is empty
                price = info.get("regularMarketPrice")
                supply = info.get("circulatingSupply")
                if price and supply:
                    aum = price * supply

            data[t] = aum
        except Exception as e:
            st.warning(f"Could not pull data for {t}: {e}")
            data[t] = None
    return data


# Variables
tokenized_assets = ['IBIT', 'ETHA', 'BSOL', 'FBTC',
                    'BTC', 'ETH', 'GBTC', 'ARKB', 'ETHE', 'HODL']

#st.subheader("Digital Assets ETF Analysis")

with st.spinner("Fetching AUM data..."):
    asset_data_dict = get_tokenized_assets_data(tokenized_assets)

# Prep Dataframe
Tokenized_AUM = pd.Series(asset_data_dict, name="AUM").dropna()
df_viz = pd.DataFrame(Tokenized_AUM).sort_values(by="AUM", ascending=False).reset_index()
df_viz.columns = ['Ticker', 'AUM']

# Visualization
if not df_viz.empty:
    fig = px.bar(
        df_viz,
        x="Ticker",
        y="AUM",
        color="Ticker",
        title="Assets Under Management (AUM) | Digital Assets ETFs",
        labels={"AUM": "Assets Under Management (USD)"},
        template="plotly_white"
    )
    st.plotly_chart(fig)
else:
    st.error("No AUM data found. Yahoo Finance may not track AUM for these specific tickers currently.")
# ______________________________________
DigitalAssets_ETF_IBIT, DigitalAssets_ETF_ETHA = st.columns(2, border=True)
with DigitalAssets_ETF_IBIT:
    st.write("iShares Bitcoin Trust ETF(IBIT)")
    st.info("""
    - Spot Bitcoin exposure via an exchange-traded trust structure
    - BlackRock / iShares (iShares Bitcoin Trust ETF)
    - The trust holds bitcoin and issues/redeems shares in large “baskets” via authorized participants (creation/redemption mechanism)
    """)
    st.write("Fidelity Wise Origin Bitcoin Fund(FBTC)")
    st.info("""
    - Spot Bitcoin exposure (Fidelity’s bitcoin fund) designed to track bitcoin performance
    - Fidelity (Fidelity Wise Origin Bitcoin Fund)
    - The trust holds bitcoin and values shares daily using Fidelity’s reference-rate methodology (per fund materials)
    """)
    st.write("Grayscale Bitcoin Trust ETF(GBTC)")
    st.info("""
    - Spot Bitcoin exposure via Grayscale Bitcoin Trust ETF
    - Issued by Grayscale.
    - Solely/passively invested in bitcoin; objective is to reflect bitcoin value held, less expenses/liabilities
    """)
    st.write("iShares Ethereum Trust ETF(ETHA)")
    st.info("""
    - Spot ether (ETH) exposure (Ethereum’s native token) via an exchange-traded trust
    - BlackRock / iShares (iShares Ethereum Trust ETF)
    - Seeks to reflect the price of ether; offers brokerage-account access without direct crypto custody burdens
    """)
    st.write("Grayscale Bitcoin Mini Trust ETF(BTC)")
    st.info("""
    - Spot Bitcoin exposure via Grayscale Bitcoin Mini Trust ETF 
    - Issued by Grayscale
    - Solely/passively invested in bitcoin; objective is to reflect bitcoin value held by the trust, less expenses
    """)
with DigitalAssets_ETF_ETHA:
    st.write("ARK 21Shares Bitcoin ETF(ARKB)")
    st.info("""
    - Spot Bitcoin exposure via ARK 21Shares Bitcoin ETF
    - Sponsored by 21Shares (with ARK branding/partnership)
    - Designed to provide bitcoin exposure with bitcoin held in custody/cold storage (per issuer description)
    """)
    st.write("Grayscale Ethereum Staking ETF(ETHE)")
    st.info("""
    - Spot ether (ETH) exposure via Grayscale Ethereum trust/ETF product
    - Issued by Grayscale
    - Solely/passively invested in ether; objective is to reflect ether value held less expenses/liabilities
    """)
    st.write("Grayscale Ethereum Staking Mini ETF(ETH)")
    st.info("""
    - Spot Ether (ETH) exposure with staking rewards
    - Issued by Grayscale
    - Holds ETH directly and participates in Ethereum’s proof-of-stake validation to generate staking income, less fees and expenses.
    """)
    st.write("VanEck Bitcoin ETF(HODL)")
    st.info("""
    - OSpot Bitcoin exposure via VanEck Bitcoin ETF/trust structure 
    - Issued by VanEck
    - Passive vehicle aiming to reflect bitcoin price (less expenses) and offers brokerage-account access without direct ownership complexity
    """)
    st.write("Bitwise Solana Staking ETF(BSOL)")
    st.info("""
    - Solana (SOL) exposure plus staking rewards (Solana staking ETP/ETF product)
    - issued by Bitwise (Bitwise Solana Staking ETF).
    - Provides direct SOL exposure and a professionally managed staking approach (Bitwise describes targeted staking participation and net staking reward rate disclosures)
    """)
# #--------------------------------Create Drop down Buttons for TopTechStock/Index Analysis--------------------------------------------------
# TopTechStock_Category=["Apple","Microsoft","Google","Amazon","Meta","Tesla"]
# test1=st.multiselect("Tech Stocks: Select 👇 for a comparison of Time-Series visualization",TopTechStock_Category)
# if "Apple" in test1:
#     st.plotly_chart(AAPL_chart(Stock_AAPL_Stock0))
# if "Microsoft" in test1:
#     st.plotly_chart(MSFT_chart(Stock_MSFT_Stock0))
# if "Google" in test1:
#     st.plotly_chart(GOOGL_chart(Stock_GOOGL_Stock0))
# if "Amazon" in test1:
#     st.plotly_chart(AMZN_chart(Stock_AMZN_Stock0))
# if "Meta" in test1:
#     st.plotly_chart(META_chart(Stock_META_Stock0))
# if "Tesla" in test1:
#     st.plotly_chart(TSLA_chart(Stock_TSLA_Stock0))
# insert figure button
REFERENCES = st.expander(label="References")
REFERENCES.write("""
    Datasource: Yahoo Finance, FRED

    Technologies: PyCharm, Python; plotly express, pandas, streamlit, Excel

    [https://data.oecd.org/unemp/unemployment-rate.htm](https://data.oecd.org/unemp/unemployment-rate.htm)

    [https://data.bls.gov/timeseries/LNS14000000](https://data.bls.gov/timeseries/LNS14000000)

    [https://ycharts.com/indicators/us_monthly_gdp](https://ycharts.com/indicators/us_monthly_gdp) 

    [https://www.macrotrends.net/2623/nasdaq-by-year-historical-annual-returns](https://www.macrotrends.net/2623/nasdaq-by-year-historical-annual-returns) 

    [https://www.slickcharts.com/dowjones/returns](https://www.slickcharts.com/dowjones/returns)

    [https://www.google.com/finance/quote/.INX:INDEXSP?hl=en](https://www.google.com/finance/quote/.INX:INDEXSP?hl=en)

    [https://www.federalreservehistory.org/essays/great-recession-of-200709#:~:text=The financial effects of the,its trough in March 2009](https://www.federalreservehistory.org/essays/great-recession-of-200709#:~:text=The%20financial%20effects%20of%20the,its%20trough%20in%20March%202009). 

    [https://fred.stlouisfed.org/series/MORTGAGE30US](https://fred.stlouisfed.org/series/MORTGAGE30US)

    [https://fred.stlouisfed.org/series/FEDFUNDS](https://fred.stlouisfed.org/series/FEDFUNDS)  

    [https://fred.stlouisfed.org/series/GDP](https://fred.stlouisfed.org/series/GDP)   

    [https://money.cnn.com/2007/10/09/markets/markets_0500/](https://money.cnn.com/2007/10/09/markets/markets_0500/)   

    [https://www.elearnmarkets.com/blog/5-instruments-of-capital-market/](https://www.elearnmarkets.com/blog/5-instruments-of-capital-market/)

    [https://en.wikipedia.org/wiki/Nasdaq#cite_note-2](https://en.wikipedia.org/wiki/Nasdaq#cite_note-2)    

    [https://focus.world-exchanges.org/issue/february-2023/market-statistics](https://focus.world-exchanges.org/issue/february-2023/market-statistics)  

    [https://indexes.nasdaqomx.com/Index/Overview/COMP](https://indexes.nasdaqomx.com/Index/Overview/COMP)  

    [https://indexes.nasdaqomx.com/Index/Weighting/COMP](https://indexes.nasdaqomx.com/Index/Weighting/COMP)   

    [https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average](https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average)  

    [https://companiesmarketcap.com/usa/largest-companies-in-the-usa-by-market-cap/](https://companiesmarketcap.com/usa/largest-companies-in-the-usa-by-market-cap/)

    [https://www.investopedia.com/terms/s/sp500.asp](https://www.investopedia.com/terms/s/sp500.asp)  

    [https://www.sifma.org/resources/research/fact-book/](https://www.sifma.org/resources/research/fact-book/)

    https://etfdb.com/etf/TLT/
    """)
st.info("""
DISCLAIMER: The production of this analysis is solely for educational purposes. The data used to explain certain events 
is subject to change, and the analysis is not intended to be used as an investment tool. If this analysis is used for any other purpose, the author is not liable.

""")

########################################################################################################################
########################################################################################################################
########################################################################################################################
