import streamlit as st
from streamlit_option_menu import option_menu
import requests as r
import babel.numbers
from PIL import Image
from sklearn.impute import KNNImputer
from pycoingecko import CoinGeckoAPI
from Utilities.Navigation import render_sidebar
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
st.set_page_config(page_title=" Digital Assets | GFC & Regulatory Compliance Analysis", layout="wide")
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

render_sidebar("GFC & Regulatory Compliance Analysis")
# _____________________________________________________________

# insert title of Financial Crimes and Compliance Analysis
st.markdown(
    "<h1 style='text-align: center; color: white;'>""Global Financial Crimes & Regulatory Compliance in Banking ""</h1>",
    unsafe_allow_html=True)
# Name on document
st.markdown("<h1 style='text-align: center; color: white; font-size: 150%'>""Guy Gnakpa""</h1>", unsafe_allow_html=True)
# Date of on documents
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>"" February, 2023""</h1>",
            unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>" "</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>" "</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>" "</h1>", unsafe_allow_html=True)
# ____________________________________Introduction of Compliance ________________________________________________________
# insert summary title and body
st.header("Summary")
st.write("<div style='text-align:justify'> ""\n"
         "The global banking industry market has grown significantly over the past decades. As of Q3 2021, the industry had an estimated "
         "market capitalization of ~$8.36 trillion. The industry had an increase of 44.13% from its previous valuation in Q3 2020 (~$5.80 trillion), (Abby McCain, Zippia.com). "
         "The trend suggests the market will continue to show signs of positive growth over the coming years. The industry growth has led to a higher number of human capital "
         "to adequately satisfy the increasing number of clients. Digital transformation initiatives have been adopted to create efficiency within processes. "
         "Although the growth has positively effected earnings, the global banking institutions face many challenges. The most evolving and important challenge is regulatory compliance "
         """due to a large number of risk factors. According to Mckinsey, "since 2009, regulatory fees have dramatically increase relative to bank's earnings"(Piotr Kaminski, mckinsey.com). """
         "This suggests the level of risk factors are continuously creating evolving challenges for the compliance department in many of the global banks. "
         , unsafe_allow_html=True)

# insert expander for earnings vs fine and settlements.
EarningsVSFees = Image.open("Data_PNG_JPG_Files/Earnings_VS_Fees.png")
McKinseyButton = st.expander(label="Performance of 20 large US and EU Universal Banks vs. Fines Settlements")
McKinseyButton.image(EarningsVSFees)
# insert Purpose title and body
st.header("Purpose")
st.write("<div style='text-align:justify'> ""\n"
         "The objective of this document is to highlight the role of regulatory compliance and governance in banking, financial regulatory authorities, "
         "risk factors in banking, and relevant risk management systems. The sub division of regulatory compliance in banking, Global Financial Crimes unit, will be the main focus. "
         "Further, an analysis of suspicious activity report(SAR) will be included to showcase "
         "and quantify challenges many financial institutions continuously face. "
         , unsafe_allow_html=True)
st.write("")
st.write("---")
# insert first point title and body
st.subheader("Regulatory compliance and governance in banking")
st.write("<div style='text-align:justify'> ""\n"
         "The compliance department has a huge responsibility in the structure of a global banking. "
         "Although the compliance division consist of many functions, they all lead to a central goal; risk management. "
         "In the banking structure the compliance division is the second line of defence for managing numerious diverse risk factors. "
         "The division must ensure the bank operates according to domestic and internal regulations. In addition, the divison is tasked to "
         "create, govern, monitor and revise compliance program and internal bank policy. Any suspicious financial activity is monitored and reported to financial regulators "
         "by the compliance department on behalf of the bank. Below are some of the core functions of the compliance(GFC) division but not limited to: "
         , unsafe_allow_html=True)
