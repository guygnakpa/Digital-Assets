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
import webbrowser
import openpyxl as xls
import datetime
from Utilities.Navigation import render_sidebar, hide_streamlit_nav
# _____________________________________________________________
st.set_page_config(page_title=" Digital Assets | Institutional Digital Assets Operating Model Library", layout="wide")
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

render_sidebar("Institutional Digital Assets Operating Model Library")
# _____________________________________________________________

# insert title of Financial Crimes and Compliance Analysis
st.markdown(
    "<h1 style='text-align: center; color: white;'>""Institutional Digital Assets Operating Model Library""</h1>",
    unsafe_allow_html=True)
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
# ____________________________________Introduction of Operating Model Library________________________________________________________

st.subheader("Executive Summary")
st.write("<div style='text-align:justify'> ""\n"
         "The Institutional Digital Asset Operating Model Library provides a set of high-level reference architectures and "
         "asset lifecycles designed to demonstrate how regulated financial institutions can integrate digital assets while "
         "preserving governance, control, and regulatory integrity. Rather than focusing on implementation detail, the library reflects "
         "the decision-making, risk assessment, and operating model considerations that guide institutional adoption."
         , unsafe_allow_html=True)

st.markdown("The models intentionally distinguish between: ")
st.info("""
* Client-owned assets
* Bank liabilities
* Regulated securities
""")
st.markdown("This separation prevents category errors and ensures each digital asset use case is aligned with its correct compliant, accounting and risk treatment.")

st.subheader("Scope of the Library")
st.markdown("The library includes three foundational institutional models: ")
st.info("""
1. Institutional Digital Asset Custody
2. Tokenized Deposits 
2. Tokenized Money Market Funds (MMF) - Tokenized RWA
""")
#3. Tokenized Money Market Fund (MMF) – Tokenized RWA
st.markdown("Together, these models cover the core digital asset primitives relevant to banks, asset managers, custodians, and financial market infrastructures.")
# ____________________________________Operating Architecture & Control Model Matrix _____________________________________
st.write("---")
Data_Matrix = {
    "Dimension": [
        "Legal Nature",
        "Ownership",
        "System of Record",
        "Balance Sheet Impact",
        "On-Chain Role",
        "Primary Risk"
    ],
    "Custody": [
        "Client assets",
        "Client",
        "Custody ledger",
        "None",
        "Settlement",
        "Asset loss"
    ],
    "Tokenized Deposits": [
        "Bank liabilities",
        "Bank obligation",
        "Core banking ledger",
        "Direct",
        "Representation + settlement",
        "Liquidity & solvency"
    ]
    ,"Tokenized MMF": [
        "Fund securities",
        "Investor",
        "Transfer agent / fund accounting",
        "Fund-level only",
        "Representation + settlement",
        "Valuation & eligibility"
    ]
}

DF_Matrix = pd.DataFrame(Data_Matrix)
st.subheader("Model Matrix")
st.dataframe(DF_Matrix, use_container_width=True)
##########################################################################################################################################
##########################################################################################################################################
# ____________________________________Institutional Digital Assets Custody – High-Level Operating Architecture & Control Model________________________________________________________
st.write("________________")
st.subheader("Institutional Digital Asset Custody")
st.markdown("Purpose:")
st.markdown("Institutional digital asset custody provide safekeeping and controlled movement of client-owned assets through authorization, secure key governance, and continuous reconciliation without ownership to the custodian.")
st.markdown("Key Characteristics:")
st.info("""
* Assets remain client-owned at all times
* Internal custody ledger is the system of record
* Layered controls govern deposits, internal transfers, and withdrawals
* Key governance (MPC / HSM / TEE) enforces separation of duties
* Continuous reconciliation between on-chain and ledger
""")
st.markdown("Institutional Value")
st.info("""
* Addresses the highest-risk area of digital assets: safekeeping
* Designed for auditability, incident response, and regulatory oversight
* Foundational capability upon which all other models rely
""")

st.write("________________")
#---Import Image of the Digital Asset Custody Model----#
Digital_Asset_Custody_Model = Image.open("Data_PNG_JPG_Files/Digital Assets Custody Model.jpg")
st.image(Digital_Asset_Custody_Model, use_container_width=True)  # output_format="auto"
#---insert Lifecycle Points----
st.subheader("Asset Lifecycle")


