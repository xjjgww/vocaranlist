from requests_html import HTMLSession
import re
from lxml import etree

session = HTMLSession()

header = """
<!DOCTYPE NETSCAPE-Bookmark-file-1>
<html>

<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
 .title {
 border: none;
 background-color: inherit;
 font-family:courier,Osaka;
  text-align: center;
color: #484848
 }
 .h {
 font-size: 40px;
 }
 .hh {
 font-size: 16px;
 }

.btn-group {
height: 36px;
width: 700px;
margin-left: auto;
  margin-right: auto;
}
.btn-group:hover {background-color: #f0f0f0;}
.white-background {background-color: #white;}
.gray-background {background-color: #fafafa;}

 .btn {
 border: none;
 outline:none;
 background-color: inherit;
 padding: 9px 19px;
 font-size: 16px;
 font-family:courier;
 cursor: pointer;
 float: left;
 display: block;
 opacity: 0.6;
 }
 .btn:hover {color: white; opacity: 1.0;}

 .mydarkblue {color: #0C457D;}
 .mydarkblue:hover {background-color: #0C457D;}
 .myorange {color: #DE9C9C;}
 .myorange:hover {background-color: #DE9C9C;}

 .btn-copy {
 border: none;
 outline:none;
 padding: 9px 10px;
 font-size: 16px;
 font-family:courier;
 float: left;
 cursor: pointer;
 display: inline-block;
 align:center;
 background-color: white;
 opacity: 0.0;
 border-radius: 5px;
position: relative;
 }
 .mydarkblue-b {color: #0C457D;}
 .myorange-b {color: #DE9C9C;}
 .btn-copy:hover {opacity: 0.8;}

 .fadetxt {
 border: 2px;
 background-color: inherit;
 padding: 5px 20px;
 font-size: 16px;
 font-family:courier;
 opacity: 0.6;
 display: block;
 }
 .fadetxt:hover {opacity: 1.0;}
</style>
</head>
"""
print(header)

print('<body>')
print('<Title>週刊VOCALOIDとUTAUランキング</Title>')
print('<h1 class="title h">週刊VOCALOIDとUTAUランキング (Vocaran)</h1><br>')

for i in range(1,2):
    url = 'https://www.nicovideo.jp/tag/週刊VOCALOIDとUTAUランキング?sort=f&order=d&page='+str(i)
    r = session.get(url)
    # seltit = 'body > div.BaseLayout > div.container.columns.column700-300 > div > div.column.main > div.contentBody.video.uad.videoList.videoList01 > ul:nth-child(2) > li > div.itemContent > p > a'
    # seldes = 'body > div.BaseLayout > div.container.columns.column700-300 > div > div.column.main > div.contentBody.video.uad.videoList.videoList01 > ul:nth-child(2) > li > div.itemContent > div.wrap > p.itemDescription'
    sel = 'body > div.BaseLayout > div.container.columns.column700-300 > div > div.column.main > div.contentBody.video.uad.videoList.videoList01 > ul:nth-child(2) > li > div.itemContent'

    lastr = ''
    oe = 0
    vresults = r.html.find(sel)
    for vresult in vresults:
        if len(vresult.find('a')) <= 0 or len(vresult.find('p.itemDescription')) <= 0: continue

        vtit = list(vresult.find('a'))[0]
        vdes = list(vresult.find('p.itemDescription'))[0]
        if len(vtit.absolute_links) <= 0: continue

        mytext = vtit.text
        if '週刊VOCALOIDとUTAUランキング　#' not in mytext or mytext == lastr: continue
        mytext = mytext.replace("・", "&#171;&#187;")
        number = re.search(r'#(\d)(\d)[^\s]+', mytext)

        mylink = list(vtit.absolute_links)[0]
        sm = re.search(r'sm(\d+)', mylink).group(0)
        songrium = 'http://songrium.jp/map/#!/playlist?type=feed&feed_uri=nicodb.jp%252Frss%252F'+sm

        mydescription = vdes.text
        date = re.search(r'VOCALOID：([^～]+～[^\s]+)', mydescription)
        if date: date = date.group(1)
        else: date = ''
        
        # if "99・" in mytext:
        #     m = number.group(1)
        #     print('------------',m)
        if "9・" in mytext:
            m = number.group(1)+number.group(2)
            print('<h2 class="title hh">#'+m+'0 ～ '+m+'9</h2><br>')

        # print(number.group(), '|', mylink, '|', sm, '|', songrium, '|', date.group(1))
        if oe%2==0: print('<div class="btn-group gray-background">')
        else: print('<div class="btn-group white-background">')
        print('<button class="btn mydarkblue" onclick="window.open(\''+mylink +'\', \'_blank\');">'+number.group()+'</button>')
        print('<button class="btn-copy mydarkblue-b">C</button>')
        print('<button class="btn myorange" onclick="window.open(\''+songrium +'\', \'_blank\');">'+sm+'</button>')
        print('<button class="btn-copy myorange-b">C</button>')
        print('<button class="fadetxt">'+date+'</button>')
        print('</div>')
        lastr = mytext
        oe = oe + 1

##
# sel = 'body > div.BaseLayout > div.container.columns.column700-300 > div > div.column.main > div.contentBody.video.uad.videoList.videoList01 > ul:nth-child(2) > li:nth-child(1) > div.itemContent > p > a'
# mylist.append((mytext, mylink))
# vtits = r.html.find(sel)
# print(r.html.text)
# print(r.html.absolute_links)
# print(vtits[0].absolute_links)
# print(vtits)
# print(get_text_link_from_sel(sel))

print('</body>')
print('</html>')
