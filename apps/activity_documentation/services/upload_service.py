import base64
import requests

class UploadService:
    def __init__(self, gas_url):
        self.gas_url = gas_url

    def upload_photos(self, activity_name, meeting_date, photos, progress_bar, status):
        folder_link = None

        total = len(photos)
        for i, photo in enumerate(photos):
            status.info(f"Mengunggah foto {i+1}/{total} ...")

            file_bytes = photo.read()
            b64file = base64.b64encode(file_bytes).decode()

            payload = {
                "activity": activity_name,
                "date": meeting_date,
                "name": photo.name,
                "file": b64file,
                "mime": photo.type
            }

            response = requests.post(self.gas_url, json=payload)
            result = response.json()

            if result["status"] != "success":
                raise Exception(result["message"])

            folder_link = result["url"]

            progress_bar.progress((i + 1) / total)

        return folder_link
