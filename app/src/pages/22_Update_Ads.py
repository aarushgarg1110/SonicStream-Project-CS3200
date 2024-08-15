import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import matplotlib.pyplot as plt
import requests
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('Update an Ad')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['username']}.")
# Create a text input box for the user to enter the mood

with st.form("Write a Review"):
    name = st.text_input("Enter the name of the ad you wish to update: ")
    status = st.text_input("Enter the new status for this ad: ")
    submitted = st.form_submit_button("Submit")

# Check if the user has entered something
if submitted:
    # Replace <keyword> in the API URL with the user's input
    api_url = f'http://web-api:4000/ma/admins/ad_fetch/{status}/{name}'
    try:
        response = requests.put(api_url)
        if response.status_code == 200:
            st.write(f"Successfully changed status.")
        else:
            st.write(f"Failed to update status. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.write('Could not connect to database to follow update status!')
        logger.error(f"Error occurred: {e}")
else:
    st.write("Please type in ad name and status.")