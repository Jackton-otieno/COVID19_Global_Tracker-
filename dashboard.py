# dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px

# Set page title
st.title("COVID-19 Global Tracker Dashboard")

# Load the dataset
df = pd.read_csv('synthetic_covid19_data.csv')

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Get unique countries from the dataset
available_countries = sorted(df['location'].unique())

# Sidebar for country selection
st.sidebar.header("Filter Options")
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    options=available_countries,
    default=['India', 'USA', 'Canada']  # Updated default values to match dataset
)

# Filter data based on selected countries
if selected_countries:
    df_filtered = df[df['location'].isin(selected_countries)]
else:
    df_filtered = df.copy()
    st.warning("No countries selected. Showing data for all countries.")

# Plot Total Cases Over Time
st.subheader("Total Cases Over Time")
fig_cases = px.line(df_filtered, x='date', y='total_cases', color='location',
                    title='Total COVID-19 Cases Over Time')
fig_cases.update_xaxes(title_text='Date')
fig_cases.update_yaxes(title_text='Total Cases')
st.plotly_chart(fig_cases)

# Plot Total Deaths Over Time
st.subheader("Total Deaths Over Time")
fig_deaths = px.line(df_filtered, x='date', y='total_deaths', color='location',
                     title='Total COVID-19 Deaths Over Time')
fig_deaths.update_xaxes(title_text='Date')
fig_deaths.update_yaxes(title_text='Total Deaths')
st.plotly_chart(fig_deaths)

# Plot Vaccination Progress
st.subheader("Vaccination Progress Over Time")
fig_vaccinations = px.line(df_filtered, x='date', y='total_vaccinations', color='location',
                           title='Total Vaccinations Over Time')
fig_vaccinations.update_xaxes(title_text='Date')
fig_vaccinations.update_yaxes(title_text='Total Vaccinations')
st.plotly_chart(fig_vaccinations)