# Streamlit Dashboard Applications

This repository contains multiple Streamlit applications demonstrating different capabilities of the Streamlit framework for building data applications.

## Project Overview

The repository includes three main applications:
- A Multi-Tab Dashboard (`demo.py`)
- A Dataset Explorer (`main.py`)
- A Data Extraction Tool (`run.py`)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/VishalPrasanna11/Basic-Streamlit.git
cd Basic-Streamlit
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Applications

To run any of the Streamlit applications, use the following command:
```bash
streamlit run <filename>.py
```

For example:
```bash
streamlit run demo.py
```

## Application Details

### 1. Multi-Tab Dashboard (demo.py)
A dashboard application featuring:
- Multiple tabs for Data Analysis, Visualization, and Settings
- Interactive data visualization using Plotly
- Configurable settings and filters
- Sidebar controls for additional functionality

Key features:
- Data analysis with basic statistics
- Multiple chart types (Line, Bar, Scatter)
- Customizable settings
- Date range filtering

### 2. Dataset Explorer (main.py)
An application for exploring Hugging Face datasets:
- Load and explore popular datasets
- Basic data visualization
- Dataset information display
- Support for both image and text datasets

Features:
- Interactive dataset selection
- Sample data display
- Basic statistics
- Dataset-specific visualizations

### 3. DataNexus Pro (run.py)
A data extraction tool supporting:
- PDF text extraction
- Web scraping
- Content analysis
- Export functionality

Features:
- Multiple data source support
- Text extraction and display
- Basic text analysis
- Download extracted content

## Basic Streamlit Concepts

### Page Configuration
```python
st.set_page_config(
    page_title="App Title",
    layout="wide"
)
```

### Adding Content
```python
# Title and headers
st.title("Main Title")
st.header("Section Header")
st.subheader("Sub Section")

# Display data
st.write("Regular text")
st.dataframe(df)  # Display DataFrame
st.metric("Label", value)  # Display metrics
```

### Interactive Elements
```python
# Input widgets
text_input = st.text_input("Label")
selection = st.selectbox("Label", options=[])
checkbox = st.checkbox("Label")

# Buttons
if st.button("Click Me"):
    # Button action
    pass
```

### Layouts
```python
# Columns
col1, col2 = st.columns(2)
with col1:
    st.write("Column 1")
with col2:
    st.write("Column 2")

# Tabs
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("Tab 1 content")

# Sidebar
with st.sidebar:
    st.write("Sidebar content")
```

### Error Handling
```python
try:
    # Your code
    st.success("Success message")
except Exception as e:
    st.error(f"Error message: {str(e)}")
```

## Best Practices

1. **State Management**
   - Use `st.session_state` for persisting data between reruns
   - Initialize session state variables at the start

2. **Performance**
   - Use `@st.cache_data` for caching computationally expensive operations
   - Load data efficiently using appropriate caching decorators

3. **User Experience**
   - Provide clear instructions and feedback
   - Use appropriate widgets for different types of inputs
   - Include loading indicators for long operations

4. **Code Organization**
   - Separate business logic from UI code
   - Use functions for reusable components
   - Keep the main app file clean and organized

## Common Issues and Solutions

1. **App Rerun Issues**
   - Streamlit reruns the entire script on any interaction
   - Use session state to persist data between reruns
   - Cache expensive computations

2. **Layout Problems**
   - Use appropriate containers (columns, expanders)
   - Consider mobile responsiveness
   - Test different screen sizes

3. **Performance**
   - Cache data loading operations
   - Use efficient data structures
   - Optimize heavy computations

## Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Components](https://streamlit.io/components)
- [Streamlit Community](https://discuss.streamlit.io/)

## Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating a new branch
3. Making your changes
4. Submitting a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.