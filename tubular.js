/**
 *
 *   __          __           __
 *  |  |_.--.--.|  |--.--.--.|  |.---.-.----.
 *  |   _|  |  ||  _  |  |  ||  ||  _  |   _|
 *  |____|_____||_____|_____||__||___._|__|
 *
 * © Copyright 2013 Ian Eure.
 * Author: Ian Eure <ian.eure@gmail.com>
 */

var tube = document.getElementById("tube");
var t;
var index = indexTubes(tubes);

var CINCOMPAT = 0;              // Incompatible
var CCOMPAT = 1;                // Compatible
var CMAYBE = 2;                 // Maybe compatible

function debounce(delay, handler) {
    var timer;
    return function(event) {
        if (timer) {
            window.clearTimeout(timer);
        }
        timer = setTimeout(handler, delay);
    };
};

function initialize() {
    tube.onkeydown = function(event) {
        var state = getState();
        hideLabel();
    };

    tube.onkeyup = debounce(200, searchEvent);

    tube.onkeyup = function(event) {
        var state = getState();
        if (!state.search) {
            showLabel();
        }

        if (t) {
            window.clearTimeout(t);
        }
        t = setTimeout(searchEvent, 200);
    };

    var form = document.getElementsByTagName("form")[0];
    form.onsubmit = searchEvent;

    var searchRes = document.getElementById("res")
    searchRes.onclick = function(event) {
        var node = event.target;
        while (node.tube == undefined | node.tagName == "body") {
            node = node.parentNode;
        }
        if (! node.tube) {
            return;
        }

        var s = "xref:" + node.tube[0];
        tube.value = s
        searchFor(s);
        updateState();
        tube.focus();
    };

    var readyStateCheckInterval = setInterval(function() {
        if (document.readyState === "complete") {
            initializeState();
            clearInterval(readyStateCheckInterval);
            window.onpopstate = function(event) {
                restoreState(event.state);
            };
        }
    }, 10);
};

function indexTubes(tubes) {
    var index = {};
    for (var i in tubes) {
        index[tubes[i][0]] = tubes[i]
    };
    return index;
}



// State

function initializeState() {
    var state = window.location.hash.substring(1);
    if (state) {
        restoreState(state);
    } else {
        tube.focus();
    }
};

function restoreState(state) {
    var state = parseState(state);
    if (state.search) {
        tube.value = state.search;
        hideLabel();
    }
    searchFor(state.search);
    setTitle(state);
};

function getState() {
    var stateObj = new Object;
    if (tube.value) {
        stateObj.search = tube.value.trim();
    }
    return stateObj;
};

function getStateHash() {
    return hashForState(getState());
};

function hashForState(state) {
    var stateCpts = new Array;
    if (state.search) {
        stateCpts.push("s/" + state.search);
    }
    return stateCpts.join(",");
};

function parseState(state) {
    var stateObj = new Object;
    if (!state) {
        return stateObj;
    }
    var cpts = state.split(",");
    for (var i in cpts) {
        switch (cpts[i].substring(0, 2)) {
        case "s/":
            stateObj.search = cpts[i].substring(2);
            break;
        }
    };
    return stateObj;
};

function updateState() {
    history.pushState(
        getState(), document.title, "#" + getStateHash());
};

function buildTitle(state)
{
    var title = "Tubular -";
    if (state.search) {
        title += " Search for " + state.search;
    }
    return title;
};

function setTitle(state) {
    document.title = buildTitle(state);
};


// BK Precision specific code

function makeRowBK(tube) {
    var row = document.createElement("tr");
    var classes = ["type"];
    if (tube[3] == 1) {
        classes.push("color");
    } else {
        classes.push("mono")
    }
    if (redGreenSwap.indexOf(tube[0]) != -1) {
        classes.push("grb");
    } else if (redBlueSwap.indexOf(tube[0]) != -1) {
        classes.push("bgr");
    }

    var modelCell = document.createElement("td");
    modelCell.appendChild(document.createTextNode(tube[0]));

    var heaterCell = document.createElement("td");
    heaterCell.appendChild(document.createTextNode(tube[1] + "v"));

    var crcaCell = document.createElement("td");
    crcaCell.appendChild(document.createTextNode("CR-" + tube[2]));

    var typeCell = document.createElement("td");
    typeCell.appendChild(document.createElement("span"));
    typeCell.setAttribute("class", classes.join(" "));

    var g1Cell = document.createElement("td");
    g1Cell.appendChild(document.createTextNode(tube[4] + "v"));

    row.appendChild(typeCell);
    row.appendChild(modelCell);
    row.appendChild(heaterCell);
    row.appendChild(g1Cell);
    row.appendChild(crcaCell);
    row.tube = tube;
    return row;
};

function isCompatibleBK(tubeA, tubeB) {
    return tubeA[1] == tubeB[1] &&  // Heater voltage
    tubeA[2] == tubeB[2] &&         // Socket
    tubeA[3] == tubeB[3] &&         // Color / mono
    tubeA[4] == tubeB[4] &&         // G1 voltage
    CCOMPAT
};


