import base64
import requests
import streamlit as st

class UploadService:
    def __init__(self, gas_url):
        self.gas_url = gas_url
    
    def upload_photos(self, photo_files, meeting_date_str, progress_bar, status_text):
        if not photo_files:
            return None
        
        folder_link = None
        total_files = len(photo_files)
        
        for idx, photo in enumerate(photo_files):
            progress = (idx + 1) / (total_files + 2)  # +2 untuk AI dan save
            progress_bar.progress(progress)
            status_text.info(f"📤 Mengunggah {photo.name}... ({idx + 1}/{total_files})")
            
            content = photo.read()
            b64_content = base64.b64encode(content).decode("utf-8")
            
            payload = {
                "name": photo.name,
                "file": b64_content,
                "mime": photo.type,
                "date": meeting_date_str
            }
            
            try:
                response = requests.post(self.gas_url, json=payload)
                result = response.json()
                
                if result.get("status") == "success" and folder_link is None:
                    folder_link = result["url"]
                elif result.get("status") != "success":
                    st.error(f"❌ Gagal mengunggah {photo.name}: {result.get('message')}")
            except Exception as e:
                st.error(f"❌ Gagal mengunggah {photo.name}: {e}")
        
        return folder_link