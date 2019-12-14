from inputs.creds import *
import json
import requests

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
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
    