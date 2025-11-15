import streamlit as st

def render_upload_form():
    with st.form("upload_form"):
        st.subheader("📸 Upload Dokumentasi Kegiatan")

        activity_name = st.text_input("Nama Kegiatan")
        meeting_date = st.date_input("Tanggal Kegiatan")

        photos = st.file_uploader(
            "Upload Foto",
            type=["jpg", "jpeg", "png"],
            accept_multiple_files=True
        )

        submit = st.form_submit_button("Upload")

        if submit:
            if not activity_name:
                st.error("Nama kegiatan wajib diisi!")
                return None

            if not photos:
                st.error("Minimal upload 1 foto!")
                return None

            return {
                "activity_name": activity_name,
                "meeting_date": meeting_date.strftime("%Y-%m-%d"),
                "photos": photos
            }
