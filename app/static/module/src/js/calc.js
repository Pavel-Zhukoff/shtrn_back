function set(op) {

    document.getElementById("calcInput").value += op;

}

function sqrRoot() {
    var tempStore = document.getElementById("calcInput").value;
    document.getElementById("calcInput").value = eval(Math.sqrt(tempStore));

}

function asine() {
    var tempStore = document.getElementById("calcInput").value;
    document.getElementById("calcInput").value = eval(Math.asin(tempStore));

}

function acosine() {
    var tempStore = document.getElementById("calcInput").value;
    document.getElementById("calcInput").value = eval(Math.acos(tempStore));

}

function fLog() {
    var tempStore = document.getElementById("calcInput").value;
    document.getElementById("calcInput").value = eval(Math.log(tempStore));

}

function atangent() {
    var tempStore = document.getElementById("calcInput").value;
    document.getElementById("calcInput").value = eval(Math.atan(tempStore));

}

function tangent() {
    var tempStore = document.getElementById("calcInput").value;
    document.getElementById("calcInput").value = eval(Math.tan(tempStore));

}

function cosine() {
    var tempStore = document.getElementById("calcInput").value;
    document.getElementById("calcInput").value = eval(Math.cos(tempStore));

}

function sine() {
    var tempStore = document.getElementById("calcInput").value;
    document.getElementById("calcInput").value = eval(Math.sin(tempStore));

}

function setOp() {
    alert("gf");
    //document.getElementById("display").value += op;
}

function answer() {
    $('#calcInput').val(eval($('#calcInput').val()))
}

function ce() {
    $('#calcInput').val(' ')
}
function events() {
    $('button.count').click(function () {
        set($(this).text())
    })
    $('#calcClear').click(ce)
    $('#answer').click(answer)

}
events()
