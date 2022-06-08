from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys_gsheet.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1Ywl60lnMbqM2WCamnT7BzTtnIIEHaVRcw3_sG4JCB0c'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="passrate!A1:C5").execute()

values = result.get('values', [])
print(values)
aoa=[[]]
request = service.spreadsheets().values().update(spreadsheetId='1Ywl60lnMbqM2WCamnT7BzTtnIIEHaVRcw3_sG4JCB0c',
                                                 range='passrate!A6', valueInputOption='USER_ENTERED', body={"values":aoa
        })
response = request.execute()



