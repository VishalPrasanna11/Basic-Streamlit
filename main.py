import streamlit as st
import pandas as pd
from datasets import load_dataset

# Page config
st.set_page_config(
    page_title="Dataset Explorer",
    page_icon="📊",
    layout="wide"
)

# Title and introduction
st.title("📊 Dataset Explorer")
st.write("This is a simple Streamlit app that loads data from Hugging Face datasets.")

# User input section
name = st.text_input("What is your name?")
if name:
    st.write(f"Hello, {name}! Let's explore some data together!")

# Dataset selection
dataset_options = [
    "mnist",
    "cifar10",
    "imdb",
    "wmt14",
    "squad"
]

selected_dataset = st.selectbox(
    "Choose a dataset to explore:",
    options=dataset_options
)

# Load dataset with error handling
@st.cache_data
def load_dataset_sample(dataset_name):
    try:
        dataset = load_dataset(dataset_name, split='train[:100]')  # Load just first 100 examples
        return dataset
    except Exception as e:
        st.error(f"Error loading dataset: {str(e)}")
        return None

if st.button("Load Dataset"):
    with st.spinner('Loading dataset...'):
        dataset = load_dataset_sample(selected_dataset)
        
        if dataset is not None:
            st.success(f"Successfully loaded {selected_dataset} dataset!")
            
            # Display dataset info
            st.subheader("Dataset Information")
            
            # Convert to DataFrame for easier display
            df = pd.DataFrame(dataset)
            
            # Display basic statistics
            st.write("Dataset Shape:", df.shape)
            st.write("Columns:", list(df.columns))
            
            # Show sample of the data
            st.subheader("Sample Data")
            st.dataframe(df.head())
            
            # Basic visualizations based on dataset type
            st.subheader("Data Visualization")
            
            if selected_dataset in ['imdb', 'squad']:
                # Text dataset visualization
                st.write("Text Length Distribution")
                if 'text' in df.columns:
                    text_lengths = df['text'].str.len()
                    st.line_chart(text_lengths)
            
            elif selected_dataset in ['mnist', 'cifar10']:
                # Image dataset visualization
                st.write("Sample Images")
                if 'image' in df.columns:
                    cols = st.columns(4)
                    for idx, col in enumerate(cols):
                        if idx < len(df):
                            col.image(df['image'][idx], caption=f"Image {idx}")

# Add sidebar with additional information
with st.sidebar:
    st.header("About")
    st.write("""
    This app demonstrates how to:
    - Load datasets from Hugging Face
    - Display basic dataset information
    - Show sample data
    - Create simple visualizations
    """)
    
    st.header("Dataset Descriptions")
    dataset_descriptions = {
        "mnist": "Handwritten digits dataset",
        "cifar10": "Image classification dataset",
        "imdb": "Movie reviews for sentiment analysis",
        "wmt14": "Machine translation dataset",
        "squad": "Question answering dataset"
    }
    
    st.write(dataset_descriptions)