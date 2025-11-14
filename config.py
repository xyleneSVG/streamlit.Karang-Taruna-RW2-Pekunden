import streamlit as st
from google.oauth2.service_account import Credentials
import gspread
from dotenv import load_dotenv

load_dotenv()

def get_google_sheets_client():
    creds_dict = st.secrets["connections"]["gsheets"]
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
    gc = gspread.authorize(creds)
    sheet = gc.open_by_url(creds_dict["spreadsheet"])
    return sheet.sheet1

GAS_WEBAPP_URL = "https://script.google.com/macros/s/AKfycbwiMsj3KCkgR2C0nC_P8IE_lnHtxepRYMiSziotydJrdSJlkmL2yr5q190KDCP_QYe0/exec"