import streamlit as st
from datetime import datetime

def render_meeting_form():
    with st.form("meeting_form"):
        meeting_date = st.date_input("📅 Tanggal Rapat", datetime.now().date())
        start_time = st.time_input("⏰ Waktu Mulai")
        end_time = st.time_input("🏁 Waktu Selesai")
        notes = st.text_area("🗒️ Isi Notulen", height=200)
        photo_files = st.file_uploader(
            "📸 Upload Foto Dokumentasi",
            type=["jpg", "jpeg", "png"],
            accept_multiple_files=True,
        )
        submitted = st.form_submit_button("💾 Simpan Notulen")
    
    if submitted:
        return {
            'meeting_date': meeting_date,
            'start_time': start_time,
            'end_time': end_time,
            'notes': notes,
            'photo_files': photo_files
        }
    return None