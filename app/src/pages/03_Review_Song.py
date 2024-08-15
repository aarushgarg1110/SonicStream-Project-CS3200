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
st.header('Review A Song')
user = st.session_state['username']

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['username']}.")

# User enters song title and review and submits
with st.form("Write a Review"):
    song_title = st.text_input("Input Song title:")
    review_text = st.text_input("Provide review description:")
    submitted = st.form_submit_button("Submit")

if submitted:
    #Construct API URL
    api_url = f'http://web-api:4000/l/listeners/songs/{user}/{song_title}/{review_text} '
    # Replace <keyword> in the API URL with the user's input
    try: 
        # Make a POST request to the API to follow artist
        response = requests.post(api_url)

        #Check if request was successful
        if response.status_code == 200:
            st.write(f"Successfully uploaded review")
        else:
            st.write(f"Failed to upload review. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.write('Could not connect to database to follow upload review!')
        logger.error(f"Error occurred: {e}")
else:
    st.write("Please submit review.")