
var nicopl = ['3165526', '3271200', '3409323', '2951756', '3900779']; // playlist of latest 5 episode

function loadtoc()
{
    var thetoc = document.getElementById('toc');
    var count = 0;
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
        btnn.className = "btn left linkp";
        btnn.innerHTML = number;
        line.appendChild(btnn);
        btnn.setAttribute("onclick", "window.open('https://www.nicovideo.jp/watch/"+sm+"','_blank')");
        btnn.setAttribute("onmouseover", "statusbar('https://www.nicovideo.jp/watch/"+sm+"')");
        btnn.setAttribute("onmouseout", "statusbar('&nbsp;')");

        var btnvn = document.createElement('button');
        btnvn.className = "btn left hovercolor hideinmobile";
        btnvn.innerHTML = '<i class="fa-regular fa-copy"></i>';
        line.appendChild(btnvn);
        btnvn.setAttribute("onclick", "copylink('"+sm+"', 'the sm #')");
        btnvn.setAttribute("onmouseover", "statusbar('https://www.nicovideo.jp/watch/"+sm+"')");
        btnvn.setAttribute("onmouseout", "statusbar('&nbsp;')");

        var btnb = document.createElement('button');
        btnb.id = 'b'+sm;
        btnb.className = "btn left linkp hideinmobile";
        btnb.innerHTML = sm;
        line.appendChild(btnb);
        btnb.setAttribute("onclick", "window.open('http://songrium.jp/map/#!/playlist?type=feed&feed_uri=nicodb.jp%252Frss%252F"+sm+"', '_blank')");
        btnb.setAttribute("onmouseover", "statusbar('songrium.jp/map/#!/playlist?type=feed&feed_uri=nicodb.jp//rss//"+sm+"')");
        btnb.setAttribute("onmouseout", "statusbar('&nbsp;')");

        var btnvs = document.createElement('button');
        btnvs.className = "btn left hovercolor hideinmobile";
        btnvs.innerHTML = '<i class="fa-regular fa-copy"></i>';
        line.appendChild(btnvs);
        btnvs.setAttribute("onclick", "copylink('http://songrium.jp/map/#!/playlist?type=feed&feed_uri=nicodb.jp%252Frss%252F"+sm+"', 'the songrium link')");
        btnvs.setAttribute("onmouseover", "statusbar('songrium.jp/map/#!/playlist?type=feed&feed_uri=nicodb.jp//rss//"+sm+"')");
        btnvs.setAttribute("onmouseout", "statusbar('&nbsp;')");

        var btnd = document.createElement('button');
        btnd.id = 'd'+sm;
        btnd.className = "btn left";
        btnd.innerHTML = datetxt;
        line.appendChild(btnd);

        var btnpl = document.createElement('button');
        btnpl.className = "btn right linkp";
        btnpl.innerHTML = "PL";
        line.appendChild(btnpl);
        btnpl.setAttribute("onclick", "window.open('https://www.nicovideo.jp/mylist/"+nicopl[episode%5]+"', '_blank')");
        btnpl.setAttribute("onmouseover", "statusbar('&#187; Playlist &#187;.')");
        btnpl.setAttribute("onmouseout", "statusbar('&nbsp;')");
        if(count >= 5) { btnpl.style.display = "none"; }

        line.setAttribute("onclick", "darkendate('"+sm+"'); document.getElementById('rightpanel').style.display = 'block';");
        if(count==0) darkendate(sm);
        count = count+1;
    }
    altercolor();
}