Asset_Custody1 = st.expander(label="Client Deposit Initiation")
Asset_Custody1.markdown("* Client initiates a deposit by transferring digital assets to a custodian-controlled deposit address.")
Asset_Custody1.markdown("* Deposit addresses are: ")
Asset_Custody1.info("""
* Uniquely assigned
* Wallet-tier appropriate
* Segregated per client or omnibus model
""")
Asset_Custody1.markdown("*Note: Custodian does not initiate deposits*")
                            #----------#
Asset_Custody2 = st.expander(label="Blockchain Detection & Confirmation")
Asset_Custody2.info("""
* Incoming transaction detected via blockchain monitoring
* Block confirmations observed
* Deposit marked as pending until finality thresholds are met
""")
Asset_Custody2.markdown("*Note: No internal crediting before settlement finality*")
                        # ----------#
Asset_Custody3 = st.expander(label="Deposit Validation & Attribution")
Asset_Custody3.markdown("* Deposit validated against:")
Asset_Custody3.info("""
* Known client deposit address
* Supported asset types
""")
Asset_Custody3.markdown("* Asset attributed to correct client account")
Asset_Custody3.markdown("* Exceptions flagged for review ")
Asset_Custody3.markdown("*Note: Attribution is recorded internally*")
                        # ----------#
Asset_Custody4 = st.expander(label="Internal Ledger Crediting")
Asset_Custody4.markdown("* Internal custody ledger updated:")
Asset_Custody4.info("""
* Client balance credited
* Timestamped audit trail created
""")
Asset_Custody4.markdown("* Ledger acts as system of record for client balances")
Asset_Custody4.markdown("* Exceptions flagged for review ")
Asset_Custody4.markdown("*Note: On-chain balance will not equal client balance until ledger update*")
                        # ----------#
Asset_Custody5 = st.expander(label="Secure Asset Safekeeping")
Asset_Custody5.markdown("* Assets managed across wallet tiers:")
Asset_Custody5.info("""
* Hot (operational liquidity)
* Warm (controlled access)
* Cold (deep storage)
""")
Asset_Custody5.markdown("* Ledger acts as system of record for client balances")
Asset_Custody5.info("""
* Policy limits 
* Approval workflows
* Key governance controls
""")
Asset_Custody5.markdown("*Note: Keys remain isolated and governed*")
                        # ----------#
Asset_Custody6 = st.expander(label="Ongoing Monitoring & Reconciliation")
Asset_Custody6.markdown("* Continuous reconciliation between:")
Asset_Custody6.info("""
* On-chain balances
* Internal custody ledger
""")
Asset_Custody6.markdown("* Thresholds and alerts configured")
Asset_Custody6.markdown("* Discrepancies escalated to operations & risk")
Asset_Custody6.markdown("*Note: Reconciliation is continuous, not periodic*")
                        # ----------#
Asset_Custody7 = st.expander(label="client Withdrawal Request")
Asset_Custody7.markdown("* Client submits withdrawal request via:")
Asset_Custody7.info("""
* Custody UI
* Authorized APIs
""")
Asset_Custody7.markdown("* Request authenticated and validated")
Asset_Custody7.markdown("* Withdrawal parameters verified")
Asset_Custody7.markdown("*Note: No direct client access to keys or wallets*")
                        # ----------#
Asset_Custody8 = st.expander(label="Policy, Risk & Compliance Checks")
Asset_Custody8.markdown("* Withdrawal evaluated against:")
Asset_Custody8.info("""
* Velocity limits
* Whitelists
* Transaction thresholds
* Sanctions / AML rules
""")
Asset_Custody8.markdown("* Requests failing checks are rejected or escalated")
Asset_Custody8.markdown("*Note: Controls precede execution*")
                        # ----------#
Asset_Custody9 = st.expander(label="Transaction Authorization & signing")
Asset_Custody9.markdown("* Approved withdrawal routed to Key Governance Layer")
Asset_Custody9.info("""
* Multi-party signing enforced
* Role-based approvals applied
* Signing occurs within secure execution environments (MPC / HSM / TEE)
""")
                        # ----------#
Asset_Custody10 = st.expander(label="On-Chain Execution")
Asset_Custody10.info("""
* Authorized transaction broadcast to blockchain
* Transaction enters mempool (temporary holding space for unconfirmed transactions)
* Settlement finality awaited
""")
                        # ----------#
