import streamlit as st
from apps.activity_documentation.main import run as run_activity
from apps.meeting_documentation.main import run as run_meeting

st.set_page_config(page_title="KT. RW2 PEKUNDEN APPS", layout="centered")

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("images/logo.png", width=500)

st.markdown(
    """
    <h1 style='text-align:center; margin-bottom: 0px;'>
        <b>KARANG TARUNA RW 02 PEKUNDEN APPS</b>
    </h1>
    """,
    unsafe_allow_html=True
)

st.write("")  

st.subheader("📌 Pilih Aplikasi")

app = st.selectbox(
    "Silakan pilih menu:",
    ["📸 Dokumentasi Kegiatan", "💬 Dokumentasi Pertemuan"],
    index=None
)

if app == "📸 Dokumentasi Kegiatan":
    run_activity()

elif app == "💬 Dokumentasi Pertemuan":
    run_meeting()
