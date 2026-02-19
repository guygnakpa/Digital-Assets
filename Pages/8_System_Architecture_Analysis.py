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
st.set_page_config(page_title=" Digital Assets | System Architecture Analysis", layout="wide")
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

render_sidebar("System Architecture Analysis")
# _____________________________________________________________

# insert date and participants to of the document
st.markdown(
"<h1 style='text-align: center; color: white;'>""System Architecture and Design Analysis: Hudson Kayak Adventures""</h1>",
    unsafe_allow_html=True)
st.markdown(
    "<h1 style='text-align: center; color: white; font-size: 150%'>"" Guy Gnakpa ""</h1>",
    unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white; font-size: 150%'>""Advanced Info Technology""</h1>",
            unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white; font-size: 150%'>""May 26, 2022""</h1>",
            unsafe_allow_html=True)
st.markdown("<h1 style= color: white; font-size: 95%;'>""</h1>", unsafe_allow_html=True)
# insert background title and body text
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>Background</h1>", unsafe_allow_html=True)
st.write("<div style='text-align:justify'>""\n"
         "Hudson Kayak Adventures, a kayak rental that rents out, instructs individuals on how to use it and guided tours about "
         "the facility and along the river, was built by the Lanes family. Linda, who is a web designer, oversees the technical aspect "
         "of the business such as making sure that the website is up to date or creating a database to log all the information about customers "
         "that are renting a kayak. And Steve makes sure that the business is running smoothly. Reservations are entered in a loose-leaf binder, "
         "with separate tabs for each business activity. Linda uses an inexpensive accounting package to keep HKA's financial records. For quick "
         "reference, she displays kayak availability on a wall-mounted board with color-coded magnets. HKA’s inventory includes 16 rental kayaks of "
         "several types, lengths, and capacities, eight car-top carriers, and a large assortment of accessories and safety equipment. And they are "
         "thinking of adding more informational videos to make it accessible to the customers. Although the current business is working fine for now, "
         "they want to create an automated reservation process and record useful data to make good predictions or change business plan.",
         unsafe_allow_html=True)

# insert problem statement title and body text
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>Problem Statement</h1>",
            unsafe_allow_html=True)
st.write("<div style='text-align:justify'>""\n"
         "Currently, HKA does not have a centralized repository for storing, organizing, accessing, or disseminating information. "
         "Whether it is client information, process information, company policy and procedure, or helpful reminders, the Lanes have "
         "a unique system for storing and accessing the various types of information which is printing out a list that wall-mounted "
         "on a board. Due to the various ways in which information is currently being stored and referenced throughout the office, "
         "it can take employees longer to locate the information that they need to do their job than it does to complete a task. "
         "They are some occasionally conflict where the Lanes must be at two places at one. Linda, who manages the database, has "
         "some trouble keeping up with the daily update of information. Additionally, there is not a universal method for integrating "
         "new clients or for managing cases from an administrative perspective, and, despite recent efforts to improve these mechanisms, "
         "the Lanes must rely on those old-fashioned ways to get work done. They want a system that gives daily reports, shows trends in "
         "the market and kayak management tools.", unsafe_allow_html=True)

# insert Audience title and body text
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>Audience</h1>", unsafe_allow_html=True)
st.write("<div style='text-align:justify'>""\n"
         "This proposal's target audience includes the company's owners, employees, and customers. An owner has full access to the "
         "detailed history of every data in this system. It compiles reservation data, kayak type data, and client data into a single "
         "data set that is sorted by reservation date. Telephone inquiries and table reservations are handled by employees. Customers "
         "enter their personal information to make a reservation and access the system's services. Both the administration and the "
         "users can see if the table is available. One of the owners, Linda, updates the data or makes improvements to the system. ",
         unsafe_allow_html=True)
# _________________________insert project plan text and corresponding png____________________________#
# insert Project Plan title and body text
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>Project Plan</h1>",
            unsafe_allow_html=True)
