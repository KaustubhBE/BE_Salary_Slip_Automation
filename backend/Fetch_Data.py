import gspread
from google.oauth2.service_account import Credentials

def fetch_google_sheet_data(sheet_id, sheet_name, credentials_file):
    
    try:
        # Define the scope for the Google Sheets API
        scope = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
        
        # Authenticate using the service account credentials
        creds = Credentials.from_service_account_file(credentials_file, scopes=scope)
        client = gspread.authorize(creds)
        
        # Open the Google Sheet and the specific sheet/tab
        sheet = client.open_by_key(sheet_id).worksheet(sheet_name)
        
        # Fetch all data
        data = sheet.get_all_values()
        return data
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
