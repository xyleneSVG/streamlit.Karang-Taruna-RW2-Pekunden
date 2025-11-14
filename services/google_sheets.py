from datetime import datetime

class GoogleSheetsService:
    def __init__(self, worksheet):
        self.worksheet = worksheet
    
    def save_meeting_notes(self, meeting_date, start_time, end_time, notes, folder_link):
        new_row = [
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            meeting_date,
            str(start_time),
            str(end_time),
            notes,
            folder_link if folder_link else ""
        ]
        self.worksheet.append_row(new_row)
    
    def get_all_records(self):
        return self.worksheet.get_all_records()