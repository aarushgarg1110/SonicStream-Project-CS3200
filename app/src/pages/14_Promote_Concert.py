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
# Use a date picker for the date input
date = st.date_input("Select the date:")

# Add a button to submit the form
if st.button("Upload Concert"):
    # Check if all fields are filled
    if venue and date:
        try:
            # Convert the date to a string in the desired format (e.g., YYYY-MM-DD)
            date_str = date.strftime('%Y-%m-%d')

            # Replace with your API URL
            api_url = f'http://web-api:4000/a/artists/concerts/upload/{fname}/{lname}/{venue}/{date_str}'
            
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
    
st.write(f"Here are all of your upcoming concerts")

try:
    api_url = f'http://web-api:4000/a/artists/concerts/upcoming/{fname}/{lname}'
except:
    st.write('could not connect to database to find songs!')

# Make a GET request to the API
response = requests.get(api_url).json()

# Display the DataFrame in Streamlit
st.dataframe(response)