st.write("<div style='text-align:justify'>""\n"
         "This plan shows the project timeline. The tasks are listed and the end date of each of them.",
         unsafe_allow_html=True)
"\n"
# ________phase1___________#
image1 = Image.open("Data_PNG_JPG_Files/systemdesign1.png")
st.image(image1, use_column_width="always")
st.write("""***Figure 1: phase 1*** """)
# ________phase2___________#
image2 = Image.open("Data_PNG_JPG_Files/systemdesign2.png")
st.image(image2, use_column_width="always")
st.write("""***Figure 2: phase 2*** """)
# ________phase 3___________#
image3 = Image.open("Data_PNG_JPG_Files/systemdesign3.png")
st.image(image3, use_column_width="always")
st.write("""***Figure 3: phase 3***""")
# ________phase 4___________#
image4 = Image.open("Data_PNG_JPG_Files/systemdesign4.png")
st.image(image4, use_column_width="always")
st.write("""***Figure 4: phase 4***""")
"\n"
# _________________________insert Requirements Modelling ____________________________#
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>Requirements Modeling</h1>",
            unsafe_allow_html=True)
# ________Outputs___________#
st.write("**Outputs:**")
st.info("""
-	Employees get daily reservations 
-	Owners get profit or losses for the business annually
-	Customers get email notifications for upcoming appointment with HKA
-	Owners get a quarterly report that identify changes in ordering pattern and trends
-	Customers get the list of kayaks on hand and time when they are available for booking
-	Owners have a daily activity report with a listing of all service transactions for the day
 """)
# ________Intputs___________#
st.write("**Inputs:**")
st.info("""
-	Customers perform a payment
-	Customers can book online appointments
-	Employees must be able to change customer appointments
-	Employees must enter customers’ booking when making phone call appointment
-	Employees must be able to update information about kayak availabilities and videos
 """)
# ________Process___________#
st.write("**Process:**")
st.info("""
-	System must perform a daily back up
-	Update the financial details into the accounting software
-	System must calculate employee salaries, bonuses and taxes related to IRS
-	System must update available slot based on employee availabilities and kayaks
-	System must calculate discount to customers that have been using HKA services multiple times
 """)
# ________Performance___________#
st.write("**Performance:**")
st.info("""
-	Website response time must not exceed four seconds
-	The website must support up to 20 users simultaneously
-	Kayak and employee must be ready to welcome customers within 10 minutes of their appointment
-	Cancel appointment by customer must be available to other customers within 10 seconds of the cancellation
 """)
# ________Controls___________#
st.write("**Controls:**")
st.info("""
-	All transactions must be audit trailed
-	Website must have a strong logon security
-	System must have a secure electronic payment 
-	The employee or customer can have ability to modify appointments
-	System must be able to back-up file every week for security purposes
-	Appointment cannot be made online unless first payment has been made
 """)
# _________________________Insert Data Flow body text and Diagram  ____________________________#
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>Data Flow Diagram</h1>",
            unsafe_allow_html=True)
st.write("<div style='text-align:justify'>""\n"
         "Hudson Kayak Adventure's data diagram can be seen below in figure 5. The figure illustrates the inflows and outflows of "
         "the electronic data interchange (EDI). There are five entities highlighted in the illustration. The Electronic Data Interchange "
         "is the main operating system which is the circle-shaped object located at the center of the diagram. The rest of the entities are "
         "represented in rectangle-shaped objects interacting with the EDI.Depicted in distinct colors, the system is composed of five outputs "
         "seen in the green color. There are 3 inputs, which are represented in the blues arrows. ",
         unsafe_allow_html=True)
"\n"
# ________DataFlowDiagram___________#
image5 = Image.open("Data_PNG_JPG_Files/DataFlowDiagram1.png")
st.image(image5, use_column_width="always")  # output_format="auto"
st.write("""***Figure 5: Data Flow Diagram***""")
"\n"
# _________________________Insert Data Dictionary body text and Diagrams  ____________________________#
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>Data Dictionary</h1>",
            unsafe_allow_html=True)
