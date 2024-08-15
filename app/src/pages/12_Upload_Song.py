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

# Set the header of the page
st.header('Upload A Song')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['firstname']}.")

# Create input boxes for the necessary song details
fname = st.session_state['firstname']
lname = st.session_state['lastname']
album = st.text_input("Enter the album name:")
title = st.text_input("Enter the song title:")
genre = st.text_input("Enter the genre:")
duration = st.text_input("Enter the duration (in time format):")

# Add a button to submit the form
if st.button("Upload Song"):
    # Check if all fields are filled
    if album and title and genre and duration:
        try:
            # Replace with your API URL
            api_url = f'http://web-api:4000/a/artists/songs/upload/{fname}/{lname}/{album}/{title}/{genre}/0:{duration}'
            
            # Make the POST request to the API
            response = requests.post(api_url)
            
            # Check the response status
            if response.status_code == 200:
                st.success("Song uploaded successfully!")
            else:
                st.error("Failed to upload the song. Please try again.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please fill in all the fields.")
