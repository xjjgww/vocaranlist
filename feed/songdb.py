import json
from requests_html import HTMLSession
import re

def getvideo(sm):
    mylist = {}
    session = HTMLSession()
    r = session.get('https://www.nicovideo.jp/watch/'+sm) # HTMLResponse
    # print(r.__dict__.keys())
    # 'X-XSS-Protection': '1; mode=block'
    if 'X-XSS-Protection' or sm=="sm35714718" in dict(r.headers):
        mylist['err'] = 1
        return mylist
    ele = r.html.find('#js-initial-watch-data') # list
    if len(ele) == 0:
        mylist['err'] = 2
        return mylist
    dataapi = ele[0].attrs['data-api-data'] # str
    dataapi = re.sub(r"\"description\".+?\"thumbnailURL\"", "\"thumbnailURL\"", dataapi)
    jvideo = json.loads(dataapi)['video'] # dict
    jowner = json.loads(dataapi)['owner'] # dict

    mylist['title'] = jvideo['title']
    mylist['thumbnailURL'] = jvideo['thumbnailURL']
    mylist['largeThumbnailURL'] = jvideo['largeThumbnailURL']
    mylist['postedDateTime'] = jvideo['postedDateTime']
    mylist['owner'] = jowner['nickname'].replace(' \u3055\u3093', '')
    mylist['ownerid'] = jowner['id']
    mylist['ownericon'] = jowner['iconURL']
    
    return mylist

# parse
outputdict = {}
with open('../json/songdb.json') as json_file:
    outputdict = json.load(json_file)

errortag = 0
with open('../json/songlist.json') as json_file:
    data = json.load(json_file)
    for s in data: # dict
        print("\033[36;1m"+s+"\033[0m")
        for item in list(data[s]):
            sm = item['id']
            if sm in outputdict: continue
            print(sm)
            getlist = getvideo(sm)
            if "err" in getlist:
                if getlist["err"]==1:
                    print("\033[31;1mdeleted\033[0m")
                    continue
                if getlist["err"]==2:
                    print("\033[31;1mfailed\033[0m")
                    errortag = 1
                    break
            outputdict[sm] = getlist
        if errortag > 0: break
        # print(outputdict)

with open('../json/songdb.json', 'w') as outfile:
    json.dump(outputdict, outfile, indent=2)

exit(errortag)
