from inputs.creds import *
import json
import requests

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
<<<<<<< HEAD
SETTINGS_RANGE = 'Settings!A1:B2'

def readSettings():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    url = "https://sheets.googleapis.com/v4/spreadsheets/" + \
        SPREADSHEET_ID + "/values/" + SETTINGS_RANGE    
    headers = {
       'cache-control': "no-cache"
       }       
    params = {
        'key': GoogleAPIkey
    }       
    payload = ""
    response = requests.request("GET", url, data=payload, headers=headers, params=params)
    settings = json.loads(response.text)
    with open('data/googleSettings.json','w') as outfile:
        json.dump(settings, outfile)
    return settings
    
def writeSettings(settings):

    url = "https://sheets.googleapis.com/v4/spreadsheets/" + \
        SPREADSHEET_ID + "/values/" + SETTINGS_RANGE    
    headers = {
       'cache-control': "no-cache",
       'Content-Type': 'application/json'
       }       
    params = {
        'valueInputOption':'USER_ENTERED',
        'key': GoogleAPIkey,
    }       
    payload = settings
    response = requests.request("PUT", url, data=payload, headers=headers, params=params)
    message = json.loads(response.text)
    return message

if __name__ == '__main__':
    s = readSettings()
    s = s['values']
    print(s)
    
    with open('data/googleSettings.json','r') as infile:
        f = json.load(infile)
    print("File data:")
    print(f)
    print('')
    
    f['values'][0][0] = 3
    print(f)
    print('')
    
    m = writeSettings(json.dumps(f))
    print(m)
    
=======
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
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
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
        print('Name, Major:')
        for row in values:
            # Print columns A and B, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[1]))
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

def format_sheet():



if __name__ == '__main__':

    creds = get_creds()
    service = build('sheets', 'v4', credentials=creds)

    # Read Data from the Pletthome spreadsheet
    data = read_sheet(service, PLETTHOME_SHEET_ID, SAMPLE_RANGE)
    print(" ")
    print(data)

    # Write data to the Pletthome spreadsheet
    data = [
        [0,1,2,3,4],
        [10,11,12,13,14]
        ]

    write_sheet(service, PLETTHOME_SHEET_ID, SAMPLE_RANGE, data)

    # Format the Pletthome spreadsheet
    #
>>>>>>> refs/remotes/origin/master
