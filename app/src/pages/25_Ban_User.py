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
st.header('Ban A User')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['username']}.")
# Create a text input box for the user to enter the mood

# get all users to use with a select box
get_users_url = f'http://web-api:4000/ma/admins/get_users'
users = requests.get(get_users_url).json()

users_cleaned = [user['username'] for user in users]

# user_input = st.text_input("Which user would you like to ban: ")
user_input = st.selectbox(
    "Select user to ban",
    users_cleaned,
    index=None,
    placeholder="Select user...",
)

confirmed_user = None
if st.button('Confirm Selection'):
    confirmed_user = user_input
    st.write(f'Selected user {confirmed_user}')

# Check if the user has entered something
if confirmed_user:

    #Construct API URL
    api_url = f'http://web-api:4000/ma/admins/ban/{confirmed_user}'
   
    try: 
        # Make a POST request to the API to follow artist
        response = requests.delete(api_url)

        #Check if request was successful
        if response.status_code == 200:
            st.write(f"Successfully deleted {confirmed_user}")
        else:
            st.write(f"Failed to delete {confirmed_user}. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.write('could not connect to database to delete user!')
        logger.error(f"Error occurred: {e}")
else:
    st.write("Please enter an user name.")