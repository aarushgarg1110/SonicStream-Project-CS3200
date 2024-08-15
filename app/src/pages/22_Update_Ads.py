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

response = requests.get(f'http://web-api:4000/ma/admins/seeAds').json()
ad_names = [r['name'] for r in response]
# this api is for the monitor ads, so it returns more than ad name
# we only care about ad name here, so this isolates the ad name
ad_statuses = ['completed', 'paused', 'active']
# hardcoded list of acceptable statuses to be used in the form

with st.form("Change ad"):
    name = st.selectbox(
        "Select ad name",
        ad_names,
        index=None,
        placeholder="Select ad...",
    )
    status = st.selectbox(
        "Select ad status",
        ad_statuses,
        index=None,
        placeholder="Select status...",
    )
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