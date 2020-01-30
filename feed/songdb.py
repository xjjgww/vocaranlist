import json
from requests_html import HTMLSession
import re

def getvideo(sm):
    mylist = {}
    session = HTMLSession()
    r = session.get('https://www.nicovideo.jp/watch/'+sm) # HTMLResponse
    # print(r.__dict__.keys())
    # print(r.headers)
    ele = r.html.find('#js-initial-watch-data') # list
    if len(ele) == 0:
        mylist['err'] = 1
        return mylist
    dataapi = ele[0].attrs['data-api-data'] # str
    dataapi = re.sub(r"\"description\".+?\"thumbnailURL\"", "\"thumbnailURL\"", dataapi)
    # print(dataapi)
    mylist = {
        "title": "",
        "thumbnailURL": "",
        "largeThumbnailURL": "",
        "postedDateTime": "",
        "owner": "",
        "ownerid": "",
        "ownericon": ""
        }
    if "video" in json.loads(dataapi):
        jvideo = json.loads(dataapi)['video'] # dict
        mylist['title'] = jvideo['title']
        mylist['thumbnailURL'] = jvideo['thumbnailURL']
        mylist['largeThumbnailURL'] = jvideo['largeThumbnailURL']
        mylist['postedDateTime'] = jvideo['postedDateTime']
    if "owner" in json.loads(dataapi):
        jowner = json.loads(dataapi)['owner'] # dict
        mylist['owner'] = jowner['nickname'].replace(' \u3055\u3093', '')
        mylist['ownerid'] = jowner['id']
        mylist['ownericon'] = jowner['iconURL']
    
    return mylist

# parse
outputdict = {}
with open('../json/songdb.json') as json_file:
    outputdict = json.load(json_file)

deadsm = {}
with open('deadlist.json') as json_file:
    deadsm = json.load(json_file)
    
with open('../json/songlist.json') as json_file:
    data = json.load(json_file)
    count = 0
    for s in data: # dict
        print("\033[36;1m"+s+"\033[0m")
        for item in list(data[s]):
            sm = item['id']
            if sm in outputdict: continue
            if sm in deadsm: continue
            print(sm)
            retry = 0
            while retry < 30:
                getlist = getvideo(sm)
                if "err" in getlist:
                    retry += 1
                    print("\033[31mretry "+str(retry)+"\033[0m\r")
                else:
                    outputdict[sm] = getlist
                    break
            if retry==30: deadsm[sm] = 1
            count += 1 # count
            with open('../json/songdb.json', 'w') as outfile:
                json.dump(outputdict, outfile, indent=2)
        with open('deadlist.json', 'w') as outfile:
            json.dump(deadsm, outfile, indent=2)
        # if count > 1000: break # count
         


