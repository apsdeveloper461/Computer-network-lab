# Import the service_account module for authenticating using a service account
from google.oauth2 import service_account
# Import the build function to create a client for interacting with a Google API
from googleapiclient.discovery import build


# Path to your service account key file (ensure the path is correct)
SERVICE_ACCOUNT_FILE ='api_key.json'
# The ID of your Google Sheet (this is the unique identifier for your Google Sheet)
SPREADSHEET_ID = '1eMRho-kb5S-NVbku48gW1QZJkNvycNF7uqOjrpVk9h4'



# Authenticate and create the Sheets API client
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=["https://www.googleapis.com/auth/spreadsheets"]
)
service = build('sheets', 'v4', credentials=credentials)

# Function to read data from the Google Sheet
def read_data(range_name):
    sheet = service.spreadsheets()
    result = sheet.values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=range_name
    ).execute()
    return result.get('values', [])

# Function to append data to the Google Sheet
def append_data(range_name, values):
    sheet = service.spreadsheets()
    body = {'values': values}
    result = sheet.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=range_name,
        valueInputOption='RAW',
        body=body
    ).execute()
    return result

# Example usage of the above functions
if __name__ == '__main__':
    # Specify the range of cells where you want to append the data (e.g., 'Sheet1')
    range_name = 'Sheet1!A1:B3'  # Target sheet where data will be appended

    # Reading data from the Google Sheet
    print("Reading data...")
    data = read_data(range_name)  # Read columns A to C
    print("Data:", data)

    # Append new data to the Google Sheet
    print("Appending data...")
    new_values = [
        ["Name", "Age", "City"],  # Header row (optional)
        ["Alicena", 25, "New York"],  # First data row
        ["Bob", 30, "San Francisco"]  # Second data row
    ]
    append_result = append_data(range_name, new_values)  # Append data
    print("Append Result:", append_result)  # Print the result of the append operation