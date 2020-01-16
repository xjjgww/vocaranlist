
function myFunction() {
    document.getElementById("title").innerHTML = "Welcome!";
}

function myfilter() {
    // Declare variables
    var test = "#62";
    var input, i, lines, idd, filteri;
    // var input, filter, ul, li, a, i, txtValue;
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
            // if(filteri%2==0) { lines[i].style.backgroundColor = "#fafafa"; }
            // else { lines[i].style.backgroundColor = "white"; }
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
}
