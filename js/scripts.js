
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

function copylink(str) {
    const el = document.createElement('textarea');
    el.value = str;
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);
    document.getElementById('clipboardtxt').innerHTML = "Copied the link.";
}

function darkendate(str) {
    document.getElementById(str).style.opacity = "1";
}
function fadedate(str) {
    document.getElementById(str).style.opacity = "0.6";
}

function showurl(str) {
    document.getElementById('clipboardtxt').innerHTML = str;
}
function hideurl() {
    document.getElementById('clipboardtxt').innerHTML = "&nbsp;";
}