Asset_Custody11 = st.expander(label="Ledger Update & Client Notification")
Asset_Custody11.markdown("* Internal ledger updated:")
Asset_Custody11.info("""
* Client balance debited
* Transaction reference recorded
""")
Asset_Custody11.markdown("* Client notified of transaction status")
Asset_Custody11.markdown("*Note: Ledger remains authoritative*")
                        # ----------#
Asset_Custody12 = st.expander(label="Post-Settlement Reconciliation")
Asset_Custody12.info("""
* On-chain settlement confirmed
* Ledger and wallet balances reconciled
* Exceptions investigated and resolved
""")
                        # ----------#
Asset_Custody13 = st.expander(label="Audit, Controls & Regulatory Oversight")
Asset_Custody13.markdown("* All lifecycle events logged:")
Asset_Custody13.info("""
* Deposits
* Internal transfers
* Withdrawals
""")
Asset_Custody13.markdown("* Evidence retained for:")
Asset_Custody13.info("""
* Audits
* Regulatory reporting
* Incident response
""")
st.markdown("Failure & Exception Handling")
st.info("""
* Unattributed deposits can be flagged for manual review
* Failed or stuck transactions can be escalated to operations
* Ledger-to-chain mismatches trigger reconciliation workflows
* No automated retries without authorization
""")
st.write("________________")
Sources_Custody = st.expander(label="Model Sources / References")
Sources_Custody.info("""
* [OCC Interpretive Letter 1170 – Bank crypto custody authority (PDF)](https://www.occ.gov/topics/charters-and-licensing/interpretations-and-actions/2020/int1170.pdf)
* [OCC Interpretive Letter 1184 – Bank custody & execution services. OCC Clarifies Crypto Custody Authority (PDF)](https://www.occ.gov/news-issuances/news-releases/2025/nr-occ-2025-42.html)
* [FDIC guidance affirming permissible crypto activities. FDIC Clarifies Crypto Activities (PDF)](https://www.fdic.gov/news/financial-institution-letters/2025/fdic-clarifies-process-banks-engage-crypto-related)
""")

st.write("________________")
##########################################################################################################################################
##########################################################################################################################################
# ____________________________________Tokenized Deposits - High-Level Operating Architecture Model________________________________________________________

st.subheader("Tokenized Deposits")
st.markdown("Bank Liabilities")
st.markdown("Purpose:")
st.markdown("Enable regulated banks to represent deposits on-chain while preserving balance-sheet control, liquidity management, and regulatory compliance.")
st.markdown("Key Characteristics:")
st.info("""
* Tokens represent bank liabilities, not bearer assets
* Core banking ledger remains the system of record
* Issuance and redemption enforce 1:1 backing
* On-chain settlement is programmable but not authoritative
* Liquidity, capital, and compliance controls remain unchanged
""")
st.markdown("Institutional Value")
st.info("""
* Bridges traditional banking and on-chain settlement
* Enables faster, programmable payments without disintermediation
* Preserves financial stability while improving operational efficiency
""")

st.write("________________")
#---Import Image of Tokenized Deposits Model----#
Tokenized_Deposits_Model = Image.open("Data_PNG_JPG_Files/Tokenized Deposits Model.jpg")
st.image(Tokenized_Deposits_Model, use_container_width=True)  # output_format="auto"

st.subheader("Asset Lifecycle")
Tokenized_Deposits0 = st.expander(label="Client Initiates Instruction -- initiation of payment submission or transfer request occurs via: ")

Tokenized_Deposits0.info("""
* Digital banking channels
* Treasury portal
* Authorized API
""")
Tokenized_Deposits1 = st.expander(label="Authentication & Access Validation -- unauthorized requests are rejected before orchestration")
#st.markdown("Authentication & Access Validation -- unauthorized requests are rejected before orchestration")
Tokenized_Deposits1.info("""
* Request passes through Payments / API Gateway
* Authentication & authorization enforced
* Limits, entitlements, and request validity checked
""")

