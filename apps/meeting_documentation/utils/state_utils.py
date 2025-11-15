import streamlit as st
import time

def reset_processing_state(delay: float = 2.0):
    st.session_state.is_processing = False
    st.session_state.form_data = None
    time.sleep(delay)
    st.rerun()
