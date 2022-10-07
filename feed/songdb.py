import json
from requests_html import HTMLSession
import re
import urllib.request
from bs4 import BeautifulSoup 

print('\033[33;1m\
########################################\n\
#       songdb.py > songdb.json        #\n\
########################################\n\
\033[0m')

def getvideo(sm):
    # print(sm)
    mylist = {}
    session = HTMLSession()
    r = session.get('https://www.nicovideo.jp/watch/'+sm) # HTMLResponse
    # print(r.html)
    # print(r.__dict__.keys())
    # print(r.headers)
    ele = r.html.find('#js-initial-watch-data') # list
    if len(ele) == 0:
        mylist['err'] = 1
        return mylist
    dataapi = ele[0].attrs['data-api-data'] # str
    # print(dataapi)
    # print("1 -------------------------------------")
    dataapi = re.sub(r"^.+?\"owner\":{\"", "{\"owner\":{\"", dataapi)
    dataapi = re.sub(r"^.+?\"owner\":null", "{\"owner\":null", dataapi)
    # print(dataapi)
    # print("2 -------------------------------------")
    dataapi = re.sub(r"\"viewer\":null}.+?\"video\":{\"id\":", "\"viewer\":null},\"video\":{\"id\":", dataapi)
    # print(dataapi)
    # print("3 -------------------------------------")
    dataapi= re.sub(r"\"description\":.+?\"count\":{", "\"count\":{", dataapi)
    # print(dataapi)

    try:
        json.loads(dataapi)
    except ValueError as e:
        return mylist

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
        # print(jvideo)
        if jvideo != None:
            mylist['title'] = jvideo['title']
            if "thumbnailURL" in jvideo:
                mylist['thumbnailURL'] = jvideo['thumbnailURL']
            else:
                mylist['thumbnailURL'] = jvideo['thumbnail']['url']
            if "largeThumbnailURL" in jvideo:
                mylist['largeThumbnailURL'] = jvideo['largeThumbnailURL']
            else:
                # mylist['largeThumbnailURL'] = jvideo['thumbnail']['largeUrl']
                mylist['largeThumbnailURL'] = jvideo['thumbnail']['middleUrl']
            if "postedDateTime" in jvideo:
                mylist['postedDateTime'] = jvideo['postedDateTime']
            else:
                mylist['postedDateTime'] = jvideo['registeredAt']
    if "owner" in json.loads(dataapi):
        jowner = json.loads(dataapi)['owner'] # dict
        # print(jowner)
        if jowner != None:
            mylist['owner'] = jowner['nickname'].replace(' \u3055\u3093', '')
            mylist['ownerid'] = jowner['id']
            if "iconURL" in jowner:
                mylist['ownericon'] = jowner['iconURL']
            elif "iconUrl" in jowner:
                mylist['ownericon'] = jowner['iconUrl']
    return mylist

# parse
outputdict = {}
with open('../json/songdb.json') as json_file:
    outputdict = json.load(json_file)

deadsm = {}
with open('deadlist.json') as json_file:
    deadsm = json.load(json_file)

episode = {}
with open('../json/episodelist.json') as json_file:
    episode = json.load(json_file)
    
retries = 40
with open('../json/songlist.json') as json_file:
    data = json.load(json_file)

for s in data: # dict
    print("\033[32;7m"+episode[s][1]+"\033[0m\r", end='', flush=True)
    count = 0
    songretry = 0
    for item in list(data[s]):
        sm = item['id']
        if sm in outputdict: continue
        # if sm in deadsm and sm < 'sm33659242': continue
        if sm in deadsm: continue
        retry = 0
        while retry < retries:
            getlist = getvideo(sm)
            if "err" in getlist:
                retry += 1
                songretry += 1
                if retry>=retries: print("\033[31;1m>> Retry "+str(retry)+"\033[0m\r", end='', flush=True)
                else: print("\033[31m>> Retry "+str(retry)+"\033[0m\r", end='', flush=True)
            elif getlist == {}:
                print("\033[31m>> Bad json: "+sm+"\033[0m")
                break
            else:
                outputdict[sm] = getlist
                if sm in deadsm: del deadsm[sm]
                if retry > 0 or count==0: print('')
                print(getlist['title'])
                break
        if retry==retries: deadsm[sm] = 1
        count += 1 # count
    
sorted_outputdict = {}
for s in sorted(outputdict):
    sorted_outputdict[s] = outputdict[s]
        
with open('../json/songdb.json', 'w') as outfile:
    json.dump(sorted_outputdict, outfile, indent=2)
with open('deadlist.json', 'w') as outfile:
    json.dump(deadsm, outfile, indent=2)

         


