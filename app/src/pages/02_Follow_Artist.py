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
st.header('Follow An Artist')
user = st.session_state['username']
# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['username']}.")
# Create a text input box for the user to enter the mood
user_input = st.text_input("Which artist would you like to follow: ")

# Check if the user has entered something
if user_input:

    #Construct API URL
    api_url = f'http://web-api:4000/l/listeners/artists/{user}/{user_input}'
   
    try: 
        # Make a POST request to the API to follow artist
        response = requests.post(api_url)

        # Log the API response
        logger.info(f"API Response: {response.text}")
        #Check if request was successful
        if response.status_code == 200:
            st.write(f"Successfully followed {user_input}")
        elif response.status_code == 400:
            st.write(f"Artist {user_input} not found or already followed.")
        else:
            st.write(f"Failed to follow {user_input}. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.write('could not connect to database to follow artist!')
        logger.error(f"Error occurred: {e}")
else:
    st.write("Please enter an artist name.")
