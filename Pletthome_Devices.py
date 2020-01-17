from sheets import *
from merakiApi import *

if __name__ == '__main__':

    creds = get_creds()
    service = build('sheets', 'v4', credentials=creds)

    r = getGroup()
    o = r[0]['id']
    d = getClients(o)
    #print(d)

    with open('data/pletthome_settings.json','r') as file:
        settings = json.load(file)

    l = []
    for i in range(0,31):
        l.append([""])
    write_sheet(service, PLETTHOME_SHEET_ID, \
        settings['EVERGREEN_DEVICES'], l)
    write_sheet(service, PLETTHOME_SHEET_ID, \
        settings['EVERGREEN_KNOWN_PEOPLE'], l)
    l = []
    p = []
    for x in d['Evergreen - Home']:
        if x['description'] not in l:
            l.append(str(x['description']))
        k = settings['MOBILE_OWNERLIST'].keys()
        if x['description'] in k:
            if x['description'] not in p:
                p.append(str(settings['MOBILE_OWNERLIST'][x['description']]))
    l = [[x] for x in l]
    p = [[x] for x in p]
    write_sheet(service, PLETTHOME_SHEET_ID, \
        settings['EVERGREEN_DEVICES'], l)
    write_sheet(service, PLETTHOME_SHEET_ID, \
        settings['EVERGREEN_KNOWN_PEOPLE'], p)

    l = []
    for i in range(0,20):
        l.append([""])
    write_sheet(service, PLETTHOME_SHEET_ID, \
        settings['ONANOLE_DEVICES'], l)
    l = []
    for x in d['Onanole - Cabin']:
        if [x['description']] not in l:
            l.append([x['description']])
    write_sheet(service, PLETTHOME_SHEET_ID, \
        settings['ONANOLE_DEVICES'], l)
