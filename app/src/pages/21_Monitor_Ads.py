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
st.header('Monitor Ads')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['username']}.")
st.write(f"Here are all of your running ads")

try:
    api_url = f'http://web-api:4000/ma/admins/seeAds'
except:
    st.write('could not connect to database to find songs!')

# Make a GET request to the API
response = requests.get(api_url).json()

# Display the DataFrame in Streamlit
st.dataframe(response)
