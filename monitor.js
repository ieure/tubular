var tube = document.getElementById("tube");
var t;
tube.onkeyup = function(event) {
    if (t) {
        window.clearTimeout(t);
    }
    t = setTimeout(searchEvent, 200);
};

var form = document.getElementsByTagName("form")[0];
form.onsubmit = searchEvent;

window.onpopstate = function(event) {
    if (event.state && event.state.tube) {
        setState(event.state.tube);
    }
};

window.onload = function() {
    var state = window.location.hash.substring(1);
    if (state) {
        setState(state);
    } else {
        tube.focus();
    }
};

function setState(state) {
    tube.value = state;
    searchFor(state);
}

function makeRow(tube) {
    var row = document.createElement("tr");
    if (tube[3] == "c") {
        var typeLabel = "color";
    } else {
        var typeLabel = "mono";
    }

    var modelCell = document.createElement("td");
    modelCell.appendChild(document.createTextNode(tube[0]));
    var heaterCell = document.createElement("td");
    heaterCell.appendChild(document.createTextNode(tube[1] + "v"));
    var crcaCell = document.createElement("td");
    crcaCell.appendChild(document.createTextNode("CR-" + tube[2]));
    var typeCell = document.createElement("td");
    if (tube[3] == 1) {
        var typeLabel = "color";
    } else {
        var typeLabel = "mono";
    }
    typeCell.appendChild(document.createTextNode(typeLabel));

    row.appendChild(modelCell);
    row.appendChild(heaterCell);
    row.appendChild(crcaCell);
    row.appendChild(typeCell);
    return row;
};

function flush(node) {
    while (node.childNodes.length >= 1) {
        node.removeChild(node.firstChild);
    }
};

function searchEvent(event) {
    if (event) {
        event.stopPropagation();
    }
    var text = document.getElementById("tube").value
    if (event && event.type == "submit" || text.length > 1) {
        searchFor(text);
        history.pushState(
            {"tube": text}, "Monitor Helper: " + text, "#" + text);
    }
    return false;
}

function searchFor(tube) {
    var exp = new RegExp(tube, "i");
    var tbody = document.getElementById("tbody");
    flush(tbody);
    if (! tube) {
        return;
    }
    for (i in tubes) {
        if (tubes[i][0].search(exp) !== -1) {
            tbody.appendChild(makeRow(tubes[i]));
        }
    }
};
