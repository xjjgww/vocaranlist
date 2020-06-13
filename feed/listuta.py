import re
import json
import requests
from bs4 import BeautifulSoup

print('\033[33;1m\
########################################\n\
#      listuta.py > songlist.json      #\n\
########################################\n\
\033[0m')

def findsonglist(url):
    readweb = requests.get(url).text
    readweb = readweb.replace('<![CDATA[', '')
    readweb = readweb.replace(']]>', '</img>')
    readweb = readweb.replace('link', 'url')
    # print(readweb)
    soup = BeautifulSoup(readweb, "html.parser")
    # print(soup.prettify())
    allitems = soup.find_all('item')

    mylist = []
    for ii in allitems:
        tt = ii.find('title').text
        ll = ii.find('url').text
        aa = ii.find('description').find('img')['alt']
        ss = ll.replace('http://www.nicovideo.jp/watch/', '')
        thisitem = {}
        thisitem['title'] = tt
        thisitem['id'] = ss
        thisitem['alt'] = aa
        mylist.append(thisitem)
    return mylist

# parse

outputdict = {}
with open('../json/songlist.json') as json_file:
    outputdict = json.load(json_file)

with open('../json/episodelist.json') as json_file:
    data = json.load(json_file)
    for s in data:
        sm = s
        if sm in outputdict: continue
        print(list(data[s])[0])
        # outputdict[sm] = findsonglist('http://nicodb.jp/u/bgm/utaran/'+sm+'/?rss=1')
        outputdict[sm] = findsonglist('http://nicodb.jp/u/index.php/bgm/rankrss/'+sm)

sorted_outputdict = {}
for epi in sorted(outputdict):
    sorted_outputdict[epi] = outputdict[epi]
        
with open('../json/songlist.json', 'w') as outfile:
    json.dump(sorted_outputdict, outfile, indent=2)