st.write("<div style='text-align:justify'>""\n"
         "The data dictionary of the internal system process of Hudson Kayak Adventure can be seen in figure 6 below. The data dictionary "
         "specifically focuses on the entity and process of the EDI in relation to the rest of the external entities. The entity table is "
         "subdivided into four attributes: entity name, description, inputs, and outputs. Each respective entity from the flow diagram is "
         "included in the data dictionary table. The description and function of each entity are also illustrated in the table before. "
         "Lastly, the data flow of each entity in respect to their relation can be seen in the table below. The process table in figure "
         "6.1 illustrates the process of the system as well as their description and order number. The relation between each entity and "
         "its function can be clearly identified in the process table.", unsafe_allow_html=True)
"\n"
# ________DataDictionary Diagrams(entities)___________#
image6 = Image.open("Data_PNG_JPG_Files/DataDictionaryDiagram1.png")
st.image(image6, use_column_width="always")  # output_format="auto"
st.write("""***Figure 6: Data Dictionary, Entities***""")
# ________(Process)___________#
image7 = Image.open("Data_PNG_JPG_Files/DataDictionaryDiagram2.png")  # output_format="auto"
st.image(image7, use_column_width="always")
st.write("""***Figure 6.1: Data Dictionary, Process***""")
# ________(Database)___________#
image8 = Image.open("Data_PNG_JPG_Files/DataDictionaryDiagram3.png")
st.image(image8, use_column_width="always")  # output_format="auto"
image8_1 = Image.open("Data_PNG_JPG_Files/DataDictionaryDiagram4.png")
st.image(image8_1, use_column_width="always")  # output_format="auto"
st.write("""***Figure 6.2: Data Dictionary, Tables for Database***""")
"\n"
# _________________________Insert Use Case body text and Diagrams  ____________________________#
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>Use Case Diagram</h1>",
            unsafe_allow_html=True)
st.write("<div style='text-align:justify'>""\n"
         "Below in figure 7, the use case diagram shows the relationship between customers, staff(employee), and administration. "
         "All personnel entities are represented in the green stick figure objects while their function is represented in the respective arrows. "
         "The function of employees and admin can overlap while the function of customers does not. The function and process of the system is "
         "represented in the circular objects and located at the center of the respective arrows.",
         unsafe_allow_html=True)
"\n"
# ________(insert use case diagram)___________#
image9 = Image.open("Data_PNG_JPG_Files/UseCaseDiagram.png")
st.image(image9, use_column_width="always")  # output_format="auto"
st.write("""***Figure 7: Use Case Diagram***""")
# _________________________Insert Specifications body text and Diagrams  ____________________________#
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>Specifications</h1>",
            unsafe_allow_html=True)
# ________insert body text ___________#
st.write("<div style='text-align:justify'>""\n"
         "\n"
         "***Management Summary***: Hudson Kayak Adventures is going to benefit from a completely new website where customers can make "
         "reservations to rent kayaks. The project cost will not be significant as Linda is a web designer and will be helping with "
         "the construction of the new website. With Linda and the two developers, the timeline for this project should take three months."
         "\n"
         "\n"
         "***System Components***: The user interface will be colorful, user-friendly, and contain photos of what kind of services we provide. "
         "We will use Microsoft Azure to buy licenses for Microsoft Teams and Outlook so that the employees and the owners can communicate freely. "
         "Also, create an Azure database that Linda will update. Files will be stored on the local computer that only an authorized person will have access to. "
         "That will be ideal for now because the company is small. The website will perform a weekly backup of all data. Linda will perform backup for files stored "
         "on the computer at the workplace. We will get a license for QuickBooks so that the company has an audit trail for tax and payroll purposes. "
         "\n"
         "\n"
         "***System Environment***: New hardware will be needed as we will have a desktop for employees that will take orders and modify them. "
         "Security will not be an issue as we will have a different log-in of each employee and act accordingly if something goes wrong. "
         "All money transactions records will be available in QuickBooks where the appropriate person will access it. "
         "\n"
         "\n"
         "***Implementation Requirements***: As the company grows, we will have to design a training document for new hires to use as a guide. "
         "We will move all the existing data over to the new database. Linda will give training to the employees on how to use the website "
         "and complete the daily tasks that they are going to achieve. "
         "\n"
         "\n"
         """***Time and Cost Estimates***: The first month will be dedicated to the building of the website and the database. This will """
         "most likely be hard to achieve but feasible. Into the second month, we will move all require data and train employees on how "
         "to use the website. The third month will most likely be an observation month where developers will fix bugs and implement new "
         "important features. Since the company is small and has a low budget, continuous delivery will be costly as it can take many months "
         "to get a product to market. Our website will be hosted on Azure to limit the headache of a crash or hack from an outside party.",
         unsafe_allow_html=True)
