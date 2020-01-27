
function loadtoc()
{
    var thetoc = document.getElementById('toc');
    for(var sm in episodejsonobj)
    {
        var theitem = episodejsonobj[sm];
        var mylink = 'https://www.nicovideo.jp/watch/' + sm;
        var songrium = 'http://songrium.jp/map/#!/playlist?type=feed&feed_uri=nicodb.jp%252Frss%252F' + sm;
        var episode = theitem[0];
        var number = theitem[1];
        var datetxt = theitem[2];
        var lineid = '#'+episode+' '+sm+' '+datetxt;

        var line = document.createElement("div");
        line.setAttribute('type', 'line');
        line.id = lineid;
        thetoc.appendChild(line);

        var btnn = document.createElement('button');
        btnn.id = 'n'+sm;
        btnn.className = "btn txttoblock-nico textaligncenter";
        btnn.innerHTML = number;
        line.appendChild(btnn);
        btnn.setAttribute("onclick", "window.open('https://www.nicovideo.jp/watch/"+sm+"','_blank')");
        btnn.setAttribute("onmouseover", "statusbar('&#187; NicoNico &#187;')");
        btnn.setAttribute("onmouseout", "statusbar('&nbsp;')");

        var btnvn = document.createElement('button');
        btnvn.className = "btn-invisible whiteblock-nico";
        btnvn.innerHTML = "N";
        line.appendChild(btnvn);
        btnvn.setAttribute("onclick", "copylink('"+sm+"', 'the sm #')");
        btnvn.setAttribute("onmouseover", "statusbar('https://www.nicovideo.jp/watch/"+sm+"')");
        btnvn.setAttribute("onmouseout", "statusbar('&nbsp;')");

        var btnb = document.createElement('button');
        btnb.id = 'b'+sm;
        btnb.className = "btn txttoblock-song textaligncenter";
        btnb.innerHTML = sm;
        line.appendChild(btnb);
        btnb.setAttribute("onclick", "window.open('http://songrium.jp/map/#!/playlist?type=feed&feed_uri=nicodb.jp%252Frss%252F"+sm+"', '_blank')");
        btnb.setAttribute("onmouseover", "statusbar('&#187; songrium &#187;')");
        btnb.setAttribute("onmouseout", "statusbar('&nbsp;')");

        var btnvs = document.createElement('button');
        btnvs.className = "btn-invisible whiteblock-song";
        btnvs.innerHTML = "S";
        line.appendChild(btnvs);
        btnvs.setAttribute("onclick", "copylink('http://songrium.jp/map/#!/playlist?type=feed&feed_uri=nicodb.jp%252Frss%252F"+sm+"', 'the songrium link')");
        btnvs.setAttribute("onmouseover", "statusbar('songrium.jp/map/#!/playlist?type=feed&feed_uri=nicodb.jp//rss//"+sm+"')");
        btnvs.setAttribute("onmouseout", "statusbar('&nbsp;')");

        var btnd = document.createElement('button');
        btnd.id = 'd'+sm;
        btnd.className = "fadetxt textalignleft";
        btnd.innerHTML = datetxt;
        line.appendChild(btnd);
        btnd.setAttribute("onmouseover", "statusbar('Click to get the song list of "+sm+".')");
        btnd.setAttribute("onmouseout", "statusbar('&nbsp;')");

        line.setAttribute("onclick", "darkendate('"+sm+"')");
    }
    altercolor();
}

function loadtoc_m()
{
    var thetoc = document.getElementById('toc');
    for(var sm in episodejsonobj)
    {
        var theitem = episodejsonobj[sm];
        var mylink = 'https://www.nicovideo.jp/watch/' + sm;
        var songrium = 'http://songrium.jp/map/#!/playlist?type=feed&feed_uri=nicodb.jp%252Frss%252F' + sm;
        var episode = theitem[0];
        var number = theitem[1];
        var datetxt = theitem[2];
        var lineid = '#'+episode+' '+sm+' '+datetxt;

        var line = document.createElement("div");
        line.setAttribute('type', 'line');
        line.id = lineid;
        thetoc.appendChild(line);

        var btnn = document.createElement('button');
        btnn.id = 'n'+sm;
        btnn.className = "btn txttoblock-nico textaligncenter";
        btnn.innerHTML = number;
        line.appendChild(btnn);
        btnn.setAttribute("onclick", "window.open('https://www.nicovideo.jp/watch/"+sm+"')");

        var btnd = document.createElement('button');
        btnd.id = 'd'+sm;
        btnd.className = "fadetxt textalignleft";
        btnd.innerHTML = datetxt;
        line.appendChild(btnd);

        line.setAttribute("onclick", "darkendate('"+sm+"')");
    }
    altercolor();
}
