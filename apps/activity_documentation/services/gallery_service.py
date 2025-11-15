import requests

class GalleryService:
    def __init__(self, gas_url):
        self.gas_url = gas_url

    def list_folders(self):
        return requests.post(self.gas_url, json={"action": "listFolders"}).json()

    def list_files(self, folder_id):
        data = requests.post(self.gas_url, json={
            "action": "listFiles",
            "folderId": folder_id
        }).json()

        if data["status"] == "success":
            for f in data["files"]:
                file_id = f["id"]
                f["directUrl"] = f"https://drive.google.com/uc?export=view&id={file_id}"

        return data

    def fetch_image_bytes(self, direct_url):
        response = requests.get(direct_url)
        return response.content