# insert core functions of the compliance division
st.info("""
    - Anti-Corruption
        -
        - regulations and procedures in place to prevent corruption where the abuse of power or position is utilized for personal gain. Acitivities like embezzlement, bribery, use of secret informatin are all forms of unethical behavior that are subject to the Anti-corruption laws. The Anti-corruption procedures are meant to mitigate risks of fraud, promote transparency accountability and integrity wihtin banking.  
        - To prevent the risk of such activities the compliance division may implement policies, education, conduct internal and external audits.
        - Anti-corruption is governed by many authorities including; Department of Justice(DOJ), Securities and Exchange Commission(SEC), Financial Crime Enformance Network(FinCen), Federal Bureau of Investigation(FBI), Internal Revenue Services(IRS).
        - The Anti-corruption prevention is part of the American Anti-Corruption Act(AACA).
    - Anti-Money Laundering
        - 
        - regulations and procedures in place to prevent the efforts of concealing illicit funds as legitimate income. Regulators required transaction of $10,000 or more to be reported. Futher, it is required to conduct due diligence on customers through the process of Know Your Customer(KYC).
        - KYC enables for banks to better identity new clients, the nature of their activities, and clarification on the source of funds. KYC ensure customers are not part of a criminal organization, under economic sanctions by U.S regulators, nor politically affiliated.
        - Anti-money laundering and KYC procedures begin with the Bank Secrecy Act(1970), and are now part of The Anti-Money Laundering Act of 2020 in order to keep up with the increase of illicit activities. This law is enforeced by The Department of the Treasury, specifically the bureau of Financial Crimes Enforcement Network(FinCEN).  
    - Anti-Tax Evasion
        -
        - regulations and procedures in place to prevent, detect and monitor suspicious activities associated with tax evasion. The objective of these procedures is to prevent tax avoidance and promote integrity within the financial system.   
        - Banking institutions must comply with regulations set forth by Foreign Account Tax Compliance Act(FATCA), Common Reporting Standard(CRS), and the U.S. Internal Revenue Code. 
    - Anti-boycott
        -
        - regulations and procedures in place by U.S regulators prohibiting discrimination or the refusal of conducting business with countries or companies that are unsanctioned by the U.S government. Share information of unsanctioned boycotted countries and firms is also prohibited by the U.S.
        - Anti-Boycott Act of 2018 is part of the Export Control Reform Act of 2018 (ECRA). This law is enforced by the Bureau of Industry and Security(BIS).
    - Economic Sanctions - OFAC
        -
        - regulations and procedures in place to monitor and prevent economic transactions with individuals, entities or countries who are sanctions by U.S regulators. The policies in place help metigate risks associated with banking operations, national security and froeign policy.  
        - The Office of Foreign Assets Control(OFAC) division in the U.S. Treasury Department is responsible for enforcing this regulation. OFAC impose economic sanctions against specific countries, terrorists and crimical organizations.  
    - Political Contributions
        -
        - regulations and procedures in place to monitor and prevent corruption associated with financial donation in order to gain political influence.  
        - political contributions are subject to the Federal Election Campaign Act laws enforced by Federal Election Commission(FEC)
    """)
# insert second point: description for regulatory bodies
st.subheader("Financial regulatory authorities")
st.write("<div style='text-align:justify'> ""\n"
         "Global financial institutions are regulated by many U.S and international agencies based on the banking structure. "
         "Below are a list of U.S. agencies who are responsible for the prevention of fraud and maintaining fairness, integrity, and accountibility in banking. "
         "Use the expand buttons below to see specific regulatory bodies responsible to enforce, govern and monitor the banking and securities industry "
         , unsafe_allow_html=True)
st.write("")
# insert expander button for each type of regulators
Banking_Regulators = st.expander(label="Expand to see the relevant banking regulators ")
Banking_Regulators.info("""
    - Consumer Financial Protection Bureau (CFPB) - consumer compliance
    - Federal Reserve System ("Fed")
    - Federal Deposit Insurance Corporation (FDIC)
    - Office of the Comptroller of the Currency (OCC)
    - National Credit Union Administration (NCUA)
    - Farm Credit Administration (FCA)
    - Federal Financial Institutions Examination Council (FFIEC) - main umbrella group for US Federal banking authorities
    - Conference of State Bank Supervisors (CSBS) - main umbrella group representing US State and Territorial banking supervisors
    """)
