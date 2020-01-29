import re
import json
import requests
from bs4 import BeautifulSoup

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
with open('../json/episodelist.json') as json_file:
    data = json.load(json_file)
    for s in data:
        print(list(data[s])[0])
        sm = s
        # outputdict[sm] = findsonglist('http://nicodb.jp/u/bgm/utaran/'+sm+'/?rss=1')
        outputdict[sm] = findsonglist('http://nicodb.jp/u/index.php/bgm/rankrss/'+sm)

with open('../json/songlist.json', 'w') as outfile:
    json.dump(outputdict, outfile, indent=2)
