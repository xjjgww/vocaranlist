import re
import json

prep = """
<!DOCTYPE html>
<html>

<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="keywords" content="vocaran,vocaloid,songrium,xjjgww,週刊VOCALOIDとUTAUランキング">
<meta name="author" content="Erica Wang">
<link rel="icon" href="https://github.com/xjjgww/vocaranlist/blob/master/img/icon.png" type = "image/x-icon">
<link rel="stylesheet" href="css/styles.css">
<script data-main="js/scripts.js" src="js/episodelist.js"></script>
<script data-main="js/scripts.js" src="js/songlist.js"></script>
<script src="js/scripts.js"></script>
</head>
<title>週刊VOCALOIDとUTAUランキング</title>

<body>
<div id="body">
<div id="ranlist">
<div id="descholder">
<div id="desc">
<p id="descrip"><a class="boldp">The Weekly VOCALOID and UTAU Ranking</a> (<a class="linkp" href="https://dic.nicovideo.jp/a/%E9%80%B1%E5%88%8Avocaloid%E3%81%A8utau%E3%83%A9%E3%83%B3%E3%82%AD%E3%83%B3%E3%82%B0" target="_blank">週刊VOCALOIDとUTAUランキング</\
a>), abbreviated to <a class="boldp">Vocaran</a> (ぼからん),
is a record chart tabulating the weekly popularity of Vocaloid and Utau songs in <a class="linkp" href="https://www.nicovideo.jp/" target="_blank">Niconico</a> (ニコニコ).
This website is based on <a class="linkp" href="http://nicodb.jp/v/" target="_blank">nicodb.jp</a>. Apologize for any possible mistake.</p>
</div>
</div>
<table id="songlist">
<tr class="songitemtitle" id="tr-1"><th id="td-1"><a class="songtexttitle" id="tda-1">&nbsp;</a></th></tr>
<tr class="songitemtitle" id="trdull"><th id="tddull"><a class="songtexttitle" id="tdadull">&nbsp;</a></th></tr>
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
print(prep)

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
