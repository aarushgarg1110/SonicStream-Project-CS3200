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
user_input = st.text_input("Which user would you like to ban: ")

# Check if the user has entered something
if user_input:

    #Construct API URL
    api_url = f'http://web-api:4000/ma/admins/ban/{user_input}'
   
    try: 
        # Make a POST request to the API to follow artist
        response = requests.delete(api_url)

        #Check if request was successful
        if response.status_code == 200:
            st.write(f"Successfully deleted {user_input}")
        else:
            st.write(f"Failed to delete {user_input}. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.write('could not connect to database to delete user!')
        logger.error(f"Error occurred: {e}")
else:
    st.write("Please enter an user name.")