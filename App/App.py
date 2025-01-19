import streamlit as st
import base64
from PIL import Image
import os

# Set page config
st.set_page_config(
    page_title="Resumeter",
    page_icon="./Logo/recommend.png",
    layout="wide"
)

# Custom CSS with Avenir font and new styling
st.markdown("""
    <link href="https://fonts.cdnfonts.com/css/avenir" rel="stylesheet">
    <style>
        @import url('https://fonts.cdnfonts.com/css/avenir');
                
        /* Main Styles */
        body {
            font-family: 'Avenir', sans-serif !important;
            color: #0A192F;
            background-color: #ECF3FB;
        }
        
        /* Header Styling */
        .stApp header {
            background-color: white;
            border-bottom: 1px solid #E5E7EB;
        }
        
        /* Custom Classes */
        .main-header {
            padding: 2rem 0;
            text-align: center;
            background: white;
            margin-bottom: 2rem;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        
        .logo-img {
            max-width: 200px;
            margin: 0 auto;
        }
        
        /* Form Styling */
        .stTextInput > div > div > input {
            border-radius: 8px;
            border: 1px solid #E5E7EB;
        }
        
        .stButton > button {
            border-radius: 8px;
            background-color: #0A192F;
            color: white;
            padding: 0.5rem 1rem;
        }
        
        /* Dark Mode Support */
        @media (prefers-color-scheme: dark) {
            body {
                background-color: #0A192F;
                color: #ECF3FB;
            }
            
            .main-header {
                background: #0A192F;
                border: 1px solid #2D3748;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Add logo and header
st.markdown("""
    <div class="main-header">
        <img src="./Logo/RESUM.png" class="logo-img" alt="Resumeter Logo">
        <h1 style="font-family: 'Avenir', sans-serif; margin-top: 1rem;">Resumeter</h1>
        <p style="font-family: 'Avenir', sans-serif;">AI-powered resume analyzer and recommendation engine</p>
    </div>
""", unsafe_allow_html=True)

# Rest of your existing App.py code here...
# [Keep all the existing functionality, just update the styling]