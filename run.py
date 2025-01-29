import streamlit as st
import requests
from bs4 import BeautifulSoup
import PyPDF2
import io
import base64

# Set page configuration
st.set_page_config(page_title="DataNexus Pro", layout="wide")

# Add a title
st.title("DataNexus Pro: Unified Data Extraction for Enterprise & Open Source")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Data Source/Extraction", "Extracted Content", "Analysis Dashboard"])

# Initialize session state for extracted content
if 'extracted_content' not in st.session_state:
    st.session_state.extracted_content = ""

# Function to extract text from PDF
def extract_pdf_text(pdf_file):
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        return f"Error extracting PDF: {str(e)}"

# Function to scrape web content
def scrape_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract text from paragraphs
        text = "\n\n".join([p.get_text() for p in soup.find_all('p')])
        return text
    except Exception as e:
        return f"Error scraping website: {str(e)}"

# Function to create download link
def get_download_link(text, filename="extracted_content.md"):
    b64 = base64.b64encode(text.encode()).decode()
    return f'<a href="data:text/markdown;base64,{b64}" download="{filename}">Download Markdown File</a>'

# Sidebar
with st.sidebar:
    st.header("Dashboard Controls")
    st.write("Use this sidebar for PDF or Web Scraping")
    extraction_type = st.selectbox(
        "Select Extraction Type",
        ["PDF Extraction", "Web Scraping"]
    )

# Tab 1: Data Source/Extraction
with tab1:
    st.header("Data Source/Extraction")
    
    if extraction_type == "PDF Extraction":
        uploaded_file = st.file_uploader("Upload PDF file", type=['pdf'])
        if uploaded_file is not None and st.button("Extract"):
            st.session_state.extracted_content = extract_pdf_text(uploaded_file)
            st.success("PDF extracted successfully!")
            
    else:  # Web Scraping
        url = st.text_input("Enter website URL")
        if url and st.button("Scrape"):
            st.session_state.extracted_content = scrape_website(url)
            st.success("Website scraped successfully!")

# Tab 2: Extracted Content
with tab2:
    st.header("Extracted Content")
    if st.session_state.extracted_content:
        st.markdown(st.session_state.extracted_content)
        st.markdown(get_download_link(st.session_state.extracted_content), unsafe_allow_html=True)
    else:
        st.info("No content extracted yet. Please use the Data Source/Extraction tab to extract content.")

# Tab 3: Analysis Dashboard
with tab3:
    st.header("Analysis Dashboard")
    if st.session_state.extracted_content:
        # Basic text analysis
        word_count = len(st.session_state.extracted_content.split())
        char_count = len(st.session_state.extracted_content)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Word Count", word_count)
        with col2:
            st.metric("Character Count", char_count)
        
        # Add more analysis features as needed
    else:
        st.info("No content to analyze. Please extract content first.")

# Add CSS to improve the download button appearance
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)