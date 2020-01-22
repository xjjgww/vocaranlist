
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
    for(var i=-1; i<42; i++)
    {
        ida = "tda"+i;
        document.getElementById(ida).innerHTML = "&nbsp;";
        if(i < 0)
        {
            document.getElementById(ida).innerHTML = '【'+episodejsonobj[sm][1]+'】 '+episodejsonobj[sm][2];
        }
        else if(i < songjsonobj[sm].length)
        {
            document.getElementById(ida).href = songjsonobj[sm][i]['url'];
            document.getElementById(ida).innerHTML = songjsonobj[sm][i]['title'];
        }
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


