import re
import json

prep1 = """
<!DOCTYPE html>
<html>

<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="keywords" content="vocaran,vocaloid,songrium,xjjgww">
<meta name="author" content="Erica Wang">
<link rel="stylesheet" href="css/styles.css">
<script data-main="js/scripts.js" src="js/songlist.js"></script>
<script src="js/scripts.js"></script>
</head>
<title>週刊VOCALOIDとUTAUランキング</title>

<body>
<div id="body">
<div id="ranlist">
<table id="songlist">
"""
print(prep1)

for i in range(0, 42):
    print('<tr class="songitem" id="tr'+str(i)+'"><td class="songunit" id="td'+str(i)+'"><a class="songtext" id="tda'+str(i)+'" href="#">&nbsp;</a></td></tr>')

prep2  = """
</table>
<div id="songlistfooter">
<p id="songlisttxt">Copyright © 2020 boundin</p>
</div>
</div>
<div id="toc">
<div id="header">

<h1 id="title">週刊VOCALOIDとUTAUランキング</h1>
<input type="text" id="filterinput" onkeyup="myfilter()" placeholder="Search... #/sm/date">
<button id="appyear" class="yrmo" onclick="appinput('年')" onmouseover="darkendate('appyear')" onmouseout="fadedate('appyear')">年</button>
<button id="appmonth" class="yrmo" onclick="appinput('月')" onmouseover="darkendate('appmonth')" onmouseout="fadedate('appmonth')">月</button>
</div>
"""
print(prep2)

with open('json/episodelist.json') as json_file:
    data = json.load(json_file)
    oe = 0
    for s in data:
        thislist = list(data[s])
        sm = s
        mylink = 'https://www.nicovideo.jp/watch/' + sm
        songrium = 'http://songrium.jp/map/#!/playlist?type=feed&feed_uri=nicodb.jp%252Frss%252F' + sm
        episode = thislist[0]
        number = thislist[1]
        datetxt = thislist[2]
        
        lineid = '#'+episode+' '+sm+' '+datetxt;
        attrs = 'type="line" id="'+lineid+'" onmouseover="darkendate(\''+sm+'\')" onmouseout="fadedate(\''+sm+'\')"'
        urlanin = 'onmouseover="statusbar(\''+mylink+'\')" onmouseout="statusbar(\'&nbsp;\')"';
        urlanis = 'onmouseover="statusbar(\''+songrium+'\')" onmouseout="statusbar(\'&nbsp;\')"';
        webn = 'onmouseover="statusbar(\'&#187; NicoNico &#187;\')" onmouseout="statusbar(\'&nbsp;\')"';
        webs = 'onmouseover="statusbar(\'&#187; songrium &#187;\')" onmouseout="statusbar(\'&nbsp;\')"';
        if oe%2==0: print('<div class="btn-group gray-background" '+attrs+'>')
        else: print('<div class="btn-group white-background" '+attrs+'>')
        print('<button id="n'+sm+'" class="btn txttoblock-nico textaligncenter" onclick="window.open(\''+mylink +'\', \'_blank\');" '+webn+'>'+number+'</button>')
        print('<button class="btn-invisible whiteblock-nico" onclick="copylink(\''+sm+'\', \'the sm #\')" '+urlanin+'>N</button>')
        print('<button id="b'+sm+'" class="btn txttoblock-song textaligncenter" onclick="window.open(\''+songrium +'\', \'_blank\');" '+webs+'>'+sm+'</button>')
        print('<button class="btn-invisible whiteblock-song" onclick="copylink(\''+songrium+'\', \'the songrium link\')" '+urlanis+'>S</button>')
        print('<button id="d'+sm+'" class="fadetxt textalignleft">'+datetxt+'</button>')
        print('</div>')
        oe = oe + 1

board = """
<div id="footer">
</div>
<div id="container">
<div id="clipboard">
<p id="clipboardtxt">&nbsp;</p>
</div>
</div>
</div>
</div>
</body>
</html>
"""
print(board)
