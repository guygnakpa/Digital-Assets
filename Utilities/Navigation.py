import streamlit as st
from streamlit_option_menu import option_menu
import streamlit as st
from streamlit_option_menu import option_menu
import requests as r
import babel.numbers
from PIL import Image
from sklearn.impute import KNNImputer
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
#########################################################
# The logic below will hide the streamlit auto page menu as it is redundant
def hide_streamlit_nav():
    st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {display: none;}
    </style>
    """, unsafe_allow_html=True)
#########################################################
# Label -> page file path (relative to app root)
PAGES = {
    "Home": "Home.py",
    #"Resume": "pages/1_Resume.py",
    "Institutional Digital Assets Operating Model Library": "pages/2_Institutional_Digital_Assets_Operating_Model_Library.py",
    "Stablecoins Analysis": "pages/3_Stablecoins_Analysis.py",
    "Geography of Cryptocurrency Report": "pages/4_Geography_of_Cryptocurrency_Report.py",
    "DeFi Liquidity Aggregator": "pages/5_Defi_Liquidity_Aggregator.py",
    "Capital Markets Analysis": "pages/6_Capital_Markets_Analysis.py",
    "GFC & Regulatory Compliance Analysis": "pages/7_GFC_Regulatory_Compliance_Analysis.py",
    "System Architecture Analysis": "pages/8_System_Architecture_Analysis.py"
    #"SQL Business Analysis": "pages/8_SQL_Business_Analysis.py",
    #"Financial & Marketing Analysis": "pages/9_Financial_and_Marketing_Analysis.py",
    #"Business Ethics Analysis": "pages/10_Business_Ethics_Analysis.py",
}

ICONS = {
    "Home": "house",
    "Resume": "briefcase-fill",
    "GFC & Regulatory Compliance Analysis": "briefcase-fill",
    "Capital Markets Analysis": "bank",
    "Stablecoins Analysis": "currency-bitcoin",
    "Geography of Cryptocurrency Report": "pin-map-fill",
    "DeFi Liquidity Aggregator": "droplet-half",
    "SQL Business Analysis": "bar-chart-fill",
    "System Architecture Analysis": "cpu-fill",
    "Financial & Marketing Analysis": "activity",
    "Business Ethics Analysis": "credit-card-2-back",
    "Institutional Digital Assets Operating Model Library": "diagram-3-fill"
}

def render_sidebar(current_label: str) -> None:
    """Renders sidebar option_menu and navigates to selected page."""
    labels = list(PAGES.keys())
    icons = [ICONS.get(lbl, "circle") for lbl in labels]

    with st.sidebar:
        selected = option_menu(
            "Menu",
            labels,
            icons=icons,
            default_index=labels.index(current_label) if current_label in labels else 0,
            orientation="vertical",
        )

    # Navigate only if user picked a different page
    if selected != current_label:
        st.switch_page(PAGES[selected])

