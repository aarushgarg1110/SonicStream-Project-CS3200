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
st.header('Company Revenue')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['username']}.")
# Create a text input box for the user to enter the mood
user_input = st.text_input("Enter the mood you are feeling today: ")

# Check if the user has entered something
if user_input:
    # Replace <keyword> in the API URL with the user's input
    try: 
        api_url = f'http://web-api:4000/l/listeners/song/{user_input}'
    except:
        st.write('could not connect to database to find songs!')

    # Make a GET request to the API
    response = requests.get(api_url).json()
        
    # Display the DataFrame in Streamlit
    st.dataframe(response, column_order=('title', 'album', 'genre'))
else:
    st.write("Please enter a mood.")