Tokenized_Deposits2 = st.expander(label="Transaction Orchestration")
#st.markdown("Transaction Orchestration")
Tokenized_Deposits2.info("""
* Normalizes payment instructions
* Classifies request (issue, transfer, redeem)
* Routes to policy and issuance logic
""")
Tokenized_Deposits3 = st.expander(label="Policy, Compliance & Risk Evaluation -- any failure halts the lifecycle here")
#st.markdown("Policy, Compliance & Risk Evaluation -- any failure halts the lifecycle here")
Tokenized_Deposits3.info("""
* AML / sanctions screening
* Counterparty eligibility checks
* Velocity and exposure limits enforced
* Jurisdictional rules applied
""")
Tokenized_Deposits4 = st.expander(label="Deposit Token Issuance / Redemption Decision")
#st.markdown("Deposit Token Issuance / Redemption Decision")
Tokenized_Deposits4.markdown("* The engine determines: ")
Tokenized_Deposits4.info("""
* Whether new tokens are minted
* Whether tokens are transferred
* Whether tokens are redeemed (burned)
* Jurisdictional rules applied
""")
Tokenized_Deposits4.markdown("* 1:1 backing enforcement validated")
Tokenized_Deposits4.markdown("* Token lifecycle rules applied")

Tokenized_Deposits5 = st.expander(label="Authorization & signing")
#st.markdown("Authorization & signing")
Tokenized_Deposits5.info("""
* Approved actions sent to Key Governance & Authorization Layer
* Role-based approvals enforced
* Multi-Party-computation(MPC) / Hardware Security Module(HSM) / Trusted Execution Environment(TEE) signing occurs
* Signing authority is cryptographically controlled
""")

Tokenized_Deposits6 = st.expander(label="On-Chain Execution")
#st.markdown("On-Chain Execution")
Tokenized_Deposits6.info("""
* Authorized transaction executed via Tokenized Deposits Smart Contract
* Transfers restricted to permissioned addresses
* Programmable settlement logic enforced
* Atomic settlement achieved on supported networks
""")

Tokenized_Deposits7 = st.expander(label="Ledger & Balance Sheet Update -- the authoritative source")
#st.markdown("Ledger & Balance Sheet Update -- the authoritative source")
Tokenized_Deposits7.markdown("* TCore Banking Ledger updated:")
Tokenized_Deposits7.info("""
* Customer deposit balances
* Accounting entries
* General ledger integration
* Jurisdictional rules applied
""")
Tokenized_Deposits7.markdown("* On-chain balances reconciled to banking records")
Tokenized_Deposits7.markdown("* Ledger remains system of record for deposit liabilities")

Tokenized_Deposits8 = st.expander(label="Treasury & Liquidity Management")
#st.markdown("Treasury & Liquidity Management")
Tokenized_Deposits8.markdown("* Treasury systems updated:")
Tokenized_Deposits8.info("""
* Reserve backing confirmed
* Liquidity buffers adjusted
* Intraday liquidity tracked
""")
Tokenized_Deposits8.markdown("* Balance-sheet exposure monitored")


Tokenized_Deposits9 = st.expander(label="Chain Observability & Reconciliation")
#st.markdown("Chain Observability & Reconciliation")
Tokenized_Deposits9.markdown("* Blockchain data and oracles provide:")
Tokenized_Deposits9.info("""
* Block confirmations
* Chain state updates
* Reconciliation inputs
""")
Tokenized_Deposits9.markdown("* Exceptions flagged for investigation")

Tokenized_Deposits10 = st.expander(label="Audit, Controls & Regulatory Oversight")
#st.markdown("Audit, Controls & Regulatory Oversight")
Tokenized_Deposits10.markdown("* Read-only oversight enabled")
Tokenized_Deposits10.markdown("* Evidence captured for:")
Tokenized_Deposits10.info("""
* Regulatory reporting
* Attestations
* Internal audits
""")
Tokenized_Deposits10.markdown("* Full lifecycle traceability preserved")


st.markdown("Failure & Exception Handling")
st.markdown("* Any policy failure halts execution before signing")
st.markdown("* Failed on-chain execution triggers:")
st.info("""
* Reconciliation review
* Exception workflows
* Internal audits
""")
st.markdown("* Ledger discrepancies escalate to:")
st.info("""
* Operations
* Risk management
* Internal audits
""")
st.markdown("* No automated retries without authorization")
st.write("________________")
Sources_Deposits = st.expander(label="Model Sources / References")
Sources_Deposits.info("""
* [OCC interpretive letter cluster on digital asset activities (custody/stablecoin/DLT) (PDF)](https://www.occ.treas.gov/news-issuances/news-releases/2025/nr-occ-2025-16.html)
* [Academic paper on tokenization and institutional adoption. Tokenization & Institutional Adoption Paper (PDF)](https://www.frontiersin.org/journals/blockchain/articles/10.3389/fbloc.2026.1747208/full)
""")