"\n"
# ________specification diagram___________#
image10 = Image.open("Data_PNG_JPG_Files/SpecificationDiagram.png")
st.image(image10, use_column_width="always")
st.write("""***Figure 8: Specifications***""")
# _________________________Insert Data Design Diagrams  ____________________________#
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>Data Design</h1>",
            unsafe_allow_html=True)
image11 = Image.open("Data_PNG_JPG_Files/DataDesign1.png")
st.image(image11, use_column_width="always")
image12 = Image.open("Data_PNG_JPG_Files/DataDesign2.png")
st.image(image12, use_column_width="always")
image13 = Image.open("Data_PNG_JPG_Files/DataDesign3.png")
st.image(image13, use_column_width="always")
st.write("""***Figure 9: 3NF Chart***""")
# _________________________Insert Description and Entity Relationship Diagram  ____________________________#
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>Entity Relationship Diagram</h1>",
            unsafe_allow_html=True)
# ________description___________#
st.write("<div style='text-align:justify'>""\n"
         "In figure 10 below, there is an entity relationship diagram. The diagram includes 9 entities that are connected to other "
         "respective entities based on their function and relationship. The primary key and foreign key for each entity has been illustrated. "
         "The connecting arrows help illustrate the flow of data within the system.", unsafe_allow_html=True)
"\n"
# ________ERD Diagram___________#
image14 = Image.open("Data_PNG_JPG_Files/ERD.png")
st.image(image14, use_column_width="always")
st.write("""***Figure 10: Entity Relationship Diagram***""")
# _________________________Insert Description and User Interface Diagram  ____________________________#
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>User Interface Diagram</h1>",
            unsafe_allow_html=True)
# ________Description___________#
st.write("<div style='text-align:justify'>""\n"
         "The user interface diagram of kayaks for online applications is shown in Figure 11, which comprises sign-in, profile, "
         "booking, payment history, notification, account settings, and log out. The main sections of the Kayaks web application "
         "include reservations, kayaks, instructors, and customer service.", unsafe_allow_html=True)
st.info("""
-	Kayaks depict the size and type of individuals.
-	Customers are guided and kayak lessons are given by instructors.
-	Customer service provides HKA email and phone details to customers.
-	The availability of a day and time to reserve the available slots is shown in the reservation.
 """)
# ________UID Diagram___________#
image15 = Image.open("Data_PNG_JPG_Files/UserInterfaceDiagram.png")
st.image(image15, use_column_width="always")
st.write("""***Figure 11: User Interface Diagram***""")
# _________________________Insert Body text for System Architecture ____________________________#
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>System Architecture</h1>",
            unsafe_allow_html=True)
# ________Body Text___________#
st.write("<div style='text-align:justify'>""\n"
         "A study of day-to-day business functions, talking to users at all levels, and focusing on operational feasibility issues "
         "is the key answer to how to describe the culture of the organization. The Lanes love outdoor activities and rely on mouth-to-mouth "
         "advertisements for years. They are doing good in terms of making money and customers happy, but they just have an issue with the "
         "technical part of the business which we will provide for them. As the database and software were designed, it was made sure that "
         "there is room for scalability in case the company expands in the upcoming years. No data will be able to be lost and the records "
         "will be kept for future implementation. The integration will not be challenging as Linda has enough technical knowledge to ensure "
         "that all employees are getting their questions answered to make the transition smoother. Training will also be provided. Every "
         "employee will have an ID number and their passwords for desktop login and website. That way, we will track every employee if "
         "something goes missing. The employee will be told to never share their info with other employees.",
         unsafe_allow_html=True)
