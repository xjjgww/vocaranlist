from requests_html import HTMLSession
import re
from lxml import etree

session = HTMLSession()

preparation = """
<!DOCTYPE html>
<html>

<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="keywords" content="vocaran,vocaloid,songrium,xjjgww">
<meta name="author" content="Erica Wang">
<link rel="stylesheet" href="css/styles.css">
</head>

<body>
<title>週刊VOCALOIDとUTAUランキング</title>

<div id="body">
"""
header = """
<div id="header">
<h1 id="title">週刊VOCALOIDとUTAUランキング</h1>
<input type="text" id="filterinput" onkeyup="myfilter()" placeholder="Search... #/sm/date">
<script src="js/scripts.js"></script>
</div>
"""
print(preparation)
print(header)

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
        number = re.search(r'#(\d)(\d)(\d)[^\s]+', mytext)
        episode = number.group(1)+number.group(2)+number.group(3)

        mylink = list(vtit.absolute_links)[0]
        sm = re.search(r'sm(\d+)', mylink).group(0)
        songrium = 'http://songrium.jp/map/#!/playlist?type=feed&feed_uri=nicodb.jp%252Frss%252F'+sm

        mydescription = vdes.text
        date = re.search(r'VOCALOID：([^～]+～[^\s]+)', mydescription)
        datetxt = ''
        if date: datetxt = date.group(1)
        
        lineid = '#'+episode+sm+' '+datetxt;
        attrs = 'type="line" id="'+lineid+'" onmouseover="darkendate(\'d'+sm+'\')" onmouseout="fadedate(\'d'+sm+'\')"'
        urlanin = 'onmouseover="statusbar(\''+mylink+'\')" onmouseout="statusbar(\'&nbsp;\')"';
        urlanis = 'onmouseover="statusbar(\''+songrium+'\')" onmouseout="statusbar(\'&nbsp;\')"';
        webn = 'onmouseover="statusbar(\'&#187; NicoNico &#187;\')" onmouseout="statusbar(\'&nbsp;\')"';
        webs = 'onmouseover="statusbar(\'&#187; songrium &#187;\')" onmouseout="statusbar(\'&nbsp;\')"';
        if oe%2==0: print('<div class="btn-group gray-background" '+attrs+'>')
        else: print('<div class="btn-group white-background" '+attrs+'>')
        print('<button id="n'+sm+'" class="btn txttoblock-nico textaligncenter" onclick="window.open(\''+mylink +'\', \'_blank\');" '+webn+'>'+number.group()+'</button>')
        print('<button class="btn-invisible whiteblock-nico" onclick="copylink(\''+sm+'\', \'the sm #\')" '+urlanin+'>N</button>')
        print('<button id="b'+sm+'" class="btn txttoblock-song textaligncenter" onclick="window.open(\''+songrium +'\', \'_blank\');" '+webs+'>'+sm+'</button>')
        print('<button class="btn-invisible whiteblock-song" onclick="copylink(\''+songrium+'\', \'the songrium link\')" '+urlanis+'>S</button>')
        print('<button id="d'+sm+'" class="fadetxt textalignleft">'+datetxt+'</button>')
        # print('<button class="btn-invisible whiteblock-song" onclick="copylink(\''+datetxt+'\')" '+urlanis+'>D</button>')
        print('</div>')
        lastr = mytext
        oe = oe + 1

print('</div>')

board = """
<div id="footer">
</div>
<div id="container">
<div id="clipboard">
<p id="clipboardtxt">&nbsp;</p>
</div>
</div>
"""
print(board)
print('</body>')
print('</html>')


