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
st.header('View Income From Songs')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['firstname']}.")
st.write(f"Here are your payouts from your songs")
fname = st.session_state['firstname']
lname = st.session_state['lastname']

# Replace <keyword> in the API URL with the user's input
try: 
    api_url = f'http://web-api:4000/a/artists/revenue/{fname}/{lname}'
    response = requests.get(api_url).json()
except:
    st.write('Could not connect to database to find songs!')

if response:
    # Convert the response to a DataFrame
    df = pd.DataFrame(response, columns=['song_title', 'revenue_in_$'])
    # Convert string data to numeric values
    df['revenue_in_$'] = pd.to_numeric(df['revenue_in_$'])
    df.index = range(1, len(df) + 1)
    # df.T.reset_index()
    
    # Display the data in an interactive table
    st.dataframe(df, use_container_width=True)

    # Create a bar chart to visualize the income
    fig = px.bar(
        df, 
        x='song_title', 
        y='revenue_in_$', 
        title='Income by Song', 
        labels={'song_title': 'Song Title', 'revenue_in_$': 'Revenue ($)'},
        color='revenue_in_$',
        color_continuous_scale='Blues'
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
    st.info('No revenue data available.')

