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
st.header('Find Songs In Common With Your Friend')
username = st.session_state["username"]

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {username}.")

get_users_url = f'http://web-api:4000//l/listeners/friends/{username}'
users = requests.get(get_users_url).json()
# this extracts a dict with [userID, friendID, listener1, listener2]
# we want the usernames that are not the user accessing this page
# below 2 lines extracts that into users_cleaned

users_unclean = [[u['listener1'], u['listener2']] for u in users]
users_cleaned = [u[0] if u[1] == username else u[1] for u in users_unclean]

user_input = st.selectbox(
    "Select friend to check common songs with",
    users_cleaned,
    index=None,
    placeholder="Select user...",
)

# Create a selection box for the user to enter the mood
friend = None
if st.button('Confirm Selection'):
    friend = user_input
    st.write(f'Selected user {friend}')

# Check if the user has selected
if friend:
    # Replace <keyword> in the API URL with the user's input
    try: 
        api_url = f'http://web-api:4000/l/listeners/songs/{username}/{friend}'
    except:
        st.write('could not connect to database to find songs!')

    # Make a GET request to the API
    response = requests.get(api_url).json()
        
    # Display the DataFrame in Streamlit
    st.dataframe(response, column_order=('title', 'album', 'name'))
else:
    st.write("Please enter friend's username.")
