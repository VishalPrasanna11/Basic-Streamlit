import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Multi-Tab Dashboard", layout="wide")

# Add a title
st.title("Dashboard with Multiple Tabs")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Data Analysis", "Visualization", "Settings"])

# Tab 1: Data Analysis
with tab1:
    st.header("Data Analysis Tab")
    
    # Create sample data
    data = pd.DataFrame({
        'Date': pd.date_range(start='2024-01-01', periods=100),
        'Sales': np.random.randint(100, 1000, 100),
        'Profit': np.random.randint(50, 500, 100)
    })
    
    # Display data
    st.subheader("Sample Data")
    st.dataframe(data)
    
    # Basic statistics
    st.subheader("Summary Statistics")
    st.write(data.describe())

# Tab 2: Visualization
with tab2:
    st.header("Visualization Tab")
    
    # Create different chart options
    chart_type = st.selectbox(
        "Select Chart Type",
        ["Line Chart", "Bar Chart", "Scatter Plot"]
    )
    
    if chart_type == "Line Chart":
        fig = px.line(data, x='Date', y=['Sales', 'Profit'])
        st.plotly_chart(fig)
    
    elif chart_type == "Bar Chart":
        fig = px.bar(data, x='Date', y='Sales')
        st.plotly_chart(fig)
    
    else:  # Scatter Plot
        fig = px.scatter(data, x='Sales', y='Profit')
        st.plotly_chart(fig)

# Tab 3: Settings
with tab3:
    st.header("Settings Tab")
    
    # Add some settings options
    st.subheader("Display Settings")
    show_raw_data = st.checkbox("Show Raw Data")
    date_range = st.date_input("Select Date Range", [data['Date'].min(), data['Date'].max()])
    
    # Color theme setting
    theme = st.selectbox(
        "Select Color Theme",
        ["Default", "Dark", "Light"]
    )
    
    # Update frequency
    update_frequency = st.slider(
        "Data Update Frequency (minutes)",
        min_value=1,
        max_value=60,
        value=5
    )
    
    # Save settings button
    if st.button("Save Settings"):
        st.success("Settings saved successfully!")

# Add a sidebar
with st.sidebar:
    st.header("Dashboard Controls")
    st.write("Use this sidebar for additional controls and filters")
    
    # Add some filter options
    data_filter = st.multiselect(
        "Filter Data",
        ["Sales", "Profit"],
        default=["Sales", "Profit"]
    )
    
    # Add a date range filter
    date_filter = st.date_input(
        "Filter by Date Range",
        [data['Date'].min(), data['Date'].max()]
    )