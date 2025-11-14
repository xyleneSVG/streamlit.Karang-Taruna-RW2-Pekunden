import streamlit as st
import time
from config import get_google_sheets_client, GAS_WEBAPP_URL
from services import GoogleSheetsService, UploadService
from ui import render_meeting_form, display_meeting_history
from utils.ai import formatedWithAI

# Page Config
st.set_page_config(page_title="Pencatat Notulen Rapat", layout="centered")
st.title("📝 Pencatat Notulen Rapat")

# Initialize Services
worksheet = get_google_sheets_client()
sheets_service = GoogleSheetsService(worksheet)
upload_service = UploadService(GAS_WEBAPP_URL)

# Initialize Session State
if 'is_processing' not in st.session_state:
    st.session_state.is_processing = False
if 'form_data' not in st.session_state:
    st.session_state.form_data = None

# Render Form (jika tidak sedang proses)
if not st.session_state.is_processing:
    form_data = render_meeting_form()
    
    if form_data:
        st.session_state.form_data = form_data
        st.session_state.is_processing = True
        st.rerun()

# Process Form Submission
if st.session_state.is_processing and st.session_state.form_data:
    with st.spinner("⏳ Sedang memproses... Jangan refresh halaman!"):
        try:
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            form_data = st.session_state.form_data
            meeting_date = form_data['meeting_date']
            start_time = form_data['start_time']
            end_time = form_data['end_time']
            notes = form_data['notes']
            photo_files = form_data['photo_files']
            
            meeting_date_str = meeting_date.strftime("%Y-%m-%d")
            
            # Upload Photos
            folder_link = upload_service.upload_photos(
                photo_files, 
                meeting_date_str, 
                progress_bar, 
                status_text
            )
            
            # Format Notes with AI
            status_text.info("💬 Memproses notulen dengan AI...")
            progress_bar.progress(0.90)
            formatted_notes = formatedWithAI(notes)
            
            # Save to Google Sheets
            status_text.info("💾 Menyimpan ke Google Sheet...")
            progress_bar.progress(0.95)
            sheets_service.save_meeting_notes(
                meeting_date_str,
                start_time,
                end_time,
                formatted_notes,
                folder_link
            )
            
            progress_bar.progress(1.0)
            status_text.empty()
            progress_bar.empty()
            
            st.success("✅ Notulen berhasil disimpan!")
            st.balloons()
            
            st.session_state.is_processing = False
            st.session_state.form_data = None
            time.sleep(2)
            st.rerun()
            
        except Exception as e:
            st.error(f"❌ Terjadi kesalahan: {e}")
            st.session_state.is_processing = False
            st.session_state.form_data = None
            time.sleep(2)
            st.rerun()

# Display Meeting History
display_meeting_history(worksheet)