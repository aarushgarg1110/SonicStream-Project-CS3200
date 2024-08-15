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

# Make a GET request to the API
api_url = f'http://web-api:4000/l/listeners/seeArtists'
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Extract the data from the JSON response
    artist_data = response.json()

    # Extract artist names from the fetched data
    artist_names = [artist['name'] for artist in artist_data]

    # Populate the selectbox with artist names
    selected_artist = st.selectbox("Select an Artist", artist_names, index=None, placeholder="Select artist...")

    confirmed_artist = None

    # Add a button to confirm the selection
    if st.button("Confirm Selection"):
        confirmed_artist = selected_artist
        st.write(f"You selected: {confirmed_artist}")
else:
    st.error("Failed to fetch data from the API.")

# Check if the user has entered something
if confirmed_artist:

    #Construct API URL
    api_url = f'http://web-api:4000/l/listeners/artists/{user}/{confirmed_artist}'
   
    try: 
        # Make a POST request to the API to follow artist
        response = requests.post(api_url)

        # Log the API response
        logger.info(f"API Response: {response.text}")
        #Check if request was successful
        if response.status_code == 200:
            st.write(f"Successfully followed {confirmed_artist}")
        elif response.status_code == 400:
            st.write(f"Artist {confirmed_artist} not found or already followed.")
        else:
            st.write(f"Failed to follow {confirmed_artist}. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.write('could not connect to database to follow artist!')
        logger.error(f"Error occurred: {e}")
else:
    st.write("Please enter an artist name.")
