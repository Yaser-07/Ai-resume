import streamlit as st

def theme_toggle():
    if 'theme' not in st.session_state:
        st.session_state.theme = 'light'
    
    theme = st.sidebar.radio(
        "Choose Theme",
        ('Light', 'Dark'),
        index=0 if st.session_state.theme == 'light' else 1
    )
    
    st.session_state.theme = theme.lower()
    
    # Inject custom CSS based on theme
    if st.session_state.theme == 'dark':
        st.markdown("""
            <style>
                .dark {
                    background-color: var(--primary-dark);
                    color: var(--primary-light);
                }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
                body {
                    background-color: var(--primary-light);
                    color: var(--primary);
                }
            </style>
        """, unsafe_allow_html=True)