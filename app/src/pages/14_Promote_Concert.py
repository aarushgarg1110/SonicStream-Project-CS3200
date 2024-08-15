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
st.write(f"### Hi, {st.session_state['firstname']}.")

# Create input boxes for the necessary song details
fname = st.session_state['firstname']
lname = st.session_state['lastname']
venue = st.text_input("Enter the venue:")
date = st.text_input("Enter the date:")

# Add a button to submit the form
if st.button("Upload Concert"):
    # Check if all fields are filled
    if venue and date:
        try:
            # Replace with your API URL
            api_url = f'http://web-api:4000/a/artists/concerts/upload/{fname}/{lname}/{venue}/{date}'
            
            # Make the POST request to the API
            response = requests.post(api_url)
            
            # Check the response status
            if response.status_code == 200:
                st.success("Concert uploaded successfully!")
            else:
                st.error("Failed to upload the concert. Please try again.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please fill in all the fields.")
