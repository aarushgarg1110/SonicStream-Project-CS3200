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
st.header('View Your Most Popular Songs')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['firstname']}.")
st.write(f"Here are your most popular songs by Play Count")
fname = st.session_state['firstname']
lname = st.session_state['lastname']

# Replace <keyword> in the API URL with the user's input
try: 
    api_url = f'http://web-api:4000/a/artists/popularSongs/{fname}/{lname}'
    
    # Make the GET request to the API
    response = requests.get(api_url).json()
except:
    st.write('Could not connect to database to find songs!')

if response:
    # Convert the response to a DataFrame
    df = pd.DataFrame(response, columns=['song_title', 'total_playcount'])
    # Convert string data to numeric values
    df['total_playcount'] = pd.to_numeric(df['total_playcount'])
    # Display the data in an interactive table
    st.dataframe(df, use_container_width=True)
    
    # Plot the data using Plotly Express
    fig = px.bar(
        df, 
        x='song_title', 
        y='total_playcount', 
        title='Popular Songs by Playcount', 
        labels={'song_title': 'Song Title', 'total_playcount': 'Total Playcount'}
        # color='total_playcount',
        # color_continuous_scale='Blues'
    )

    # Customize the chart appearance
    fig.update_layout(
        title_font=dict(size=24, color='black', family="Arial"),
        xaxis_title_font=dict(size=18, color='black', family="Arial"),
        yaxis_title_font=dict(size=18, color='black', family="Arial")
    )

    # Display the bar chart
    st.plotly_chart(fig)
else:
    st.write('No play count data available.')
