import re
import json

prep = """
<!DOCTYPE html>
<html>

<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="keywords" content="vocaran,vocaloid,songrium,xjjgww,週刊VOCALOIDとUTAUランキング">
<meta name="description" content="The Weekly VOCALOID and UTAU Ranking (週刊VOCALOIDとUTAUランキング), abbreviated to Vocaran (ぼからん), is a record chart tabulating the weekly popularity of Vocaloid and Utau songs in Niconico (ニコニコ).">
<meta name="author" content="Erica Wang">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<link rel="icon" href="https://xjjgww.github.io/vocaranlist/img/icon.png" type="image/x-icon">
<link rel="stylesheet" href="css/styles_m.css">
<script data-main="js/scripts.js" src="js/episodelist.js"></script>
<script data-main="js/scripts.js" src="js/songlist.js"></script>
<script data-main="js/loadtoc.js" src="js/episodelist.js"></script>
<script src="js/scripts.js"></script>
<script src="js/loadtoc.js"></script>
</head>
<title>週刊VOCALOIDとUTAUランキング</title>

<body>
<div id="header">
<div id="title">
<div id="titletext">
週刊VOCALOIDとUTAUランキング
</div>
</div>
<div id="filter">
<div id="filtergroup">
<input type="text" id="filterinput" onkeyup="myfilter()" placeholder="Search... #/sm/date">
<button id="appyear" class="yrmo" onclick="appinput('年')">年</button>
<button id="appmonth" class="yrmo" onclick="appinput('月')">月</button>
</div>
</div>
</div>

<div id="body">
<div id="ranlist">
<table id="songlist">
<tr class="songitemtitle" id="tr-1"><th id="td-1"><a class="songtexttitle" id="tda-1">Song&nbsp;list&nbsp;&#187;</a></th></tr>
<tr class="songitemtitle" id="trdull"><th id="tddull"><a class="songtexttitle" id="tdadull">&nbsp;</a></th></tr>
</table>
</div>
<div id="toc">
"""
print(prep)

# with open('json/episodelist.json') as json_file:
#     data = json.load(json_file)
#     oe = 0
#     for s in data:
#         thislist = list(data[s])
#         sm = s
#         mylink = 'https://www.nicovideo.jp/watch/' + sm
#         songrium = 'http://songrium.jp/map/#!/playlist?type=feed&feed_uri=nicodb.jp%252Frss%252F' + sm
#         episode = thislist[0]
#         number = thislist[1]
#         datetxt = thislist[2]
        
#         lineid = '#'+episode+' '+sm+' '+datetxt;
#         attrs = 'type="line" id="'+lineid+'" onclick="darkendate(\''+sm+'\')"'
#         webn = '';
#         if oe%2==0: print('<div class="btn-group gray-background" '+attrs+'>')
#         else: print('<div class="btn-group white-background" '+attrs+'>')
#         print('<button id="n'+sm+'" class="btn txttoblock-nico textaligncenter" onclick="window.open(\''+mylink +'\', \'_blank\');" '+webn+'>'+number+'</button>')
#         print('<button id="d'+sm+'" class="fadetxt textalignleft">'+datetxt+'</button>')
#         print('</div>')
#         oe = oe + 1

board = """
</div>
<script>loadtoc()</script>
</div>
<div id="container">
<div id="clipboard">
<div id="clipboardtxt">Copyright © 2020 boundin</div>
</div>
</div>
</body>
</html>
"""
print(board)
