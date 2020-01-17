from sheets import *
import datetime

if __name__ == '__main__':

    creds = get_creds()
    service = build('sheets', 'v4', credentials=creds)

    # Read Data from the Pletthome spreadsheet
    SETTINGS_RANGE = 'Settings!A4:B15'
    data = read_sheet(service, PLETTHOME_SHEET_ID, SETTINGS_RANGE)
    settings = {}
    settings['Updated'] = str(datetime.datetime.now())
    for row in data:
        settings[row[0]]=row[1]

    data = read_sheet(service, PLETTHOME_SHEET_ID, settings['STATIC_WHITELIST_RANGE'])
    settings['STATIC_WHITELIST'] = []
    settings['STATIC_WHITELIST'] = data

    data = read_sheet(service, PLETTHOME_SHEET_ID, settings['MOBILE_OWNERLIST_RANGE'])
    settings['MOBILE_OWNERLIST'] = {}
    for row in data:
        settings['MOBILE_OWNERLIST'][row[0]] = row[1]

    with open('data/pletthome_settings.json','w') as file:
        json.dump(settings, file)
