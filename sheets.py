from __future__ import print_function
from inputs.creds import *
import json
import requests
import os.path
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
PLETTHOME_SHEET_ID = '1MZ8PpknP19lBbdlDyEmMTiS6a6Vdd9OAd69qQTasEXk'
SAMPLE_RANGE = 'Settings!A3:E7'

def get_creds():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('inputs/token.pickle'):
        with open('inputs/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'inputs/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('inputs/token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def read_sheet(service, sheet_id, range_str):

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id,
                                range=range_str).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        pass
        #for row in values:
            # Print columns A and B, which correspond to indices 0 and 4.
            #print(row)
    return values

def write_sheet(service, sheet_id, range_str, data):

    values = data
    body = {
        'values': values
        }
    result = service.spreadsheets().values().update(
        spreadsheetId=sheet_id, range=range_str,
        valueInputOption='USER_ENTERED', body=body).execute()

    print('{0} cells updated.'.format(result.get('updatedCells')))


if __name__ == '__main__':

    creds = get_creds()
    service = build('sheets', 'v4', credentials=creds)

    # Read Data from the Pletthome spreadsheet
    data = read_sheet(service, PLETTHOME_SHEET_ID, SAMPLE_RANGE)
    print(" ")
    with open('data/pletthome_settings.json','w') as file:
        file.write(str(data))
    #print(data)
    sys.exit()

    # Write data to the Pletthome spreadsheet
    data = [
        [0,1,2,3,4],
        [10,11,12,13,14]
        ]

    write_sheet(service, PLETTHOME_SHEET_ID, SAMPLE_RANGE, data)
