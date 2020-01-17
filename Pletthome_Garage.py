from sheets import *
from inputs.settings import *
from inputs.creds import *
import requests
import json

def getBrightness():
    url = "https://garagepi.local:5000/brightness"
    headers = {
       'auth-token': GARAGEPI_TOKEN
       }
    payload = ""
    response = requests.request("GET", url, data=payload, headers=headers, verify=False)
    r = json.loads(response.text)
    return r

def getImage():
    url = "https://garagepi.local:5000/view"
    headers = {
       'auth-token': GARAGEPI_TOKEN
       }
    payload = ""
    response = requests.request("GET", url, data=payload, headers=headers, verify=False)
    r = json.loads(response.text)
    return r

def getStatus(b):
    if b["brightness"] < 0.01:
        s = "Door CLOSED and light OFF"
    elif 0.15 < b["brightness"] < 0.17:
        s = "Door OPEN"
    elif 0.12 < b["brightness"] < 0.2:
        s = "Door CLOSED and light ON"
    elif b["brightness"] > 0.2:
        s = "Door OPEN"
    else:
        s = "The status is unclear"
    return s

if __name__ == '__main__':

    creds = get_creds()
    service = build('sheets', 'v4', credentials=creds)

    with open('data/pletthome_settings.json','r') as file:
        settings = json.load(file)

    l = []
    b = getBrightness()
    l.append([b["brightness"]])
    l.append([getStatus(b)])

    write_sheet(service, PLETTHOME_SHEET_ID, \
        settings["EVERGREEN_GARAGE_BRIGHTNESS"], l)
