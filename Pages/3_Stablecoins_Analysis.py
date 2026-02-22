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
st.set_page_config(page_title=" Digital Assets | Stablecoins Analysis", layout="wide")
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

render_sidebar("Stablecoins Analysis")
# _____________________________________________________________

st.markdown(
    "<h1 style='text-align: center; color: white;'>""Stablecoins: Key Roles in Blockchain & Traditional Banking""</h1>",
        unsafe_allow_html=True)
# Name on document
st.markdown("<h1 style='text-align: center; color: white; font-size: 150%'>""Guy L. Gnakpa""</h1>",
            unsafe_allow_html=True)
# Date of on documents
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>"" May 2022""</h1>",
            unsafe_allow_html=True)
# ____________________________Insert Abstract and Introduction title/body text___________________________________________
"\n"
"\n"
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>""Abstract""</h1>",
            unsafe_allow_html=True)
# subtitle "Abstract" using markdown function with html
st.write("<div style='text-align:justify'> ""\n"
         "2020-2021 was a remarkable year for cryptocurrency and the blockchain industry"
         " as a whole. The market capitalization reaching $3 billion in November 2021 was a surprisingly incredible event. While many "
         "individuals couldn't have predicted this moment, others waited patiently to witness history in the making. Who would have thought "
         "decentralized networks with a peer-to-peer architecture would be so disruptive. The fundamental idea that anybody in the world can "
         "participate in the transaction of data in a secured and robust fashion is in fact revolutionary and disruptive. Among this technical "
         "revolution exist a class of cryptocurrency known as stablecoins. At a rudimentary level, stablecoins act as settlement agents because the "
         "value can represent the traditional dollar or a respective commodity. The stablecoin asset class grew over the course of 12 months surpassing "
         "$100 billion. The growth and adoption of stablecoins can have a significant influence on the cryptocurrency market and future of finance. "
         "This document will discuss the value proposition and types of stablecoins, the impact of stablecoins on blockchain adoption, and the impact on traditional "
         "fiat rails. A clear understanding of the value and multitudes of use-cases are essential as we examine it's effect on blockchain adoption and future financial "
         "applications. The document will take a technical approach as it attempt to analyze and explain the main points mentioned. Statistical methods and reliable data will be "
         "utilised to elucidate and visualize the objectives of this document. This analysis has been completed while considering the regulatory research of stablecoins "
         "for unified ruling as they may raise concerns and opportunities for traditional markets. Note, the report should serve as a sophisticated educational tool to further comprehend the evolution "
         "happening in the distributed ledger technology and financial markets.", unsafe_allow_html=True)
# insert Introduction title and text
st.subheader("Introduction")
st.write("<div style='text-align:justify'>""\n"
         "The adoption growth of cryptocurrency, stablecoins in particular have wheeled\n"
         "the interest of many traditional market makers and market regulators worldwide. Federal Reserve Chairman, Jerome Powell said,"
         """ "One of the stronger argument for the U.S. central bank to set a digital currency is that it could undercut the need for private """
         """alternatives such as cryptocurrency and stablecoins", Reuters (Gary B. Gorton and Jeffery Y. Zhang, 2021). Federal Reserve Chairman, """
         "Jerome Powell is one of many officials who have commented on the adoption and influence of stablecoins. The demand of these digital assets "
         "has fostered an urgency for traditional markets and regulatory bodies to investigate the risks and opportunities that exist. The value proposition "
         "and utility will be defined by reporting on the various types of stablecoins. Further, a linear regression will be conducted to explore the relationship "
         "between the top stablecoin and Bitcoin. Lastly, the impact of stablecoins on centralized banking will be observed by assessing traditional institutions "
         "that are engaging with Central Bank Digital Currencies(CBDCs).", unsafe_allow_html=True)
st.markdown("""---""")
# _______________________________I.A Insert Body text for Categorical Analysis:value proposition ________________________
# Descriptive analysis
st.subheader("I. Descriptive Analysis")
st.markdown(
    "<h1 style='text-align: left; color: white; font-size: 120%'>""A. Categorical Analysis: Value Proposition & Types of Stablecoins""</h1>",
    unsafe_allow_html=True)
st.write(
    "<div style='text-align:justify'>There are many components that are associated with the value proposition offered by "
    "stablecoins. Stablecoins were originally designed to serve as stabilizer agents for crypto trading settlements. More "
    "specifically, stablecoins minimize the volatility that is associated with the cryptocurrency market. The following are some examples "
    "of value proposition currently practiced.", unsafe_allow_html=True)
"\n"
st.write("<div style='text-align:justify'>""\n"
         "\n"
         "1. ***Hedging***: against volatility is one way stablecoins have created value for the"
         "   crypto market. Many cryptocurrencies or tokens are subject to market volatility. Stablecoins hold their value to a fixed price pegged"
         "   traditionally to the dollar, commodity or a respective native token. An investor who accumulated a significant amount of capital gain on"
         "   a given principle may not want to subject the funds to future market trends. The investor can use stablecoins as a vehicle to hedge for long"
         "   or short term move against volatility that’s in the market. Cryptocurrency miners can as well use stablecoins as a hedging instrument. During Bitcoin halving(s), miners who"
         "   are inclined to liquidate their crytocurrency assets for the purchase of equipments can leverage stablecoins without loosing significant value. This action prevents"
         "   miners from exposing their total portfolio to market volatility.", unsafe_allow_html=True)
"\n"
st.write("<div style='text-align:justify'>""\n"
         "\n"
         "2. ***Remittance***: transaction is an example in which stablecoins have infiltrated\n"
         "   the traditional banking system. Sending remittance via stablecoins can save significant upside for the parties involved."
         "   The reduction of time allocation and processing fees enable stablecoins to thrive in this specific financial sector. Traditional"
         "   rails like Western Union can often take 24 hours for domestic money transfer. Internationally, this process can take one to five business"
         "   days and be significantly expensive due to intermediaries. Processing such transactions utilizing USD Coin for example can take less than 10 minutes"
         "   with lower fees than Western Union. Additionally, the currency exchange rate between regions can reduce the original value when using traditional rails. Stablecoins allow for"
         "   fast transactions while removing intermediary bodies. Participants can transact without loosing a significant value on the total fund.\n",
         unsafe_allow_html=True)
"\n"
st.write("<div style='text-align:justify'>""\n"
         "\n"
         "3. ***Capital gain***: settlement in stablecoins is a positive value transfer for investors. Traders can transfer in and out"
         "   of an asset without loosing sigificant value on trading fees. In addition, the porfolio can be protected from negative market trends.",
         unsafe_allow_html=True)
"\n"
st.write("<div style='text-align:justify'>""\n"
         "\n"
         "4. ***Reduction in trading cost***: is an added value stablecoins bring to the"
         "   digital asset and traditional markets. Stablecoins like Gemini Dollar(GUSD) and Binance USD(BUSD) enable cheaper transaction"
         "   fees than the traditional U.S. dollar during settlement of realized profits. Many stablecoins with such utility have helped increase"
         "   liquidity while creating optionality in the market.", unsafe_allow_html=True)
"\n"
st.write("<div style='text-align:justify'>""\n"
         "\n"
         "5. ***Medium of exchange***: consistently takes place in the cryptocurrency market. Naturally,"
         "   the stablecoins infrastructure have created a simpler medium of exchange. Individuals utilize stablecoins to purchase other volatile"
         "   digital assets on exchanges that support stablecoins. Web 3 platforms like Travala and fintech firms like Stripe have added stablecoins as a"
         "   medium to purchase goods and services. This trend may continue as Stablecoins become more accepted.",
         unsafe_allow_html=True)