st.write("________________")
##########################################################################################################################################
##########################################################################################################################################
# ____________________________________Tokenized Money Market Fund - High-Level Operating Architecture Model________________________________________________________
st.subheader("Tokenized Money Market Fund (MMF)")
st.markdown("Tokenized Regulated Securities (RWA)")
st.markdown("Purpose:")
st.markdown("Tokenized MMF shares represent (cash-equivalent) regulated fund ownership interests that are issued, transferred, and redeemed on-chain while valuation, ownership records, and"
            "fund governance remain off-chain under established fund controls.")

st.markdown("Key Characteristics:")
st.info("""
* Tokens represent securities ownership, not cash
* Transfer Agent is the system of record for ownership
* Fund accounting is the system of record for balances and NAV
* NAV calculation and fund governance remain off-chain
* Transfers restricted to eligible, whitelisted investors
""")
st.markdown("Institutional Value")
st.info("""
* Enables on-chain distribution of regulated investment products
* Aligns with existing fund administration and custody models
* Supports tokenized cash-management and treasury use cases
""")

st.write("________________")
#---Import Image of the Digital Asset Custody Model----#
Tokenized_MMF_Model = Image.open("Data_PNG_JPG_Files/Tokenized MMF Model.jpg")
st.image(Tokenized_MMF_Model, use_container_width=True)  # output_format="auto"

st.subheader("Asset Lifecycle")

Tokenized_MMF_Model0 = st.expander(label="Institutional or corporate investor submits a subscription request via: ")

Tokenized_MMF_Model0.info("""
* fund distribution platform
* Treasury portals
* Authorized APIs
""")
 # ----------------#
Tokenized_MMF_Model1 = st.expander(label="Authentication & Access Controls -- Fund / Transfer API Gateway enforces:")
Tokenized_MMF_Model1.info("""
* Authentication & authorization
* Investor entitlement
* Subscription parameters
""")
Tokenized_MMF_Model1.markdown("*Note: invalid requests are rejected before orchestration*")
#----------------#
Tokenized_MMF_Model2 = st.expander(label="Subscription & Redemption Orchestration")
Tokenized_MMF_Model2.markdown("Orchestration service:")
Tokenized_MMF_Model2.info("""
* Normalizes subscription instructions
* Determines transaction type (subscribe / redeem / transfer)
* Routes request to eligibility, NAV, and TA logic
""")
# ----------------#
Tokenized_MMF_Model3 = st.expander(label="Investor Eligibility, Compliance & Risk Validation")
Tokenized_MMF_Model3.info("""
* AML / KYC / sanctions screening
* Eligible investor class verification
* Jurisdictional restrictions enforced
* Concentration & exposure checks applied
""")
Tokenized_MMF_Model3.markdown("*Note: Any failure halts the lifecycle immediately")
# ----------------#
Tokenized_MMF_Model4 = st.expander(label="NAV Determination & Pricing")
Tokenized_MMF_Model4.markdown("* Fund Administration & NAV Engine: ")
Tokenized_MMF_Model4.info("""
* Calculates applicable NAV (daily or intraday)
* Enforces cut-off times
* Validates pricing inputs
* Computes share quantities
""")
 # ----------------#
Tokenized_MMF_Model5 = st.expander(label="Transfer Agent Validation:")
Tokenized_MMF_Model5.info("""
* Confirms subscription / redemption eligibility
* Updates official shareholder register
* Validates ownership records
* Confirms share issuance or cancellation
""")
Tokenized_MMF_Model5.markdown("System of Record for Share Ownership")
# ----------------#

Tokenized_MMF_Model6 = st.expander(label="Authorization & Token Issuance / Burn")
Tokenized_MMF_Model6.markdown("* Approved issuance or redemption routed to:")
Tokenized_MMF_Model6.info("""* Key governance & Authorization Layer""")
Tokenized_MMF_Model6.markdown("* Role-based approvals enforced")
Tokenized_MMF_Model6.markdown("* Token mint / burn authority cryptographically controlled")
Tokenized_MMF_Model6.markdown("* No bypass of governance controls")
Tokenized_MMF_Model6.markdown("*Notes: Authorization precedes execution*")
# ----------------#

