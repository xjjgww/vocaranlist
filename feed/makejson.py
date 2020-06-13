from requests_html import HTMLSession
import re
from lxml import etree
import json

session = HTMLSession()

print('\033[33;1m\
########################################\n\
#    makejson.py > episodelist.json    #\n\
########################################\n\
\033[0m')

urllist = ['https://www.nicovideo.jp/tag/VOCAL_Character%E3%83%A9%E3%83%B3%E3%82%AD%E3%83%B3%E3%82%B0?sort=f&order=d']
# for i in range(1,13):
#     urllist.append('https://www.nicovideo.jp/tag/週刊VOCALOIDとUTAUランキング?sort=f&order=d&page='+str(i))

mylist = {}
with open('../json/episodelist.json') as json_file:
    mylist = json.load(json_file)

for url in urllist:
    print(url)
    r = session.get(url)
    # seltit = 'body > div.BaseLayout > div.container.columns.column700-300 > div > div.column.main > div.contentBody.video.uad.videoList.videoList01 > ul:nth-child(2) > li > div.itemContent > p > a'
    # seldes = 'body > div.BaseLayout > div.container.columns.column700-300 > div > div.column.main > div.contentBody.video.uad.videoList.videoList01 > ul:nth-child(2) > li > div.itemContent > div.wrap > p.itemDescription'
    sel = 'body > div.BaseLayout > div.container.columns.column700-300 > div > div.column.main > div.contentBody.video.uad.videoList.videoList01 > ul:nth-child(2) > li > div.itemContent'

    vresults = r.html.find(sel)

    for vresult in vresults:
        if len(vresult.find('a')) <= 0 or len(vresult.find('p.itemDescription')) <= 0: continue

        vtit = list(vresult.find('a'))[0]
        vdes = list(vresult.find('p.itemDescription'))[0]
        if len(vtit.absolute_links) <= 0: continue

        mytext = vtit.text
        if '週刊VOCALOIDとUTAUランキング　#' not in mytext and '週刊VOCAL CharacterとUTAUランキング　#' not in mytext: continue

        number = re.search(r'#(\d)(\d)(\d)[^\s]+', mytext)
        episode = number.group(1)+number.group(2)+number.group(3)

        mylink = list(vtit.absolute_links)[0]
        sm = re.search(r'sm(\d+)', mylink).group(0)
        if sm in mylist: continue
        songrium = 'http://songrium.jp/map/#!/playlist?type=feed&feed_uri=nicodb.jp%252Frss%252F'+sm

        mydescription = vdes.text
        date = re.search(r'：([^～]+～[^\s]+)', mydescription)
        datetxt = ''
        if date: datetxt = date.group(1)

        thisitem = [episode, number.group(), datetxt]
        mylist[sm] = thisitem
        print(episode)

sorted_mylist = {}
for sm in sorted(mylist, reverse=True):
    sorted_mylist[sm] = mylist[sm]

# print(json.dumps(mylist, indent=2))

with open('../json/episodelist.json', 'w') as outfile:
    json.dump(sorted_mylist, outfile, indent=2)