"\n"
st.write("___")
#                   _______________________Stablecoins Categories__________________________
st.write("<div style='text-align:justify'>""\n"
         "Majority of custodial stablecoins claim to be backed by traditional reserves like fiat, treasury bonds or other commodities. As of today, there exists four type of stablecoins."
         " Most stablecoins can be found on centralized and decentralized exchanges. The most common are fiat-backed stablecoins, which most participants have access to through markets "
         "like Coinbase and Uniswap. Below are the different categories available to the public.",
         unsafe_allow_html=True)
"\n"
st.write("<div style='text-align:justify'>""\n"
         "\n"
         "1. ***Fiat-backed stablecoins***: which are commonly known to be pegged one-to-one to the value held in reserve( dollars,euros, yen, yuan etc...)."
         "\n"
         "2. ***Commodity-backed stablecoins***: are often pegged to a tangible asset like oil, gold, silver, or other precious metals. The main attraction of these"
         "   stablecoins is that they are highly liquid while representing some illiquid traditional commodities.\n"
         "\n"
         "3. ***Crypto-backed stablecoins***: are pegged to fiat; however, the collateral is a digital crypto asset native to a respective network like; Bitcoin, Ethereum and many more."
         "\n"
         "4. ***Algorithmic-backed stablecoins***: maintain the price stability through smart contract conditions and algorithms that adjust supply based on market volatility.",
         unsafe_allow_html=True)
"\n"
st.write(
    "<div style='text-align:justify'>""The figures below are examples of categorical stablecoins by market capitalization.",
    unsafe_allow_html=True)


# ______________________________________________________________________________________________________________________#
# Using a def-function Pull Data from coingecko: Top 18 stablecoins \ provide currency \store and display in dataframe
@st.cache
def API_Data_Top():
    cg = CoinGeckoAPI()  # call the coingecko API
    Top_Stablecoins_response = cg.get_coins_markets(
        ids=["tether", "usd-coin", "binance-usd", "terrausd", "dai", "frax", "magic-internet-money", "true-usd",
             "pax-gold", "neutrino", "paxos-standard", "fei-usd", "liquity-usd", "tether-gold", "husd", "mimatic",
             "gemini-dollar", "tether-eurt", "alchemix-usd", "usdx", "xsgd", "stasis-eurs", "nusd"],
        vs_currency="usd")
    return Top_Stablecoins_response


Top_Stablecoins_response = API_Data_Top()
# store and display return of function as a dataframe \ clean: Drop columns \ print new dataframe
Top_Stablecoins_df = pd.DataFrame(Top_Stablecoins_response)
Top_Stablecoins_New_df = Top_Stablecoins_df.drop(
    columns=["id", "image", "symbol", "market_cap_rank", "fully_diluted_valuation", "roi", "ath_change_percentage",
             "last_updated", "atl", "ath_date", "atl_date", "ath", "atl_change_percentage", "max_supply",
             "price_change_percentage_24h", "market_cap_change_24h", "price_change_24h",
             "market_cap_change_percentage_24h"
             ],
    axis=0)
st.dataframe(Top_Stablecoins_New_df)
# insert figure button
TopStablecoin_button = st.expander(label="figure 1.0 : Top Stablecoins Dataset")
TopStablecoin_button.write("""
    Datasource: CoingeckoAPI

    Technologies: PyCharm, CoingeckoAPI functions, Python; pandas, streamlit """)
# ___________________________________________prep variabbles to be plotted_______________________________________________#

# __________________________Fiat-Backed Stablecoins___________________________#
Fiat_Backed_Stablecoins_New_df = Top_Stablecoins_New_df[
    Top_Stablecoins_New_df["name"].isin(["Tether", "USD Coin", "Binance USD",
                                         "TrueUSD", "HUSD", "Gemini Dollar", "Pax Dollar", "Euro Tether",
                                         "STASIS EURO", "XSGD"])].sort_index(ascending=False)
# st.dataframe(Fiat_Backed_Stablecoins_New_df)
Fiat_MktCap = Fiat_Backed_Stablecoins_New_df["market_cap"].sum()
# st.write(Fiat_MktCap)
# __________________________Commodity-Backed Stablecoins___________________________#
Commodity_Backed_Stablecoins_New_df = Top_Stablecoins_New_df[
    Top_Stablecoins_New_df["name"].isin(["PAX Gold", "Tether Gold"])].sort_index(ascending=False)
# st.dataframe(Commodity_Backed_Stablecoins_New_df)
Commodity_MktCap = Commodity_Backed_Stablecoins_New_df["market_cap"].sum()
# st.write(Commodity_MktCap)
# __________________________Crypto-backed Stablecoins___________________________#
Crypto_Backed_Stablecoins_New_df = Top_Stablecoins_New_df[
    Top_Stablecoins_New_df["name"].isin(["Dai", "Magic Internet Money", "Liquity USD",
                                         "Alchemix USD", "Neutrino USD", "USDX", "sUSD"])].sort_index(
    ascending=False)
# st.dataframe(Crypto_Backed_Stablecoins_New_df)
Crypto_MktCap = Crypto_Backed_Stablecoins_New_df["market_cap"].sum()
# st.write(Crypto_MktCap)
# __________________________Algo-backed Stablecoins___________________________#
Algo_Backed_New_df = Top_Stablecoins_New_df[
    Top_Stablecoins_New_df["name"].isin(["TerraUSD", "Frax", "Fei USD", "MAI", ])].sort_index(ascending=False)
# st.dataframe(Algo_Backed_New_df)
Algo_MktCap = Algo_Backed_New_df["market_cap"].sum()
# st.write(Algo_MktCap)

# ____________________Create a Dataframe for the Calculated MarketCap _____________#
Category_MarketCap = {"StablecoinCategory": ["Fiat-backed Stablecoins", "Commodity-backed Stablecoins",
                                             "Crypto-backed Stablecoins", "Algorithmic-backed Stablecoins"],
                      "MarketCapitalization": [Fiat_MktCap, Algo_MktCap, Crypto_MktCap, Commodity_MktCap]}
Category_MarketCap_df = pd.DataFrame(Category_MarketCap)  # .sort_index(ascending=False)
# st.dataframe(Category_MarketCap_df)
# ________________________________________________Using plotly display bar charts______________________________________#
st.markdown("<h1 style='text-align: center; font-size: 100%'>Stablecoins Categories</h1>", unsafe_allow_html=True)
# Initiate figure with subplot
fig = make_subplots(rows=2, cols=2, subplot_titles=(
    "Fiat-backed Stablecoins",
    "Commodity-backed Stablecoins",
    "Crypto-backed Stablecoins",
    "Algorithmic-backed Stablecoins"),
                    vertical_spacing=0.35,
                    horizontal_spacing=0.25)
# Add Needed Traces
fig.add_trace(go.Bar(x=Fiat_Backed_Stablecoins_New_df["name"], y=Fiat_Backed_Stablecoins_New_df["market_cap"]),
              row=1, col=1, )
fig.add_trace(
    go.Bar(x=Commodity_Backed_Stablecoins_New_df["name"], y=Commodity_Backed_Stablecoins_New_df["market_cap"]),
    row=1, col=2)
fig.add_trace(go.Bar(x=Crypto_Backed_Stablecoins_New_df["name"], y=Crypto_Backed_Stablecoins_New_df["market_cap"]),
              row=2, col=1)
