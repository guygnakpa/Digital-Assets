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
st.set_page_config(page_title=" Digital Assets | Resume", layout="wide")
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

render_sidebar("Resume")

#st.title("Resume")

# _____________________________________________________________
st.markdown("<h1 style='text-align: center; color: white;'>""Guy L. Gnakpa""</h1>", unsafe_allow_html=True)

Space_col1, Space_col2, Space_col3 = st.columns([1,2,1])
with Space_col1:
    st.markdown("<h1 style='text-align: center; color: white;'>"" ""</h1>", unsafe_allow_html=True)
    image0 = Image.open("Data_PNG_JPG_Files/IMG_2675.JPG")
    st.image(image0, width=250)

with Space_col2:
    st.markdown(
        """
        <div style="text-align: center;">
            <a href="https://www.linkedin.com/in/guy-gnakpa/"
               target="_blank"
               style="font-size:20px; text-decoration:none; color:#0077B5; font-weight:600;">
               🔗 Connect on LinkedIn
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="text-align: center;">
            <a href="https://github.com/guygnakpa"
               target="_blank"
               style="font-size:20px; text-decoration:none; color:#0077B5; font-weight:600;">
               🔗 Connect on Github
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
with Space_col3:
    " "

    ###--------------------------------------------------------------###
    # Custom function for printing text
    def txt(a, b):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(a)
        with col2:
            st.markdown(b)


    def txt2(a, b):
        col1, col2 = st.columns([1, 4])
        with col1:
            st.markdown(f'`{a}`')
        with col2:
            st.markdown(b)


    def txt3(a, b):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown(a)
        with col2:
            st.markdown(b)


    def txt4(a, b, c):
        col1, col2, col3 = st.columns([1.5, 2, 2])
        with col1:
            st.markdown(f'`{a}`')
        with col2:
            st.markdown(b)
        with col3:
            st.markdown(c)

# # ###--------------------------------------------------------------##
st.markdown("## Profile", unsafe_allow_html=True)
st.info("""A goal-oriented and collaborative professional with years of experience in financial services.
    Hand on experience with non-financial risk data analysis, digital assets analysis, fund management and administration for alternative assets in investment banking. Holds a
    graduate-level education focused on management sciences and quantitative methods. Skilled at utilizing analytical tools to
    better understand data for valuable insights with a focus on Data Analysis, ML Models, Data Visualization and Strategic
    Reporting. Ability to adapt quickly, identify inefficiencies and communicate effectively with stakeholders. Passionate about
    financial instruments, technology and the implication of decentralized ledger technology for decades to come. Seeking a challenging
    opportunity with a renown and innovative culture where my experience, skills and education can add value for all stakeholders.""")

###--------------------------------------------------------------##
### Skills ###
st.markdown("## Skills", unsafe_allow_html=True)
st.info("""
    - Machine Learning Models (Regression, Time-series), Statistical Analysis (Exploratory, Predictive, Reporting)
    - Python (Pandas, NumPy, Seaborn, Matplotlib, Scikit-learn, Streamlit), Data Visualization/BI (Tableau, PowerBI) Data Wrangling (MySQL, DBeaver, Alteryx)
    - Microsoft Office (Word, Excel, PowerPoint, Visio, Project), Coaching and Mentoring – AICPA (06/21)
    - Blockchain (POW, POS, L1, L2), Defi Protocols (Dex, Asset Management, Lend/Borrow, Yield), Tokenized RWA (MMF, FoF, Deposits)
    """)

###--------------------------------------------------------------##
###Education###
st.markdown("""## Education """, unsafe_allow_html=True)
# Master of Science, Management Sciences and Quantitative Methods
txt("**Master of Science**, *Management Sciences and Quantitative Methods*", "****Jan 2021-Apr 2022****")
st.markdown("""
    - Southern New Hampshire University, Manchester, NH
    - NECHE Accredited
    - GPA :  3.8/4.0
    """)
#
# Bachelor of Arts, Economics
txt("**Bachelor of Arts**, *Economics*", "****Sep 2017-Dec 2019****")
st.markdown("""
    - Ramapo College of New Jersey, Mahwah, NJ
    - AACSB Accredited
    - GPA :  3.0/4.0
    """)
###--------------------------------------------------------------##
###EXPERIENCE###
st.markdown("""## Experience
     """)
txt("###### ****Morgan Stanley, New York, NY****", "****Apr 2023-Present****")
st.text("Director (AVP), NFR Data Analytics – Visualization & Reporting Solutions (Full-Time)")
st.markdown("""
    - Acted as a core contributor to a firm-wide Metrics Enhancement Program, focused on data quality, metric effectiveness, control oversight, and strategic reporting modernization.
    - Managed end-to-end design, governance, and delivery of enterprise risk metrics (KRI/KPI) used by Governance Committees, Business Heads, and Board-level stakeholders across global regions.
    - Owned authoritative data sources, schemas, and taxonomy alignment, ensuring consistency across enterprise reporting and downstream consumption by risk, audit, and control functions.
    - Partnered with regional teams across AMER, EMEA, and APAC to align data sourcing, controls, and reporting standards across multiple business units and operating environments.
    - Designed and optimized SQL-based data pipelines to query, transform, validate, and reconcile large-scale datasets, materially reducing manual processing and accelerating reporting timelines.
    - Engineered and maintain automation workflows (Python, Alteryx) to support scalable, repeatable metric production and operational resilience.
    - Implemented threshold-based escalation frameworks (RAG methodology) to monitor AML, operational risk, and control breaches, including EDD/PEP reviews, control framework issues, and internal audit findings.
    - Served as steward of a centralized data aggregation and metrics repository, supporting recurring ad-hoc regulatory, audit, and governance requests.
    """)
txt("Manager, Global financial Crimes (GFC) – Metrics and Reporting Professional (Full-Time)", "****Apr 2023-March 2024****")

txt("###### ****BNY Mellon, Woodland Park, NJ****", "****Jul 2020-Jan 2021****")
st.text("Analyst, Fund Of Funds Custody (Full-Time)")
st.markdown("""
    - Supported daily custodial operations for alternative asset portfolios, ensuring accurate asset servicing, recordkeeping, and reconciliation.  
    - Utilized operational dashboards and custody management systems to report on fund allocations, holdings, and performance.  
    - Executed and monitored subscriptions, redemptions, transfers, proxies, and trade instructions, ensuring accuracy and timeliness across settlement workflows.  
    - Performed daily cash and demand deposit reconciliations, coordinating closely with Treasury and Operations teams.
    - Applied AML/KYC procedures in fund distribution and client servicing, supporting compliance and audit readiness.
    - Authenticated trade instructions and resolved operational inquiries to protect client asset integrity.
    - Assisted in adapting operational tooling for custody fee calculation and reporting, improving accuracy and efficiency.
    """)

txt("###### ****Premium Merchant Funding, New York, NY****", "****Oct 2018-Sept 2019****")
st.text("Analyst, Account Management (Full-Time)")
st.markdown("""
    - Supported a funding team responsible for capital allocation to SMEs, coordinating investment workflows and stakeholder communications. 
    - Analyzed financial statements, credit histories, and contractual documentation to assess risk, compliance, and eligibility.
    - Verified business account histories and compliance with financial and operational prerequisites. 
    - Presented financial products and services to new and existing clients, contributing to increased capital deployment.
    - Trained and mentored interns on financial products, operational processes, and compliance expectations.  
    - Delivered investment and operational recommendations that improved approval quality and client service demand.
    """)

txt(" ###### ****Lobster Life Systems, Lodi, NJ****", "****Aug 2016-Aug 2017****")
st.text("Assistant Project Manager, Internship (Full-Time)")
st.markdown("""
    - Conducted administrative duties for a manufacturing and wholesale business.
    - Implemented management strategies for on demand resources.
    - Onboarded new team members to maintain and supply the demand for services.
    - Adapted administrative aides, hands on manufacturing production and inventory management.
    - Assisted in the strategy of expansion and client acquisition in the northeast region of the country.
    - Facilitated communication between internal and external project stakeholders to keep all parties well-informed.
    """)

# ###--------------------------------------------------------------###
###PROJECTS###
st.markdown("## Projects", unsafe_allow_html=True)
txt4("Institutional Digital Assets Model Library",
     "A set of high-level reference architectures and asset lifecycle designed to demonstrate how regulated financial institutions can integrate digital assets while preserving governance, control & regulatory integrity.",
     "Public Data, Data manipulation and Visual Engineering all with Python libraries.")

txt4("Stablecoins Analysis",
     "An analytical research document describing stablecoins and their functions. The opportunities and risks "
     "are discused. Trend analysis and Machine learning modeling are utilised to convey existing relationship "
     "between Bitcoin and Stablecoins.",
     "Machine Learning with Python, Visual engineering with Python, Visualization Dashboard with Tableau.")

txt4("Geography of Cryptocurrency Report",
     "An analysis on received and deposited funds based on-chain data. The analysis explores "
     "existing trends within geographic locations. Fundamental questions are explored to produce insightful feedback. ",
     "On-Chain Data, Data manipulation and Visual engineering with Python Libraries.")

txt4('DeFi Liquidity Aggregator',
     "A DeFi liquidity aggregator interactive dashboard. Representation of decentralized application (dapp) as an "
     "insightful tool for fundamental understanding of liquidity allocation. Aggregates total value locked, market "
     "capitalization, daily volume, and other metrics for tracking DeFi activity.",
     "API Requests, Data manipulation and Visual Engineering all with Python libraries.")

txt4("Capital Markets Analysis",
     "An analysis on capital markets focused on equity and bond securities. The primary and secondary "
     "markets are discussed. Economic factors which effect these markets are explored and illustrated through "
     "data visualisations. Time-series index analysis were conducted with statistical methodologies. The market "
     "capitalization of selected Bond / Tokenized ETFs securities are calculated and visually displayed.",
     "API Requests, Data manipulation and visual engineering all completed with excel and python libraries.")

txt4("Global Financial Crimes & Regulatory Compliance Analysis",
     "An analysis on global financial crimes and regulatory compliance in banking."
     "The purpose of a compliance division in a bank and its core responsibilities are discussed. "
     "Financial regulators responsible for governing, monitoring and enforcing respective laws are highlighted  "
     "Risk factors associated with compliance in banking are mentioned as well as risk management systems ."
     "Data analysis of suspicious activity filings is conducted and reported through metric visualization  .",
     "FinCEN Data, Data manipulation and visual engineering all completed with excel, tableau and python libraries.")

txt4("System Architecture Analysis",
     "A system architecture case study focused on system development for data management,"
     " service scheduling and daily reporting for a small business. A full analysis of developing an internal "
     "Electronic Data Interchange has been conducted and tested via reports.",
     "Microsoft Project, Microsoft Visio, Microsoft Excel, Microsoft Word, Discord, and Python were all utilized")

# txt4('SQL Business Analysis',
#      "An SQL query case study for a small business operation. Conducted 4 queries, asking 4 fundamental questions. Turning results of the questions and queries into an insightful feedback accompanied with recommendations for increasing revenue.",
#      "SQL for Data Queries. Python and Streamlit for front-end execution.")
# txt4("Financial & Marketing Analysis",
#      "A case study higlighting the utilization of financial documents and reporting to evaluate how to strategically implement a product in a new market sector.",
#      "Completed with Google Suite")
# txt4("Business Ethics Analysis",
#      "Business Ethics case study evaluating ethical approaches to marketing, and corporate social responsibility.",
#      "Completed with Google Suite")
# Insert Resume for Download
with open("Resumes/GuyGnakpa_CV_1.0.pdf", "rb") as file:
    Button = st.download_button(
        label="Download Resume",
        data=file,
        file_name="Resumes/GuyGnakpa_CV_1.0.pdf",
        mime="image/png"
    )

st.write("")

st.info("""
    DISCLAIMER: The production of these analyses are solely for educational purposes. The data used to explain certain events
    is subject to change, and the analyses are not intended to be used as investment tools.
    If these analyses are used for any other purposes than intended, the author is not liable.
    """)
########################################################################################################################
########################################################################################################################
########################################################################################################################