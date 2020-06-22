import json
from requests_html import HTMLSession
import re
import urllib.request
import sys

print('''\033[33;1m
########################################
#       Get nico video details         #
########################################
\033[0m''')

ssmm = 'sm37023967'
if len(sys.argv) > 1: ssmm = str(sys.argv)[1]
retries = 30

def getvideo(sm):
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
    tmp = json.loads(dataapi)
    if "video" in json.loads(dataapi):
        jvideo = json.loads(dataapi)['video'] # dict
        if jvideo != None:
            mylist['title'] = jvideo['title']
            mylist['thumbnailURL'] = jvideo['thumbnailURL']
            mylist['largeThumbnailURL'] = jvideo['largeThumbnailURL']
            mylist['postedDateTime'] = jvideo['postedDateTime']
    if "owner" in json.loads(dataapi):
        jowner = json.loads(dataapi)['owner'] # dict
        if jowner != None:
            mylist['owner'] = jowner['nickname'].replace(' \u3055\u3093', '')
            mylist['ownerid'] = jowner['id']
            mylist['ownericon'] = jowner['iconURL']
    return mylist

# parse
print("\033[32;7m"+ssmm+"\033[0m")
sm = ssmm
getlist = getvideo(sm)
retry = 0
while retry < retries:
    if "err" in getlist:
        retry += 1
        songretry += 1
        if retry>=retries: print("\033[31;1m>> Retry "+str(retry)+"\033[0m\r", end='', flush=True)
        else: print("\033[31m>> Retry "+str(retry)+"\033[0m\r", end='', flush=True)
    else:
        if retry > 0: print('')
        print('\033[2mTitle: \033[0m'+getlist['title'])
        print('\033[2mthumbnailURL: \033[0m'+getlist['thumbnailURL'])
        print('\033[2mlargeThumbnailURL: \033[0m'+getlist['largeThumbnailURL'])
        print('\033[2mpostedDateTime: \033[0m'+getlist['postedDateTime'])
        print('\033[2mowner: \033[0m'+getlist['owner'])
        print('\033[2mownericon: \033[0m'+getlist['ownericon'])
        break

print('')