# _________________________Insert Body text for Project Monitoring and Control Plan____________________________#
st.markdown(
    "<h1 style='text-align: center; color: white; font-size: 120%'>Project Monitoring and Control Plan</h1>",
    unsafe_allow_html=True)
# ________Body Text___________#
st.write("<div style='text-align:justify'>""\n"
         "The changes made to the project towards the end of the semester played in our favor. Originally, we were given a short period of time "
         "to deliver the project proposal by the semester and we were racing against the clock to meet it. Between correcting our mistakes from "
         "the past deliveries and planning to work on the next, the workload was a little big and there was no time to entirely grasp the fundamentals "
         "of the lessons taught. With the change of schedule, we were allowed to make mistakes and correct those mistakes before moving onto the next chapter. "
         "The quality of the proposal looked so much better as we were dedicating a large amount of our time to this project as we will use those skills in our future jobs. "
         "The risk of failure was significantly reduced to a minimum as the team were preparing the best version of HKA proposal to present at the end of the semester. "
         "The risk of success was significantly up by those changes and the team felt really good about it.",
         unsafe_allow_html=True)
# _________________________Insert Body text and Diagram for System Mockup: Related Tables, Data Types, Relationships____________________________#
st.markdown(
    "<h1 style='text-align: center; color: white; font-size: 120%'>System Mockup: Related Tables, Data Types, Relationships</h1>",
    unsafe_allow_html=True)
# ________Body Text___________#
st.write("<div style='text-align:justify'>""\n"
         "\n"
         "\n"
         "In ***figures 12 – 13***, Access was utilized to create a prototype for the new information system. As illustrated, the prototype "
         "matches the logical design models as well as the supporting details in the data dictionary. Access does a great showcasing "
         "the relationship between the different entities. In figure 15, the Employee entity has two foreign keys, Title_ID and Address_ID. "
         "Similarly, the Address entity has two foreign keys, City_ID and Stat_ID. The Customer entity has a foreign key as Address_ID while "
         "the Reserve entity has Customer_ID and Inventory_ID. Lastly, the Payment entity has Reservation_ID as its foreign key. "
         "\n"
         "\n"
         "***Figure 13*** displays the related tables and data types. Each table represents an entity with its respective primary key and "
         "foreign key. Each table also includes some sample data and functionality. In the tables, the entities are represented in "
         "the red highlight while the primary keys are represented in yellow. For a logical flow of the entities and data, please "
         "follow the relationship diagram (figure 12) rather than figure 13.", unsafe_allow_html=True)
"\n"
# ________System Mockup Relationship Diagram___________#
image16 = Image.open("Data_PNG_JPG_Files/SystemMockupRelationships.png")
st.image(image16, use_column_width="always")
st.write("""***Figure 12: System Mockup Relationships***""")
# ________System Mockup Table and Data___________#
image16 = Image.open("Data_PNG_JPG_Files/SystemMockupRelationships2.png")
st.image(image16, use_column_width="always")
image17 = Image.open("Data_PNG_JPG_Files/SystemMockupRelationships3.png")
st.image(image17, use_column_width="always")
st.write("""***Figure 13: System Mockup Related Tables & Data Type***""")
# _________________________Insert Body text and Diagram for System Mockup: Six Queries Utilizing Relating Tables ____________________________#
st.markdown(
    "<h1 style='text-align: center; color: white; font-size: 120%'>System Mockup: Six Queries Utilizing Relating Tables</h1>",
    unsafe_allow_html=True)