Tokenized_MMF_Model7 = st.expander(label="On-Chain Token Execution")
Tokenized_MMF_Model7.markdown("* Tokenized MMF Smart Contract:")
Tokenized_MMF_Model7.info("""
* Mints or burns MMF tokens
* Enforces permissioned transfers
* Restricts transfers to whitelisted addresses
* Executes programmable settlement logic
""")
Tokenized_MMF_Model7.markdown("*Note: On-chain execution is not the same as ownership authority*")
# ----------------#

Tokenized_MMF_Model8 = st.expander(label="Fund Accounting & Record keeping Update")
Tokenized_MMF_Model8.markdown("* Fund Accounting System updates:")
Tokenized_MMF_Model8.info("""
* Share balances
* Accrued income
* NAV reconciliation
""")
Tokenized_MMF_Model8.markdown("* Reconciles token supply to issued shares")
Tokenized_MMF_Model8.markdown("*Note: System of Record for Fund Accounting & Share Balances*")
# ----------------#

Tokenized_MMF_Model9 = st.expander(label="Portfolio & Custody Alignment")
#st.markdown("Chain Observability & Reconciliation")
Tokenized_MMF_Model9.markdown("* Underlying MMF assets::")
Tokenized_MMF_Model9.info("""
* Held by regulated fund custodian
* Valuation inputs fed to NAV engine
""")
Tokenized_MMF_Model9.markdown("* Portfolio positions adjusted as required")
Tokenized_MMF_Model9.markdown("*Note: Assets remain segregated and custodied off-line*")
# ----------------#
Tokenized_MMF_Model10 = st.expander(label="Secondary Transfers (If Permitted)")
Tokenized_MMF_Model10.markdown("Transfers allowed only between:")
Tokenized_MMF_Model10.info(""""Eligible, whitelisted investors""")
Tokenized_MMF_Model10.markdown("* Compliance enforced at smart-contract level")
Tokenized_MMF_Model10.markdown("* Transfer Agent & Accounting systems updated accordingly")
Tokenized_MMF_Model10.markdown("*Note: Secondary liquidity does not bypass governance*")
# ----------------#
Tokenized_MMF_Model11 = st.expander(label="Redemption & Cash Settlement")
Tokenized_MMF_Model11.markdown("* Investor initiates redemption request")
Tokenized_MMF_Model11.markdown("* Tokens burned")
Tokenized_MMF_Model11.markdown("* Cash proceeds settled via traditional payment rails")
Tokenized_MMF_Model11.markdown("* Fund liquidity adjusted")
Tokenized_MMF_Model11.markdown("*Note: SCash settlement remains off-chain*")
# ----------------#
Tokenized_MMF_Model12 = st.expander(label="Chain Observability & Reconciliation")
Tokenized_MMF_Model12.markdown("* Blockchain data & oracles provide:")
Tokenized_MMF_Model12.info("""
* Block confirmation
* token balances
* Reconciliation inputs
""")
Tokenized_MMF_Model12.markdown("* Exceptions flagged for investigation")
# ----------------#
Tokenized_MMF_Model12 = st.expander(label="Audit, Controls & Regulatory Oversight")
Tokenized_MMF_Model12.markdown("* Read-only oversight enabled across:")
Tokenized_MMF_Model12.info("""
* NAV calculations
* Share registry changes
* Token issuance / burns
""")
Tokenized_MMF_Model12.markdown("* Evidence retained for:")
Tokenized_MMF_Model12.info("""
* Regulatory reporting
* Attestations
* Audits
""")
# ----------------#
st.markdown("Failure & Exception Handling include:")
st.info("""
* Eligibility or compliance failure halts execution pre-issuance
* NAV discrepancies trigger pricing review
* Token-to-registry mismatches escalate to fund operations
* No automated retries without governance approval
""")

st.write("________________")
Sources_MMF = st.expander(label="Model Sources / References")
Sources_MMF.info("""
* [Franklin Templeton OnChain MMF product. Franklin Templeton OnChain Money Fund (PDF)](https://www.franklintempleton.com/investments/options/money-market-funds/products/29386/SINGLCLASS/franklin-on-chain-u-s-government-money-fund/FOBXX)
* [BIS research on tokenized money market funds. Rise of Tokenised Money Market Funds (BIS) (PDF)](https://www.bis.org/publ/bisbull115.pdf?)
""")

st.write("________________")