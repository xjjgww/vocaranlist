
function myFunction() {
    document.getElementById("title").innerHTML = "Welcome!";
}

function myfilter() {
    var input, i, lines, idd, filteri;
    input = document.getElementById('filterinput').value;
    lines = document.getElementsByTagName('div');
    filteri = 0;
    for(i=0; i<lines.length; i++)
    {
        if(lines[i].getAttribute('type') != "line") continue;
        idd = lines[i].id;
        if(idd.indexOf(input) > -1)
        {
            lines[i].style.display = "";
            if(filteri%2==0) { lines[i].className = "btn-group gray-background"; }
            else { lines[i].className = "btn-group white-background"; }
            filteri++;
        }
        else { lines[i].style.display = "none"; }
    }
}

function copylink(str, noti) {
    const el = document.createElement('textarea');
    el.value = str;
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);
    document.getElementById('clipboardtxt').innerHTML = "Copied "+noti+".";
}

function darkendate(sm) {
    document.getElementById('d'+sm).style.opacity = "1";
    var thetab = document.getElementById('songlist');
    for(var i=0; i<42; i++)
    {
        var eletr = document.getElementById('tr'+i);
        if(eletr !== null) { eletr.remove(); }
    }
    document.getElementById('tda-1').innerHTML = '【'+episodejsonobj[sm][1]+'】 '+episodejsonobj[sm][2];
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
        newtd.appendChild(newtda);
    }
}
function fadedate(sm) {
    document.getElementById('d'+sm).style.opacity = "0.6";
}

function statusbar(str) {
    document.getElementById('clipboardtxt').innerHTML = str;
}

function appinput(str) {
    document.getElementById('filterinput').value += str;
    myfilter();
}


