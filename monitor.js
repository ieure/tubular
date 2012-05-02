var tube = document.getElementById("tube");
var t;
tube.onkeyup = function () {
    if (t) {
        window.clearTimeout(t);
    }
    t = setTimeout(search, 200);
};

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
    heaterCell.appendChild(document.createTextNode(tube[1]));
    var crcaCell = document.createElement("td");
    crcaCell.appendChild(document.createTextNode(tube[2]));
    var typeCell = document.createElement("td");
    if (tube[3] == "c") {
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

function search() {
    var tube = document.getElementById("tube");
    var exp = new RegExp(tube.value, "i");
    var tbody = document.getElementById("tbody");
    flush(tbody);
    if (! tube.value) {
        return;
    }
    for (i in tubes) {
        if (tubes[i][0].search(exp) !== -1) {
            tbody.appendChild(makeRow(tubes[i]));
        }
    }
    return false;
};