fig.add_trace(go.Bar(x=Algo_Backed_New_df["name"], y=Algo_Backed_New_df["market_cap"]), row=2, col=2)
fig.update_layout(width=1350, height=700, plot_bgcolor='rgba(0,0,0,0)')
# Update xaxis properties
fig.update_layout(showlegend=False)
fig.update_xaxes(showgrid=False, tickangle=90, row=1, col=1)
fig.update_xaxes(showgrid=False, tickangle=90, row=1, col=2)
fig.update_xaxes(title_text="Stablecoins", showgrid=False, tickangle=90, row=2, col=1)
fig.update_xaxes(title_text="Stablecoins", showgrid=False, tickangle=-90, row=2, col=2)
# Update yaxis properties
fig.update_yaxes(title_text="Market Capitalization($)", showgrid=False, row=1, col=1)
fig.update_yaxes(title_text="Market Capitalization($)", showgrid=False, row=1, col=2)
fig.update_yaxes(title_text="Market Capitalization($)", showgrid=False, row=2, col=1)
fig.update_yaxes(title_text="Market Capitalization($)", showgrid=False, row=2, col=2)
# fig.show()
st.plotly_chart(fig)

# insert figure button
Stablecoin_Categ_button = st.expander(label="Figure 1.1A - 1.1D : Stablecoins by Categories")
Stablecoin_Categ_button.write("""
1.1A: Fiat Stablecoin

1.1B: Commodity-backed Stablecoins

1.1C: Crypto-backed Stablecoins

1.1D: Algorithmic-backed Stablecoins

Datasource: CoingeckoAPI

Technologies: PyCharm, Python; plotly subplots, pandas, streamlit, """)

# Display the various stablecoins category and  marketcaps
Categ_Visual1 = px.bar(data_frame=Category_MarketCap_df, x=["MarketCapitalization", "StablecoinCategory"],
                       y="StablecoinCategory",
                       color="StablecoinCategory", orientation="h", barmode="stack", width=1290, height=250, )