Securities_Regulators = st.expander(label="Expand to see the relevant securities regulators")
Securities_Regulators.info("""
    - Securities & Exchange Commission (SEC)
    - Commodity Futures Trading Commission (CFTC)
    - Securities Investor Protection Corporation (SIPC)
    - Financial Industry Regulatory Authority (FINRA)
    - Municipal Securities Rulemaking Board (MSRB)
    - National Futures Association (NFA)
    """)
Other_Regulators = st.expander(label="Expand to see other relevant regulators")
Other_Regulators.info("""
    - Financial Stability Oversight Board (FSOC) - systemic risk
    - Federal Housing Finance Agency (FHFA) - government sponsored housing finance
    - Financial Crimes Enforcement Network (FinCEN) - anti-money laundering
    - National Association of Insurance Commissioners (NAIC) - insurance
    - Each US state and territory generally has its own banking, insurance, and securities authorities
    """)
st.write("---")
# insert risk factors in banking
st.subheader("Risk factors")
st.write("<div style='text-align:justify'> ""\n"
         "More than ever banks are facing many challenges that are placing more pressure on compliance division to better operate "
         "with integrity and adhere to applicable laws, regulations and internal policies. Aside from the compliance department's core functions of "
         "enforcing Anti-Money Laundering(AML), Anti-Corruption, Anti-Tax Evasion, Economic Sanctions, and Political Contribution regulatory requirements, many other "
         "risk factors must be mitigated. Below are many other risk factors a compliance division may be faced with."
         , unsafe_allow_html=True)
st.info("""
    - Market risk
    - Financial Risk
    - Operation risk
    - Reputation Risk
    - Compliance Cost
    - Regulatory change
    - Digital transformation risk
    - Hybrid work environment risk 
    - Legal and regulatory penalties
    """)
# insert relevant risk management systems for growing risk factors
st.subheader("Risk management systems")
st.info("""
    - Continue to implement adequate procedures to govern, monitor and report suspicious activity related to anti-money laundering, anti-tax evasion, anti-corruption, economic sanctions, and political contributions.   
    - Implement quality specialized training programs to better educate employees on relevant and evolving regulations.  
    - Continue to conduct internal audit, review and address compliance policies to identify inefficiencies that can lead to potencial risks.  
    - Implementing a more advance monitoring and reporting system to recognize and address risk factors associated with regulatory violation. 
    - Increase the use of data analysis to better understand trends associated with internal policy performance and financial activities. 
    - Increase reporting to senior management and the Board of Directors on compliance-related risks and the effectiveness of risk management measures. 
    - Improve relationships with regulatory agencies to stay informed on evolving laws and regulations. 
    """)
st.write("---")
# insert title and body of suspicious activity report
st.subheader("Suspicious Activity Report(SARs) Analysis")
st.info("""
    - The compliance division is the second line of defence against any illicit activities.
    - Within compliance exist a sub-division, Global Financial Crimes(GFC), responsible for governing and escalating any activity behaving against the internal compliance program.
    - The GFC program is a set of policies associated with the enforcement of Bank Secrecy Act, AML, Anti-Corruption, Anti-Tax Evasion, Economic Sanctions, and Political Contributions. 
    - Per regulations, the GFC sub-division must monitor, investigate and report any suspicious activity. The GFC employs a number of risk measures to adhere to the laws and regulations.   
    - One of the control methods to mitigate potential risk factors associated with regulations and internal policies is a standard of metrics reporting. 
    - The metrics reporting can aid all departments, including the business unit, and chairman committee to better understand existing threats to the bank. 
    - Below is an analysis of Suspicious Activity Report(SARs) filed by entities in the Depository and Securities/Futures industry. 
    - The visualizations highlight key metrics within the data provided by the Financial Crimes Enforcement Network(FinCEN)
    """)

st.info("""
    - SAR: Filings of Depository Institution Industry
        - 
        - From 2014 to 2021 there is a positive trend in the number of SAR filings. 
        - More recently from 2020 to 2021 the number of SAR has increased by 17.78%.
        - When observing filings by specific categories from 2020 -2021, the data suggests Mortgage Fraud is down 22.41% and Terririst Financing is down by 15.18%.
        - Amongst the top 25 types of suspicious activity filed from 2014 - 2021, "Suspicion Concerning the Source of Funds" has the higher quatity.
        - When observing the distribution of filings per state and territory, New York (903,948), and California (1,463,306) have the highest quantity of SAR filings.      

    """)

