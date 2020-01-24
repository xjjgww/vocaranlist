
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

        var btnd = document.createElement('button');
        btnd.id = 'd'+sm;
        btnd.className = "fadetxt textalignleft";
        btnd.innerHTML = datetxt;
        line.appendChild(btnd);

        var nicolink = 'https://www.nicovideo.jp/watch/'+sm.valueOf();
        document.getElementById('n'+sm).onclick = function() { window.open(nicolink.valueOf(), '_blank'); }
        // if(episode=="604") { document.getElementById('title').innerHTML = document.getElementById('n'+sm).onclick; }
        if(episode=="604") { document.getElementById('title').innerHTML = nicolink; }
        // document.getElementById(lineid).onclick = function() { darkendate(sm); } 
    }
    altercolor();
}
