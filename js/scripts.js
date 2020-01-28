
function myFunction() {
    document.getElementById("title").innerHTML = "Welcome!";
}

function altercolor() {
    var lines = document.getElementsByTagName('div');
    var filteri = 0;
    for(var i=0; i<lines.length; i++)
    {
        if(lines[i].getAttribute('type') != "line") continue;
        if(lines[i].style.display == "none") continue;
        if(filteri%2==0) { lines[i].className = "btn-group gray-background"; }
        else { lines[i].className = "btn-group white-background"; }
        filteri++;
    }    
}

function myfilter() {
    var input, i, lines, idd;
    input = document.getElementById('filterinput').value;
    lines = document.getElementsByTagName('div');
    for(i=0; i<lines.length; i++)
    {
        if(lines[i].getAttribute('type') != "line") continue;
        idd = lines[i].id;
        var sm = idd.match(/sm\d+/g);
        var findmatch = '';
        for(var jitem in songjsonobj[sm]) { findmatch += (' '+songjsonobj[sm][jitem]["alt"]); }
        if(idd.indexOf(input) > -1 || findmatch.indexOf(input) > -1) { lines[i].style.display = ""; }
        else { lines[i].style.display = "none"; }
    }
    altercolor();
}

function copylink(str, noti) {
    const el = document.createElement('textarea');
    el.value = str;
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);
    document.getElementById('clipboard').innerHTML = "Copied "+noti+".";
}

function darkendate(sm) {
    // document.getElementById('iconholder').style.display = "none";
    var thetab = document.getElementById('songlist');
    for(var i=0; i<100; i++)
    {
        var eletr = document.getElementById('tr'+i);
        if(eletr !== null) { eletr.remove(); }
    }
    var input = document.getElementById('filterinput').value;
    document.getElementById('tr-1').innerHTML = episodejsonobj[sm][1]+' '+episodejsonobj[sm][2];
    for(var i=0; i<songjsonobj[sm].length; i++)
    {
        var newtr = document.createElement("tr");
        newtr.id = 'tr'+i;
        newtr.className = "songitem";
        thetab.appendChild(newtr);
        var newtd = document.createElement("td");
        newtd.id = 'td'+i;
        newtr.appendChild(newtd);
        var newtda = document.createElement("a");
        newtda.id = 'tda'+i;
        newtda.className = "songtext";
        newtda.innerHTML = songjsonobj[sm][i]['title'];
        newtda.href = songjsonobj[sm][i]['url'];
        newtda.setAttribute('target', '_blank');
        newtd.appendChild(newtda);

        if(songjsonobj[sm][i]['title'].indexOf(input) > -1 && input != '') { newtda.style.color = "white"; newtda.style.backgroundColor = "#CC6666"; }
    }
}
function fadedate(sm) {
    document.getElementById('d'+sm).style.opacity = "0.8";
}

function statusbar(str) {
    document.getElementById('clipboard').innerHTML = str;
}

function appinput(str) {
    document.getElementById('filterinput').value += str;
    myfilter();
}