# ________Body Text___________#
st.write("<div style='text-align:justify'>""\n"
         "We have made 6 queries from our database. The above image shows the different queries that we have conducted. "
         "The first query is related to the list of employees that were employed before 2018. The second one is the query of all employees "
         "that the last name is “Walker”. As of right now, we only have one result to show for. The third one is the list of inventories "
         "that can fit more than 2 people. As of right now, the query shows that we only have 4 on hands. The fourth image shows the "
         "query of all customers that last name is “Smith”. The reservation query is sorted by descending according to the Reservation_ID. "
         "The last query is related to all the payments that amount is greater than $300.", unsafe_allow_html=True)
"\n"
# ________System Mockup Queries___________#
image18 = Image.open("Data_PNG_JPG_Files/SystemMockupQueries1.png")
st.image(image18, use_column_width="always")
image19 = Image.open("Data_PNG_JPG_Files/SystemMockupQueries2.png")
st.image(image19, use_column_width="always")
st.write("""***Figure 14: System Mockup Six Queries***""")
# _________________________Insert Body text and Diagram for System Mockup: Four Forms ____________________________#
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>System Mockup: Four Forms</h1>",
            unsafe_allow_html=True)
# ________Body text___________#
st.write("<div style='text-align:justify'>""\n"
         "From our database design, we have made four forms. The customer will be able to enter their information when creating a "
         "profile as the figure below shows it. A manager will be able to create an account for an employee and create a reservation "
         "for a customer. The design was made for either customer and employee to have an easy and simple UI to make the daily activities easier.",
         unsafe_allow_html=True)
"\n"
# ________Four Form Diagram___________#
image20 = Image.open("Data_PNG_JPG_Files/SystemMockup4Form1.png")
st.image(image20, use_column_width="always")
image21 = Image.open("Data_PNG_JPG_Files/SystemMockup4Form2.png")
st.image(image21, use_column_width="always")
st.write("""***Figure 15: System Mockup Four Forms***""")
# _________________________Insert Body text and Diagram for System Mockup: Four Reports ____________________________#
st.markdown("<h1 style='text-align: center; color: white; font-size: 120%'>System Mockup: Four Reports</h1>",
            unsafe_allow_html=True)
# ________Body text___________#
st.write("<div style='text-align:justify'>""\n"
         "Figure 16 shows the reports for the following: customer employee, reservation and payment. As displayed the customer report "
         "represents a small portion of Hudson Kayak Adventure’s clientele. The customers are stored in the internal database. "
         "The information for each customer is specific and associated with their respective Customer_ID. The employee report "
         "represents the staff who work for Hudson Kayak Adventure. Some of the employees' responsibilities are to service the "
         "customers by making reservations, updating reservations and cancelling reservations. Like the customer report, the "
         "employee’s information is stored in the internal database. The information for each employee is specific and associated "
         "with their respective Emloyee_ID. Reservation report shows the internal database of the reservations initiated by the "
         "employee that is correlated to the respective customer. Each reservation is associated to the Customer_ID and Reservation_ID. "
         "The payment report shows each capital settlement based on the reservation. As illustrated, the payments are associated "
         "to the Reservation_ID. The report also shows an aggregate value of all the payments of $21,300. ",
         unsafe_allow_html=True)
"\n"
# ________Four Reports Diagram___________#
image22 = Image.open("Data_PNG_JPG_Files/SystemMockup4Reports1.png")
st.image(image22, use_column_width="always")
image23 = Image.open("Data_PNG_JPG_Files/SystemMockup4Reports2.png")
st.image(image23, use_column_width="always")
st.write("""***Figure 16: System Mockup Four Reports***""")
# _________________________Insert expander Button for References ____________________________#
references_expander = st.expander(label="Expand for References")
references_expander.write("""
Case Study: Hudson Kayak Adventures

Data Source: Arbitrary strings and integers

Author(s): Streamlit Project: Guy Gnakpa | case: Guy Gnakpa & other mentioned in the title

Technologies: Microsoft Project, Microsoft Visio, Microsoft Excel, Microsoft Word, Discord, Streamlit library
""")