# Update xaxis properties
Categ_Visual1.update_xaxes(title_text="Market Capitalization($)", showgrid=True)
# Update yaxis properties
Categ_Visual1.update_yaxes(title_text="Categories")
Categ_Visual1.update_layout(legend_title="Stablecoin Categories", plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(Categ_Visual1)
# insert figure button
Categ_Visual1_button = st.expander(label="Figure 1.2 : Stablecoins Categories by Market capitalization ")
Categ_Visual1_button.write("""
Datasource: CoingeckoAPI

Technologies: PyCharm, Python; plotly express, pandas, streamlit""")
# ___________________#Bar charts Body Text description_________________________________#
st.write("<div style='text-align:justify'>""\n"
         "Looking at the examples provided above, the data suggests the Fiat-backed category is the most valuable category representing"
         " more than $140 billion based on the market capitalization. Within the Fiat-backed category, the token Tether occupies most"
         " of the market shares with a market capitalization of roughly $75 billions. Although the Commodity-backed categogy has only two"
         " tokens, Pax Gold has a high market capitalization of more than $601 million versus Tether Gold hovering around $458 million."
         " There exists large domiance when observing the Crypto-backed stablecoins category. Within the five examples given, the Dai token by far has"
         " the largest market capitalization of approximately $6 billion. The token sUSD hold the smallest market capitalization of about $91"
         " million. Lastly, the Algorithmic-backed stablecoins category also displays a large dominance effect. Frax proves to hold the largest"
         " market capitalization of about $1.5 billion, while MAI holds the smallest market capitalization of roughly $269.5 million. It is important "
         "to note the market capitalizations expressed for these categories are not fixed and suggest to change based on the market demand. The interpretation of the"
         " numerical values and ranking of each token correlates to the time in which the document is written (live data).\n",
         unsafe_allow_html=True)
# ___________________________________I.B Trend Analysis: Bitcoin vs. Tether______________________________________________
st.markdown(
    "<h1 style='text-align: left; color: white; font-size: 120%'>""B. Trend Analysis: Bitcoin vs Tether ""</h1>",
    unsafe_allow_html=True)
st.write("<div style='text-align:justify'>""\n"
         "Bitcoin has been the most dominant cryptocurrency since its inception. Despite the fluctuation of percentage dominance"
         " due to market volatility, Bitcoin has held a significant percentage of the total liquidity available on the market for years."
         " More than often the cryptocurrency market follows the bitcoin trend. The above categorical analysis indicates Tether is the most"
         " liquid among all stablecoins. A time series analysis between the total volumes of Bitcoin and Tether can be conducted to explore"
         " any existing relationships. Exploring the volume as opposed to the price can better demonstrate the trend of supply and demand.",
         unsafe_allow_html=True)
"\n"
st.write("<div style='text-align:justify'>""\n"
         "Figure 1.3 below, is a line graph expressing the trend between the total volumes of Bitcoin and Tether from January 2, 2020 to April 3,"
         " 2022. At a fundamental level, both Bitcoin and Tether display some characteristics of seasonality. Further, the graph indicates Tether has"
         " more volume than Bitcoin at a consistent level for the chosen time period. The figure shows one event when the daily Bitcoin volume is greater"
         " than Tether's volume. On September 6th 2020, the total volume for Bitcoin was $56.43 billion, while Tether's volume was $53.09 billion."
         " From the given data, the daily Bitcoin volume surpassed Tether's volume by $3.34 billion. Aside from Bitcoin's one event of daily volume significance,"
         " Tether's daily volume has dominated for the given time period. From November 16, 2020 to May 27 2021, Tether's volume indicates a positive trend. Whithin"
         " that time period, there were five all-time high peaks, whithout a pull-back to the daily volume of November 16, 2020. On November 27 2020, the daily volume was"
         " $81.12 billion. The next all-time high of daily volume is $116.09 billion on January 9, 2021. Followed by a peak on February 10, 2021 with a significant"
         " volume of $120.39 billion. The trend continues on April 13, 2021 with a daily volume of $123.52 billion dollars. Lastly, on April 27th 2021, the all-time high surpasses"
         " the previous with a daily volume of $124.92 billion before a significant pullback.\n",
         unsafe_allow_html=True)
# _____________________________________Import GoingeckoAPIexcel file_____________________________________________________
# import data
BTC_USDT_DF = pd.read_excel("Data_XLSX_Files/Stablecoins.xlsx")
# ______________________________________CLean Data for Trend and Regression Analysis____________________________________
# check data before outlier -> NUll
Null_check = BTC_USDT_DF.isnull().sum()


#                           ________#Define a function to treat columns simultaneously_________
# first ID the outlier that are behond the UL and LL limits
@st.cache_data
def Outlier_limits(col):
    Q3, Q1 = np.nanpercentile(col, [75, 25])
    IQR = Q3 - Q1
    Upper_limit = Q3 + 1.3 * IQR
    Lower_limit = Q1 - 1.3 * IQR
    return Upper_limit, Lower_limit


# st.write(Outlier_limits)
#                               _____________Convert the Outlier to Missing values_________
for column in BTC_USDT_DF.columns:
    if BTC_USDT_DF[column].dtype != "object":
        Upper_limit, Lower_limit = Outlier_limits(BTC_USDT_DF[column])
        BTC_USDT_DF[column] = np.where((BTC_USDT_DF[column] > Upper_limit) | (BTC_USDT_DF[column] < Lower_limit),
                                       np.nan, BTC_USDT_DF[column])

#                      _______Check for missing Values|There are zero missing values_______
# check data after outlier -> NUll
SL_Null_check2 = BTC_USDT_DF.isnull().sum()
# st.write(Null_check2)
#       ______Conduct Treatment of missing(outliers) values via KNNImputerAlgo___________
# Create a copy of the original df and apply KNN method
BTC_USDT_DF_KNN = BTC_USDT_DF.copy()
knn = KNNImputer()
BTC_USDT_DF_KNN.iloc[:, :] = knn.fit_transform(BTC_USDT_DF_KNN)
# check for Null after KNN treatment
Null_check3 = BTC_USDT_DF_KNN.isnull().sum()
# st.write(Null_check3)
# _________________________________________Plot Line Chart for Trend Analysis____________________________________________
# change unix format into datetime format
BTC_USDT_DF_KNN["Timestamp"] = pd.to_datetime(BTC_USDT_DF_KNN["Timestamp"], unit="ms").dt.date
# Plot the data above
x2 = pd.DataFrame(BTC_USDT_DF_KNN)
BTC_USDT_Plot = px.line(x2, x="Timestamp",
                        y=["Bitcoin Total Volumes", "Tether Total Volumes", "USD Coin Total Volumes",
                           "Pax Gold Total Volumes"],
                        title="BTC and USDT Total Volumes From Jan 2020-April 2022")
BTC_USDT_Plot.update_layout(legend_title="Digital Assets", width=1300, height=450, title_x=0.5, title_y=.85,
                            plot_bgcolor='rgba(0,0,0,0)')
BTC_USDT_Plot.update_xaxes(showgrid=False, title="Date")
BTC_USDT_Plot.update_yaxes(showgrid=True, title="Daily Volume($)")
st.plotly_chart(BTC_USDT_Plot)
#      ____________Insert Body Text for Metric Visuals of Daily Volume % Growth between Nov2020-May2021________
st.write("<div style='text-align:justify'>""\n"
         "The metrics highlighted below, show a significant increase in the daily trading volume of Tether. From November 16th 2020 to April 27th 2021, Tether's daily volume"
         " increased by approximately 54%. In a matter of 5 months, the daily trading volume grew incredibly. After a significant correction, the market ajusted to a much lower volume"
         " of $32.36 billion as displayed on the line chart above.\n", unsafe_allow_html=True)
#      ____________Insert Metric visuals of Daily Volume % Growth between Nov2020-May2021_______________
"\n"
col1 = 81.12
col2 = 124.92
col3 = format((col2 - col1), ".2f")
Nov_2020_Col, May_2021_col2, N_months, DailyVolume_PercentChange_col3 = st.columns(4)
Nov_2020_Col.metric("Nov 16,  2020 Daily Volume($)", "81.12B")
May_2021_col2.metric("April 27, 2021 Daily Volume($)", "124.92B")
N_months.metric("Number of Months", "5")
DailyVolume_PercentChange_col3.metric(label="∆ in Daily Volume(%)", value="43.8B",
                                      delta=format(((col2 - col1) / (col1) * 100), ".2f"))
# insert figure button
BTC_USDT_Plot_button = st.expander(label="figure 1.3 : BTC and USDT line Graph")
BTC_USDT_Plot_button.write("""
Datasource: CoingeckoAPI

Disclaimer: Data was treated for outliers using KNNImputer Algorithm

Technologies: PyCharm, API functions, Python; plotly express, pandas, numpy sklearn.Impute, streamlit """)
st.write("___")
# ___________________________________II. Predictive Analysis: Bitcoin vs. Stablecoins _________________________________________
# Insert Title/Body Text
st.subheader("II. Predictive Analysis: Bitcoin vs. Stablecoins ")
st.write("<div style='text-align:justify'>""\n"
         " The demand for stablecoins have increased its supply and volume in the past several months. With that in mind, the questions remains, "
         " does the trading volume of Stablecoins influence the volume of Bitcoin and to what degree of significance? "
         " The question can be observed through a first principle framework by utilizing the technique of simple linear regression."
         " Although figure 2.0 displays many variables, the daily volume for Bitcoin and Tether are the two variables needed to conduct the "
         "regression. Bitcoin will be the dependent variable (response) while Tether will act as the independent variable (predictor). Figure 2.0 "
         "shows the dataset extracted from CoingeckoApi for the regressions.", unsafe_allow_html=True)
"\n"
# insert the respective dataset
st.dataframe(BTC_USDT_DF_KNN)
#              ______________Insert summary statistics Body Text & Graphs_______________
st.write("<div style='text-align:justify'>""\n"
         "The table below is a summary statistics derived from the original dataset. All the variables have "
         " the same number of data ; 821 observations. Among the observations, the variable with the largest mean value is Tether; $59.46 "
         "billion. TerraUSD holds the minimum value of $16.19 billion, while Tether representing the largest median value at $54.35 billion. "
         "Lasly, Tether holds the largest maximum value of $124.92 billion. As illustrated, Tether's daily total volume dominate in every "
         "level (except minimum value) compared to the rest of the variables.", unsafe_allow_html=True)

# insert descriptive summary
Desc_BTC_USDT_DF = BTC_USDT_DF_KNN.describe()
"\n"
st.table(Desc_BTC_USDT_DF)
# insert figure button
Dataset_button = st.expander(label="Figure 2.0 - 2.1 : Stablecoins Regression Dataset & Summary Statistics")
Dataset_button.write("""
Figure 2.0: Stablecoins Regression Dataset

Figure 2.1 : Summary Statistics

Datasource: CoingeckoAPI

Disclaimer: Data was treated for outliers using KNNImputer Algorithm

Technologies: PyCharm, CoingeckoApi, Python; KNNImputer, pandas, streamlit""")

#                   ____________#insert Simple Linear Regression title&Body Text________________
st.markdown(
    "<h1 style='text-align: left; color: white; font-size: 120%'>""A. Simple Linear Regression: Bitcoin vs Tether""</h1>",
    unsafe_allow_html=True)
# Insert Histogram Plot Body Text
st.write("<div style='text-align:justify'>""\n"
         "Before the model implementation, let's first observe the data's frequency distribution through a histogram. Figure 2.1A"
         " below, is a histogram showcasing value distribution of both variables. Tether's values are represented in the blue color,"
         " while Bitcoin's values are represented in red. The x-axes holds both the BTC and USDT values. The y-axes represents the "
         "frequency. The histogram appears to be asymmetrical due to the right-skewed distribution (positive skewed distribution). "
         "More specifically, the Bitcoin's distribution shows left truncation. This distribution indicates the mean, median and mode are much different."
         " Unlike a normal distribution with equal mean, median and mode, the positive skewed distribution tend to be less predictable. The dataset skews "
         "to the right much more for Tether because the lower bounds are much smaller values relative to the complete dataset. With better understanding of the data frequency distribution,"
         " the next graphs can be plotted.", unsafe_allow_html=True)
#                           __________________Insert all respect plots___________________
SL_Reg = BTC_USDT_DF_KNN
# Plot Histogram
Reg_BTC_USDT_Hist_DF = px.histogram(SL_Reg[["Tether Total Volumes", "Bitcoin Total Volumes"]],
                                    title="Histogram of BTC and USDT Volume", range_x=[-10, 350000000000])
Reg_BTC_USDT_Hist_DF.update_layout(legend_title="Digital Assets", width=1300, height=450, title_x=0.5, title_y=.85,
                                   plot_bgcolor='rgba(0,0,0,0)')
Reg_BTC_USDT_Hist_DF.update_xaxes(showgrid=False, title="BTC and USDT Volume($)")
Reg_BTC_USDT_Hist_DF.update_yaxes(showgrid=True, title="Frequency")
st.plotly_chart(Reg_BTC_USDT_Hist_DF)
# Insert Scatter Plot Body Text
st.write("<div style='text-align:justify'>""\n"
         "Figure 2.1B is a scatter plot illustrating the daily volume distribution between Bitcoin and Tether. Bitcoin's values are "
         "represented on the y-axes in billions. Tether's daily trading volumes are represented on the x-axes in billions as well. "
         "The plot shows significant characteristics of a positive correlation between the two digital assets. It is clear both variables "
         "are rising and moving to the right in a positive direction. Lastly, the distribution does not demonstrate data points far beyond "
         "majority of the cluster, thus lowering the risks of outliers. The next plot will confirm if any outliers exist.",
         unsafe_allow_html=True)
# Plot Scatter plot(Bitcoin)
Reg_BTC_USDT_Scatter_DF = px.scatter(SL_Reg, x="Tether Total Volumes", y="Bitcoin Total Volumes",
                                     title="Scatter Plot of BTC and USDT Volume")  # trendline="ols"
Reg_BTC_USDT_Scatter_DF.update_layout(width=1300, height=450, title_x=0.5, title_y=.85,
                                      plot_bgcolor='rgba(0,0,0,0)')  # width=1000, height=450,
Reg_BTC_USDT_Scatter_DF.update_xaxes(showgrid=False, title="Tether Volume($)")
Reg_BTC_USDT_Scatter_DF.update_yaxes(showgrid=False, title="Bitcoin Volume($)")
st.plotly_chart(Reg_BTC_USDT_Scatter_DF)
# Insert BoxPlot Body Text
st.write("<div style='text-align:justify'>""\n"
         "Figure 2.1C is a boxplot to better visualize the potential existing outliers. In the both distributions, the plot shows "
         "the median of the data is slightly closer to 25th quantile as also indicated in the histogram. This event signifies the data is slightly skewed and not symmetrical."
         " The distribution has no data points within or beyond either whiskers. Essentially, there are no outliers based on the boxplot.",
         unsafe_allow_html=True)
# Insert a Outlier Boxplot
Reg_BTC_USDT_BoxPlot_DF = px.box(SL_Reg, y=["Bitcoin Total Volumes", "Tether Total Volumes", ],
                                 title="Box Plot of BTC and USDT Volume",
                                 notched=True)  # color="Tether Total Volumes",
Reg_BTC_USDT_BoxPlot_DF.update_layout(width=1300, height=450, title_x=0.5, title_y=.85,
                                      plot_bgcolor='rgba(0,0,0,0)')  # width=1000, height=450,
Reg_BTC_USDT_BoxPlot_DF.update_xaxes(showgrid=False, title="Digital Assets")
Reg_BTC_USDT_BoxPlot_DF.update_yaxes(showgrid=False, title="Volume($)")
st.plotly_chart(Reg_BTC_USDT_BoxPlot_DF)
# insert model implementation info
st.info(
    "The model below is implementated using Ordinary Least Squared to attempt to quantify the level of significance between the relationship of the BTC volume and USDT volume. ")
# Inser Simple Linear Regression formula
st.markdown(
    "<h1 style='text-align: center; color: white; font-size: 120%'>"" ŷ= Bitcoin Total Volume, b0 = y-intercept , x1 =Tether Total Volume, e =  Error Term  ""</h1>",
    unsafe_allow_html=True)
st.markdown(
    "<h1 style='text-align: center; color: white; font-size: 120%'>"" Bitcoin Total Volume = Y-Intercept + Tether Total Volume + Error Term ""</h1>",
    unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>"" ŷ  = b0 + b1x1 + e  ""</h1>",
            unsafe_allow_html=True)
st.markdown(
    "<h1 style='text-align: center; color: white; font-size: 120%'>"" ŷ  = 7.8221e+09 + 0.47489 Tether Total Volume ""</h1>",
    unsafe_allow_html=True)

#                             ______________Conduct Simple Regression & Body Text________________
SL_Reg2 = SL_Reg.copy()
x_variable = SL_Reg2["Tether Total Volumes"]
y_variable = SL_Reg2["Bitcoin Total Volumes"]
x_variable = sm.add_constant(x_variable)
Model_1 = sm.OLS(y_variable, x_variable).fit()
st.write(
    # Model_1.params,
    # Model_1.summary()
)
SLRegression_imge = Image.open("Data_PNG_JPG_Files/SLRegression1.png")
# Create/Insert col for Reg output and interpretation
SL_col1, SL_col2, = st.columns(2)
with SL_col1:
    st.image(SLRegression_imge, width=700)
with SL_col2:
    st.info("""
***Result Overview***: The results of the OLS linear regression model is on the left in figure 2.1D. The data was tested for outliers through clear logic. Existing outliers were transformed to null values. All null values were treated using an KNNImputer algorithm.
The Data was tested for multicollinearity using a VIF method. A result of 5 indicated moderate level and no treatment was necessary.

***Key Metrics***: The R-squared and Standard Error of Regression (S) are important metrics to observe and interpret when conducting a regression. The R-Squared explains the variation in y = (Bitcoin volume).
S explains the distance the data falls from the regression line as displayed below. Figure 2.1E shows the predictive trend line and the equation.

***Result Interpretation***: The coefficient of determination(R-Squared) is .72. Tether's volume explains 72% of the total variation in the Bitcoin volume.
The S value and predictive regression line below indicate a significant number of data points fall on the regression line and near it.
Each additional added volume of Tether is correlated with an average increase of 0.4748(coefficient) in Bitcoin volume based on the slope. Further, the t-stat associated
with the respective p-value remains at 0. In conclusion, the standard error of the regression slope is smaller than the coefficient making Tether's volume
statistically significant in relation to Bitcoin's volume.""")

#                   ______________Insert Scatter PLot & Trend line For SL_Reg_____________
# Plot Scatter plot(Tether)
Reg_BTC_USDT_Scatter_DF = px.scatter(SL_Reg2, x="Tether Total Volumes", y="Bitcoin Total Volumes", trendline="ols",
                                     title="Scatter Plot of BTC and USDT(Trend Line)",
                                     trendline_color_override='white', color="Tether Total Volumes", )
Reg_BTC_USDT_Scatter_DF.update_layout(width=1300, height=450, title_x=0.5, title_y=.85,
                                      plot_bgcolor='rgba(0,0,0,0)')  # width=1000, height=450,
Reg_BTC_USDT_Scatter_DF.update_xaxes(showgrid=False, title="Tether Volume($)")
Reg_BTC_USDT_Scatter_DF.update_yaxes(showgrid=False, title="Bitcoin Volume($)")
st.plotly_chart(Reg_BTC_USDT_Scatter_DF)
# insert a correlation matrix table
corrMatrix_0 = pd.DataFrame(BTC_USDT_DF_KNN,
                            columns=["Bitcoin Total Volumes", "Tether Total Volumes", "USD Coin Total Volumes",
                                     "Pax Gold Total Volumes", "Dai Total Volumes", "TerraUSD Total Volumes"])
corrMatrix = corrMatrix_0.corr()
Corr_fig = px.imshow(corrMatrix)
Corr_fig.update_layout(width=1230, height=450)
st.plotly_chart(Corr_fig)

# insert figure button
SLReg_button = st.expander(label="Figure 2.1A - 2.1F : Visual Plots & OLS Regression Results")
SLReg_button.write("""
Figure 2.1A: Histogram of BTC and USDT Volume

Figure 2.1B: Scatter Plot of BTC and USDT Volume

Figure 2.1C: Box Plot of BTC and USDT Volume

Figure 2.1D: OLS Regression Results

Figure 2.1E: Scatter Plot of BTC and USDT Volume(Trend Line)

Figure 2.1E: Heatmap of Digital Assets

Datasource: CoingeckoAPI

Disclaimer: Data was treated for outliers using KNNImputer Algorithm

Technologies: PyCharm, CoingeckoApi, Python; statsmodels.api, KNNImputer, plotly express, pandas, streamlit""")

# insert a correlation matrix table
st.write("___")
# _______________________________________III. Stablecoins & Fiat rails  _________________________________________________
# Insert Title & Body text
st.subheader("III. S.W.O.T Analysis: Central Bank Digital Currencies")

st.write("<div style='text-align:justify'>""\n"
         "Distributed Ledger Technology has given rise to a multitude of digital asset applications particularly in the financial sector. "
         "Blockchain, derived from DLT, solved the doubled-spending problem enabling the prevention of data minipulation and payment authentication. "
         "The most powerful aspect of the technology is the transparency of the digital ledger, aka, data record. Any participant who is part of the "
         "network can view any public transactions stored on the network. The implication of the technology is disruptive for many intermediary institutions "
         "like brokers, settlement agencies and independent third-party verification. When mentioning stablecoins, it is without thinking of Central Bank Digital Currencies. "
         "The efficiency and immutability for a central bank-issued digital cash has proppeled nations worldwide to seriously investigate the opportunities and risk exposure if fully adopted. "
         "For years now, many nations and regulatory bodies have began research or implemented a pilot version of a government-issue stablecoin. Conducting a S.W.O.T analysis can "
         "help deepen the understanding of the risks and opportunities associated with the use of CBDCs.",
         unsafe_allow_html=True)

# Insert Strength title & body text
st.markdown("<h1 style='text-align: left; color: white; font-size: 120%'>""A. Strengths</h1>",
            unsafe_allow_html=True)
st.write("<div style='text-align:justify'>""\n"
         "Central bank stablecoins, CBDCs, can have a significant influence on the market as they serve as legal tender being they are already pegged "
         "to the existing central bank notes. When compared to traditional private bank deposits, CBDCs are a risk free alternative. This without a doubt is "
         "a competitive advantage compared to other forms of stablecoins. The issuance of CBDCs by a central bank can expand financial inclusion. Many regions in "
         "the U.S and in emerging nations lack access to financial banking vehicles. Accompanied with financial inclusion, participants can experience better efficiency in the "
         "payment system as opposed to the legacy system. For decades, the cost of conventional digital payment options like credit and debit card has been expensive with little innovation. "
         "CBDCs can be credit risk free for participants as they are directly coming from central bank. The reduction of a multitude of intermediary bodies can cut transaction fees and create "
         "more savings for the individual. Faster and better cross border payments would be an added strength to CBDCs. A study conducted by many financial institutions like Central Bank of Canada, "
         "Singapore and the UK has concluded CBDCs have the potential to reduce counterparty credit risk regarding cross-border payments. In that specific regard, countries that previously couldn't "
         "trade with other nations would then have access to new trade avenues while reducing the friction of foreign currency exchange rates. In totality, risks associated with the collapse of commercial bank "
         "and national hyperinflation can be eliminated. Although many strengths of CBDCs have been mentioned, many more will surface as more research and experimemts are completed by regulatory bodies. "
         "The figure 3.0, displays the types of Central Bank Digital Currencies. ", unsafe_allow_html=True)
"\n"
"\n"
# insert CBDCs Architecture
CBDC_col1, CBDC_col2, = st.columns(2)
with CBDC_col1:
    CBDC_image0 = Image.open("Data_PNG_JPG_Files/CBDC Architecture3.png")
    st.image(CBDC_image0, width=645)
with CBDC_col2:
    st.info("""
    Figure 3.0: CBDC Models. Expand picture for better visual. 

    ***Wholesale CBDCs***: facilitate payment and settling transactions between financial institutions for the purchase of
    assets and services. Ideally Wholesale CBDCs could replace the Real-Time Gross Settlement systems. Some are restricted to the regional
    issuer while others can be interoperable.

    ***Retail CBDCs***: focuses on day-to-day transactions for good and services by non-enterprise. Retail CBDCs can even be a vehicle 
    for public capital distribution during economic uncertainty.Retail CBDCs can be distributed directly to the consumer,
    though intermediary parties or a mixture of both techniques.""")

# Insert Weaknesses title & body text
st.markdown("<h1 style='text-align: left; color: white; font-size: 120%'>""B. Weaknesses</h1>",
            unsafe_allow_html=True)
st.write("<div style='text-align:justify'>""\n"
         "Well constructed CBDCs will have to iron key issues that are raising many concerns today. Primarily, Central Banks will have full control over CBDCs. "
         "With a centralized framework, central banks can restrict or influence the types of transactions permitted. In a long term this can be unsettling for all participants and  "
         "reduce confidence in the CBDC and its issuer. Further, central powers will have enormous data through the ledger. A clear ethical framework of data collection and data governance by central powers "
         "will have to be addressed to mitigate privacy concerns. Knowing education often fosters adoption, many individuals who do not have adequate resources may fall behind the DLT adoption curve. Central powers may need to "
         "take on the responsibility of educating the masses and promoting financial inclusion. The benefit of utilizing CBDCs are inherently great; however, many intermediary agencies like; small commercial banks, lenders and brokers "
         "could be significantly affected by the transition. Beyond the examples mentioned, there are many other weaknesses or concerns to be addressed by central banks in the years to come.",
         unsafe_allow_html=True)

# Insert Opportunity title & body text
st.markdown("<h1 style='text-align: left; color: white; font-size: 120%'>""C. Opportunities</h1>",
            unsafe_allow_html=True)
st.write("<div style='text-align:justify'>""\n"
         "The demand for blockchain technology and digital assets has open a space for many opportunities. CBDCs have the chance to modernize the legacy banking system."
         "As previously expressed fast, cheaper, and more secure transactions would be the standard for payments and financial services if CBDCs are adopted throughout different markets. This would be a clear opportunity to shift to a cashless system."
         """Further, it is important to consider the vast number of unbanked individuals who still wish to participate in the financial market. According to Global Findex Database, "Globally about 1.7 billion adult remains """
         """unbanked--without an account at a financial institution or through a mobile money provider. In 2014 that number was 2 billion." At a local level, "5.4 percent of U.S. households (~ 7.1 million) were unbanked in 2019, meaning"""
         """ no one in the household had a checking or savings account at a bank or credit union" (FDIC, 2021,"How America Bank: Household Use of Banking and Financial Services)." There, lies an opportunity for CBDCs to onboard billions of people into """
         "a modern financial system. In return, the economy can increase in saving deposits. Once disposable income increases, individuals have more optionality for quality of living and spending. Emerging nations like Haiti, Zimbabwe, Nigeria, Ecuador and Ghana are regions "
         "that can benefit greatly from CBDCs as their native currencies often fall victim to hyperinflation and geopolitical events. An inclusive and efficient CBDC that has proper governance can certainly change the lives of billion individuals. Many nations have considered "
         "adopting to their own CBDC. Figure 3.1A shows an interactive dashboard of countries who have shown interest or begun testing CBDCs.",
         unsafe_allow_html=True)

# Insert Threats body text
st.markdown("<h1 style='text-align: left; color: white; font-size: 120%'>""D. Threats</h1>", unsafe_allow_html=True)
st.write("<div style='text-align:justify'>""\n"
         "Beyond all opportunities, there exists a large number of threats for central digital currencies. First and formost, decentralized ledger technologies have proven a significant level of security depending on the consensus protocol. "
         "While that holds to be true, cybersecurity remains the largest threat of CBDCs. Any database or digital payment system falls prey to cybersecurity attacks like; data breaches, account theft, and counterfeiting. There has already been "
         "numerous events of digital currencies experiencing large liquidation due to a weakness in the network. CBDCs will have to be constructed in a robust way to instill confidence in its security. Next, users with privileged rolls can be a thread to CBDCs. "
         "In the current payment system, central authorities have the privilege to authorize or deny transactions as part of compliance. The same behavior or action can take place with CBDCs compliance. Based on the consensus, central authorities or third parties whom have privileged actions "
         "must prevent internal bias or malicious action. Lastly, too many intermediary enterprises can increase the level of risk if not properly vetted. As there are many versions of CBDCs (figure 3.0), indirect retail CBDCs controlled by multitude of payment service providers will have to implement sound "
         "cybersecurity risk management for the benefit of all stakeholders. At last, there are many other significant threats to CBDCs; however, cybersecurity holds supreme. Figure, 3.1A below shows an interactive dashboard of nations interested in CBDCs. ",
         unsafe_allow_html=True)
"\n"
st.info(" ")

#                               _________#Insert Tableau Dashboard__________
Tableau_embedded_value = """
<div class='tableauPlaceholder' id='viz1653292527042' style='position: relative'>
    <noscript>
        <a href='#'>
        <img alt='Central Bank Digital Currencies Dashboard ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;te&#47;test_16530957433120&#47;Dashboard1&#47;1_rss.png' style='border: none' />
        </a>
        </noscript>
        <object class='tableauViz' style='display:none;'>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
        <param name='embed_code_version' value='3' /> 
        <param name='site_root' value='' />
        <param name='name' value='test_16530957433120&#47;Dashboard1' />
        <param name='tabs' value='no' /><param name='toolbar' value='yes' />
        <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;te&#47;test_16530957433120&#47;Dashboard1&#47;1.png' /> 
        <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                
        <script type='text/javascript'> 
        var divElement = document.getElementById('viz1653292527042');var vizElement = divElement.getElementsByTagName('object')[0]; 
            if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='727px';} 
                else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='727px';} 
                    else { vizElement.style.width='100%';vizElement.style.height='1177px';} 
                    var scriptElement = document.createElement('script'); 
                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js'; 
                    vizElement.parentNode.insertBefore(scriptElement, vizElement); 
        </script>"""
components.html(Tableau_embedded_value, width=9000, height=700)

# insert figure button
SLReg_button = st.expander(label="Figure 3.0 - 3.1A : CBDC Models & CBDCs Dashboard")
SLReg_button.write("""
Figure 3.0: CBDCs Models Architecture

Figure 3.1A: Central Bank Digital Currencies Interactive Dashboard

Datasource: CoingeckoAPI, cbdctracker.org

Technologies: PyCharm, CoingeckoApi, Tableau, Miro Visual Whiteboard, Streamlit""")

# insert a correlation matrix table
st.write("___")
# _________________________________________________IV. Conclusion________________________________________________________
# Insert Stablecoins risks: Title and body text
st.subheader("IV. Conclusion: Risk Analysis")
st.markdown(
    "<h1 style='text-align: left; color: white; font-size: 120%'>""A. Stablecoin Risks: Lack of Reserves </h1>",
    unsafe_allow_html=True)
st.write("<div style='text-align:justify'>""\n"
         "Traditional stablecoins have shown lots of promises for the near future. The capibility for stablecoins to become mainstream has raised a primary concern for its reverse mechanism. Many individuals fear "
         "stablecoins are not fully backed by reserve currencies they claim. A stablecoin that is not sufficiently backed by cash, bank deposits, treasury bills, commodities or corporate bonds can experience detrimental liquidation events. "
         "This is a critical risk that can affect the greater crypto market. Algorithmic-backed stablecoins are the most susceptable to such vulnerability. A clear example of this concern has been examplified by the stablecoin TerraUSD. "
         "TerraUSD by Terrafor Labs is an algorithmic-backed stablecoin that collapsed with a loss of approximately $45 billion, including Terra Luna (native token), in less than seven days. The lack of reserves, risky stabilizer protocol and fixed high yield of its governance token(LUNA) led to de-risking pressure. "
         " A domino-effect of selling pressure caused many investors to lose life savings. This event is considered to be one of the most catastrophic in the history of cryptocurrency. In figures 5.0 and 5.1A, one graph shows the volume collapse of TerraUSD while the other shows the price collapse of its governance token Terra Luna. "
         " A correlation between the stablecoins's volume and governance token is evident. On May 6th, 2022 theres a massive retracement on both graphs. There seem to be an injection of liquidity in TerraUSD on May 7th, 10th and 12th, however; "
         " the sell off continued and Terra Luna kept dumping. The $1 stablecoin has been de-pegged from the US dollar since May 9th, 2022 and is currently trading below $0.10. The governance token, Terra Luna, was once trading at $116.29, today the same token is trading bellow $0.003. "
         "This collapse could very well be a foreshadowing for many Algorithmic-backed stablecoins if the system is not well constructed and has inadequate reserves.",
         unsafe_allow_html=True)


#                              _________Call API for TerraUSD and Terra Luna___________
# CallAPI/Select the needed columns

def API_TerraUSD():
    cg = CoinGeckoAPI()  # call the coingecko API
    TerraUSD_history = cg.get_coin_market_chart_by_id(id="terrausd", vs_currency="usd", days=365)
    TerraUSD_history_DF = pd.DataFrame(TerraUSD_history["total_volumes"])
    TerraUSD_history_DF = TerraUSD_history_DF.rename(columns={0: "Timestamp", 1: "TerraUSD Volume"})
    return TerraUSD_history_DF


TerraUSD_history_DF = API_TerraUSD()


def API_TerraLuna():
    cg = CoinGeckoAPI()  # call the coingecko API
    TerraLuna_history = cg.get_coin_market_chart_by_id(id="terra-luna", vs_currency="usd", days=365)
    TerraLuna_history_DF = pd.DataFrame(TerraLuna_history["prices"])
    TerraLuna_history_DF = TerraLuna_history_DF.rename(columns={0: "Timestamp", 1: "Terra Luna Price"})
    return TerraLuna_history_DF


TerraLuna_history_DF = API_TerraLuna()

# Combine Tables
UST_LUNA_DF = TerraUSD_history_DF
UST_LUNA_DF["Terra Luna Price"] = TerraLuna_history_DF[["Terra Luna Price"]]
UST_LUNA_DF["Timestamp"] = pd.to_datetime(UST_LUNA_DF["Timestamp"], unit="ms").dt.date

#                              _____________Insert line graph of TerraUST/Luna___________
UST_DF_PLOT = px.line(UST_LUNA_DF, x="Timestamp", y=["TerraUSD Volume"],
                      title="TerraUSD Volume")
UST_DF_PLOT.update_layout(legend_title="Digital Asset", width=1300, height=450, title_x=0.5, title_y=.85,
                          plot_bgcolor='rgba(0,0,0,0)')
UST_DF_PLOT.update_xaxes(showgrid=False, title="Date")
UST_DF_PLOT.update_yaxes(showgrid=True, title="Daily Volume($)")
st.plotly_chart(UST_DF_PLOT)

LUNA_DF_PLOT2 = px.line(UST_LUNA_DF, x="Timestamp", y=["Terra Luna Price"],
                        title="Terra Luna Price")
LUNA_DF_PLOT2.update_layout(legend_title="Digital Asset", width=1300, height=450, title_x=0.5, title_y=.85,
                            plot_bgcolor='rgba(0,0,0,0)')
LUNA_DF_PLOT2.update_xaxes(showgrid=False, title="Date")
LUNA_DF_PLOT2.update_yaxes(showgrid=True, title="Daily Price($)")
st.plotly_chart(LUNA_DF_PLOT2)

#                           _________Insert Stablecoins risks: Title and body text__________
st.markdown("<h1 style='text-align: left; color: white; font-size: 120%'>""A. CBDC Risks: Mass surveillance </h1>",
            unsafe_allow_html=True)
st.write("<div style='text-align:justify'>""\n"
         "The S.W.O.T analysis has highlighted many threats with CBDCs. The risk of mass surveillance is a critical risk associated with the adoption of CBDCs. Based on the model and design, these "
         "government issued digital cash can have a massive implication on human rights. Government agencies will have the ability to monitor every move of every participant as all transactions are forever "
         "on the ledger. Individual's activity could potentially be targeted based on their credit history, politican ties, race or ethnicity. Transactions can very well be restricted or permitted by central bank authorities. "
         "Aside from control of funds, if applied CBDC issuers will have full access to digital identity of individuals. This also reigns massive implication on human rights. Participants will need confidence that their digital identity isn't misused. "
         "The best way to mitigate these concerns is to adopt CBDC solutions which place these risks at the forefront and eliminates them entirely. Central bank digital currencies will need to address a number of important risks and concerns in a short "
         "amount of time if authorities wish to include this technology in the fabric of traditional finance and banking.",
         unsafe_allow_html=True)

# Insert Stablecoins risks: Title and body text
st.markdown("<h1 style='text-align: left; color: white; font-size: 120%'>""C. Bottom line </h1>",
            unsafe_allow_html=True)
st.write("<div style='text-align:justify'>""\n"
         "Distributed Ledger technologies have given rise to blockchains. Many of these chains have grown enormously in the past four years sparking pockets of economic value. "
         "Nations worldwide have recognized the future opportunities with their own version of stablecoins; CBDCs (digital cash). With so much innovations ahead for programmable money, there are many risks and concerns. Market makers, national authorities and "
         "international regulatory bodies will have to work extremly hard for an equilibrium between innovation and ethical implementation framework. In the months and years to come, the evolution of blockchain will be an exciting dance to watch between regulators and all stakeholders! ",
         unsafe_allow_html=True)
"\n"
# insert figure button
SLReg_button = st.expander(label="Figure 5.0 - 5.1A : TerraUSD Volume & Terra Luna Volume")
SLReg_button.write("""
Figure 5.0: TerraUSD Volume

Figure 5.1A: Terra Luna Volume

Datasource: CoingeckoAPI

Technologies: PyCharm, CoingeckoApi, Python; plotly express, pandas, streamlit""")

st.info("REFERENCES")

# insert References button
SLReg_button = st.expander(label=" Expand for references")
SLReg_button.write("""

[bcg.com, Kay Burchardi, igor Mikhalev, Bihao Song, and Steven Alexander Kok (2020), "Get ready for the Future of Money"]
    (https://www.bcg.com/publications/2020/get-ready-for-the-future-of-money) 

[bis.org, Hyun Song Shin, Benoit Coeure (2021), "Bis Annual Economic Report"]
    (https://www.bis.org/publ/arpdf/ar2021e3.htm)

["big.org, Condruta Boar and Andreas Wehrli (2021), "Ready, Steady, go? --Results of the Third BIS Survey on Central Bank Digital Currency]
    (https://www.bis.org/publ/bppdf/bispap114.pdf)

[consensys.net, Matthieu Saint Olive (2020), "What is Retail Central Bank Digital Currency"]
    (https://consensys.net/blog/enterprise-blockchain/what-is-retail-central-bank-digital-currency/)

[globalfindex.worldbank.org, "The Unbanked"]
    (https://globalfindex.worldbank.org/sites/globalfindex/files/chapters/2017%20Findex%20full%20report_chapter2.pdf)

[FDIC.gov, Federal Deposite Insurance Corporation (2021), "How American Banks: Households Use of Banking and Financial Services"]
    (https://www.fdic.gov/analysis/household-survey/index.html)

[nytimes.com, David Yaffe-Bellany and Erin Griffith (2022), "How a Trash-Talking Crypto Founder Caused a $40 Billion Crash "]
    (https://www.nytimes.com/2022/05/18/technology/terra-luna-cryptocurrency-do-kwon.html)

[ecb.europa.eu, Mitsutoshi Adachi, Alexandra Born, Isabella Gschossmann and Anton Van Der Kraaij (2021), "The Expanding Functions and Uses of Stablecoins"]
    (https://www.ecb.europa.eu/pub/financial-stability/fsr/focus/2021/html/ecb.fsrbox202111_04~45293c08fc.en.html)

[ieeexplore.ieee.org, Clemens Jeger, Bruno Rodrigues, Eder Scheid, and Burkhard Stiller (2020), "Analysis of Stablecoins During the Global COVID-19 Pandemic"]
    (https://ieeexplore.ieee.org/abstract/document/9274450?figureId=fig1#fig1)

[libertystreeteconomics.newyorkfed.org, Rod Garratt, Michael Lee, Antoine Martin, and Joseph Torregrossa (2022), "The Future of payments Is Not Stablecoins"]
    (https://libertystreeteconomics.newyorkfed.org/2022/02/the-future-of-payments-is-not-stablecoins/)

[finra.org, Finra (2020), "3 Things to Know About Stablecoins"]
    (https://www.finra.org/investors/insights/3-things-stablecoins

[coindesk.com, Alexander Lipton (2020), "Stablecoins Are the Bridge From Central Banks to Consumer Payments."]
    (https://www.coindesk.com/markets/2020/05/30/stablecoins-are-the-bridge-from-central-banks-to-consumer-payments/)

[coindesk.com, Kay Burchardi and Igor Mikhalev (2020), "Central Bank Digital Currencies Need Decentralization"]
    (https://www.coindesk.com/policy/2020/05/23/central-bank-digital-currencies-need-decentralization/)

[101blockchains.com, Qwyneth Iredale (2021), "Advantages of Central Bank Digital Currencies (CBDCs)"]
    (https://101blockchains.com/advantages-of-central-bank-digital-currencies/)

[weforum.com, Sebastian Banescu, Ben Borodach, and Ashley Lannquist (2021), "4 Key Cybersecurity threats to new central bank digital currencies"]
    (https://www.weforum.org/agenda/2021/11/4-key-threats-central-bank-digital-currencies/#:~:text=Yet%20like%20any%20digital%20payment,be%20confident%20in%20its%20security).

[finextra.com, Jeremy Light (2022), "The Risks to Society of central Bank Digital Currencies"]
    (https://www.finextra.com/blogposting/21584/the-risks-to-society-of-central-bank-digital-currencies)

[bloomberg.com, Hannah Miller (2022), "Terra $45 Billion Face Plant Creates Crowd of Crypto Losers"]
    (https://www.bloomberg.com/news/articles/2022-05-14/terra-s-45-billion-face-plant-creates-a-crowd-of-crypto-losers)

[Coingecko API ]
    (https://www.coingecko.com/en/api/documentation)

[CBDCs Tracker]
    (https://cbdctracker.org/)
""")
st.write("---")
########################################################################################################################
##########################################################################################################################
########################################################################################################################