SAR_Tableau_Dashboard = """
    <div class='tableauPlaceholder' id='viz1771480213940' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fi&#47;FinancialCrimes_Dashboard&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='FinancialCrimes_Dashboard&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fi&#47;FinancialCrimes_Dashboard&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1771480213940');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1427px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>        
    """
components.html(SAR_Tableau_Dashboard, width=5000, height=900, scrolling=True)


SAR_ByStateFiling_Dash = """
        <div class='tableauPlaceholder' id='viz1675874378527' style='position: relative'>
        <noscript>
        <a href='#'>
        <img alt='Dashboard 2 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fi&#47;FinancialCrimes_Dashboard&#47;Dashboard2&#47;1_rss.png' style='border: none' />
        </a>
        </noscript><object class='tableauViz'  style='display:none;'>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
        <param name='embed_code_version' value='3' /> <param name='site_root' value='' />
        <param name='name' value='FinancialCrimes_Dashboard&#47;Dashboard2' />
        <param name='tabs' value='no' />
        <param name='toolbar' value='yes' />
        <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fi&#47;FinancialCrimes_Dashboard&#47;Dashboard2&#47;1.png' />
        <param name='animate_transition' value='yes' />
        <param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' />
        <param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' />
        <param name='language' value='en-US' />
        <param name='filter' value='publish=yes' />
        </object>
        </div>                
        <script type='text/javascript'>                    
        var divElement = document.getElementById('viz1675874378527');                    
        var vizElement = divElement.getElementsByTagName('object')[0];                    
            if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';}
             else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';}
              else { vizElement.style.width='100%';vizElement.style.height='727px';}                     
              var scriptElement = document.createElement('script');                    
              scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
              vizElement.parentNode.insertBefore(scriptElement, vizElement);
        </script>
        """
components.html(SAR_ByStateFiling_Dash, width=5000, height=900, scrolling=False)



# # insert Suspicious activity report analysis
# tableau_Col0, tableau_Col1 = st.columns(2)
# with tableau_Col0:
#     # st.info("description for the below visualization")
#     SAR_Tableau_Dashboard = """
#     <div class='tableauPlaceholder' id='viz1771480213940' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fi&#47;FinancialCrimes_Dashboard&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='FinancialCrimes_Dashboard&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fi&#47;FinancialCrimes_Dashboard&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1771480213940');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1427px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
#     """
#     components.html(SAR_Tableau_Dashboard, width=900, height=500)
# # insert second tableau visual
# with tableau_Col1:
#     # st.info("description for the below visualization")
#     SAR_ByStateFiling_Dash = """
#         <div class='tableauPlaceholder' id='viz1675874378527' style='position: relative'>
#         <noscript>
#         <a href='#'>
#         <img alt='Dashboard 2 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fi&#47;FinancialCrimes_Dashboard&#47;Dashboard2&#47;1_rss.png' style='border: none' />
#         </a>
#         </noscript><object class='tableauViz'  style='display:none;'>
#         <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
#         <param name='embed_code_version' value='3' /> <param name='site_root' value='' />
#         <param name='name' value='FinancialCrimes_Dashboard&#47;Dashboard2' />
#         <param name='tabs' value='no' />
#         <param name='toolbar' value='yes' />
#         <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fi&#47;FinancialCrimes_Dashboard&#47;Dashboard2&#47;1.png' />
#         <param name='animate_transition' value='yes' />
#         <param name='display_static_image' value='yes' />
#         <param name='display_spinner' value='yes' />
#         <param name='display_overlay' value='yes' />
#         <param name='display_count' value='yes' />
#         <param name='language' value='en-US' />
#         <param name='filter' value='publish=yes' />
#         </object>
#         </div>
#         <script type='text/javascript'>
#         var divElement = document.getElementById('viz1675874378527');
#         var vizElement = divElement.getElementsByTagName('object')[0];
#             if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';}
#              else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';}
#               else { vizElement.style.width='100%';vizElement.style.height='727px';}
#               var scriptElement = document.createElement('script');
#               scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
#               vizElement.parentNode.insertBefore(scriptElement, vizElement);
#         </script>
#         """
#     components.html(SAR_ByStateFiling_Dash, width=2000, height=500, scrolling=False)

