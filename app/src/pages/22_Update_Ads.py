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
user_input = st.text_input("Enter the name of the ad you wish to update: ")
user_input_2 = st.text_input("Enter the new status for this ad: ")

# Check if the user has entered something
if user_input and user_input_2:
    # Replace <keyword> in the API URL with the user's input
    try:
        api_url = f'http://web-api:4000/ma/admins/ad_fetch'
    except:
        st.write('could not connect to database to update ads!')

    data = {}
    data['name'] = user_input
    data['status'] = user_input_2

    # Make a put request to the API
    requests.put(api_url, json=data)

    # Display a success message in streamlit
    st.write(data)
    st.write(f'Updated ad with ID {user_input} to status {user_input_2}')

else:
    st.write("Please enter an ad name & status.")