// Sencore-specific code

function makeRowSencore(tube) {
    var row = document.createElement("tr");

    var typeCell = document.createElement("td");
    typeCell.appendChild(document.createElement("span"));
    // Sencore data doesn't indicate color/B&W or gun swaps.
    typeCell.setAttribute("class", "type color");

    var modelCell = document.createElement("td");
    modelCell.appendChild(document.createTextNode(tube[0]));

    var heaterCell = document.createElement("td");
    heaterCell.appendChild(document.createTextNode(tube[3] + "v"));

    var biasCell = document.createElement("td");
    biasCell.appendChild(document.createTextNode(tube[4]));

    var socketCell = document.createElement("td");
    socketCell.appendChild(document.createTextNode(tube[1]));

    row.appendChild(typeCell);
    row.appendChild(modelCell);
    row.appendChild(heaterCell);
    row.appendChild(biasCell);
    row.appendChild(socketCell);
    row.tube = tube;
    return row;
};

function isCompatibleSencore(tubeA, tubeB) {
    return tubeA[3] == tubeB[3] &&  // Heater (filament) voltage
    tubeA[1] == tubeB[1] &&         // Socket
    tubeA[4] == tubeB[4] &&         // Bias
    CCOMPAT
};


// Mode thunks

if (mode == 'bk') {
    var makeRow = makeRowBK;
    var isCompatible = isCompatibleBK;
} else {
    var makeRow = makeRowSencore;
    var isCompatible = isCompatibleSencore;
}

function rowFor(tube) {
    if (!tube.row) {
        tube.row = makeRow(tube);
    }
    return tube.row;
};



function getTube(tube) {
    return index[tube];
};

function flush(node) {
    while (node.childNodes.length >= 1) {
        node.removeChild(node.firstChild);
    }
};

function showLabel() {
    document.getElementsByTagName("label")[0].style.display = "block";
}

function hideLabel() {
    document.getElementsByTagName("label")[0].style.display = "none";
}


// Predicates

var predicateMap = [
    [/^(xref:)(.*)/, xrefPredicate]
];

function substringOrRegexPredicate(search) {
    if (isRegex(search)) {
        return regexPredicate(search);
    }
    return substringPredicate(search.toUpperCase());
};

function isRegex(search) {
    return search.toLowerCase().search(/^[a-z0-9]+$/) == -1;
};

function substringPredicate(search) {
    return function(mTube) {
        return mTube[0].indexOf(search) !== -1;
    };
};

function regexPredicate(search) {
    try {
        var exp = new RegExp(search, "i");
    } catch(ex) {
        return substringPredicate(search.toUpperCase());
    }

    return function(mTube) {
        return mTube[0].search(exp) !== -1;
    };
};

function xrefPredicate(xrefTube) {
    var ti = index[xrefTube.toUpperCase()];
    if (ti == undefined) {
        console.warn("No such tube: " + xrefTube);
        return function(mTube) {
            return false;
        }
    }
    return function(mTube) {
        return isCompatible(ti, mTube);
    };
};

function combinePredicates(preds) {
    return function(x) {
        for (var i in preds) {
            if (!preds[i](x)) {
                return false;
            }
        }
        return true;
    }
};

function predicateFor(token) {
    for (i in predicateMap) {
        var m = token.match(predicateMap[i][0]);
        if (m) {
            return predicateMap[i][1](m[m.length - 1]);
        }
    }
    return substringOrRegexPredicate(token);
};

/**
 * Turn the search text into a predicate to apply to the tube list
 */
function makePredicates(text) {
    if (text.trim() == "") {
        var tokens = [];
    } else {
        var tokens = text.split(/\s+/);
    }
    var predicates = []
    for (var i in tokens) {
        predicates.push(predicateFor(tokens[i]));
    }
    return combinePredicates(predicates)
};


// Searching

function searchEvent(event) {
    if (event) {
        event.stopPropagation();
    }
    var state = getState();
    if (event && event.type == "submit" ||
        (state.search && state.search.length > 1)) {
        searchFor(state.search);
    }
    setTitle(state);
    updateState();
    return false;
};

function searchFor(text) {
    var predicate = makePredicates(text);
    var tbody = document.getElementById("res");
    flush(tbody);
    if (! text) {
        clearSearch();
        return;
    }
    // Hide the table while we mutate the body to avoid browser lag.
    document.getElementById("search").style.display = "none";
    for (i in tubes) {
        if (!predicate(tubes[i])) {
            continue;
        }
        tbody.appendChild(rowFor(tubes[i]));
    }
    document.getElementById("search").style.display = "table";
};

function clearSearch() {
    tube.value = "";
    document.getElementById("search").style.display = "none";
    showLabel();
    updateState();
    tube.focus();
};

initialize();