# insert figure references button
TableauDash_button = st.expander(label="Figure 2.0 references : Financial Crime Enforcement Network ")
TableauDash_button.write("""
    Datasource: FinCEN

    Technologies: Excel, Tableau, PyCharm, Python; plotly express, pandas, streamlit""")

# insert title and body of suspicious activity report
st.info("""
    - SAR: Filings of Securities and Futures Industry
        - 
        - Within the Securities and Futures industry the top type of suspicious activity filing is "ACH". 
        - The overall filing value for ACH is 60,942, making up 8.92% of the overall distribution.
        - "Identity theft" is the second biggest type of suspicious activity within the securities and futures industry.
        - The overall filings for Identity theft is 54,968, making up 8.04% of the total distribution.
        - "Wire" fraud is responsible for 52,968 suspicious activity filings in the securities and futures industry. It is 7.72% of the total distribution.       
    """)
SecuritiesFutures_Type_DF = pd.read_csv("Data_CSV_Files/SAR_SecuritiesFutures_Type.csv")
# SecuritiesFutures_Type_DF=SecuritiesFutures_Type_DF.drop(Securities_Futures_DF.index[-1])
# insert figure references button
SecuritiesFuturess_button = st.expander(label="Expand to see data table of Securities and Futures ")
SecuritiesFuturess_button.dataframe(SecuritiesFutures_Type_DF)

SecuritiesFutures_Type_DF2 = SecuritiesFutures_Type_DF
SecuritiesFutures_Type_DF2.sort_values(by="Rank", ascending=True, inplace=True)
SecuritiesFutures_Type_fig = px.bar(SecuritiesFutures_Type_DF2,
                                    x="Suspicious Activity Type",
                                    y="Filings (Overall)",
                                    title="Number of Filings by Type of Suspicious Activity from Securities/Futures Industry:January 1, 2014 - December 31, 2021")
SecuritiesFutures_Type_fig.update_layout(legend_title="Features", width=1550, height=1050, plot_bgcolor='rgba(0,0,0,0)')
SecuritiesFutures_Type_fig.update_xaxes(showgrid=False, title="Types of Securities/Futures")
SecuritiesFutures_Type_fig.update_yaxes(showgrid=False, title="Overall Filings")
st.plotly_chart(SecuritiesFutures_Type_fig)

# insert figure references button
Ploty_button = st.expander(label="Figure 3.0 references : Financial Crime Enforcement Network ")
Ploty_button.write("""
    Datasource: FinCEN

    Technologies: Excel, Tableau, PyCharm, Python; plotly express, pandas, streamlit""")

st.write("---")

REFERENCES = st.expander(label="References")
REFERENCES.write("""
    Data Source: Financial Crimes Enforcement Network (FinCEN)

    https://www.zippia.com/advice/financial-services-industry-statistics/#:~:text=Global%20Financial%20Services%20Industry%20Statistics&text=This%20data%20was%20published%20at,by%20the%20end%20of%202021.

    https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/a-best-practice-model-for-bank-compliance

    https://www.investopedia.com/terms/a/anti-boycott-regulations.asp#:~:text=Anti%2Dboycott%20regulations%20have%20provisions,about%20boycotted%20countries%20and%20firms.

    https://www.bis.doc.gov/index.php/enforcement/oac#:~:text=The%20antiboycott%20provisions%20of%20the%20EAR%20require%20U.S.%20persons%20to,their%20receipt%20of%20boycott%20requests.

    https://www.fincen.gov/history-anti-money-laundering-laws

    https://www.fec.gov/help-candidates-and-committees/candidate-taking-receipts/types-contributions/

    https://en.wikipedia.org/wiki/List_of_financial_regulatory_authorities_by_country

    https://www.bankingsupervision.europa.eu/press/publications/newsletter/2020/html/ssm.nl200212_1.en.html#:~:text=Compliance%20functions%20are%20a%20key,laws%2C%20regulations%20and%20internal%20policies.

    """)
########################################################################################################################
########################################################################################################################
########################################################################################################################
