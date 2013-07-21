var text = "0,0";
var width = $(window).width();
var height = $(window).height();
var ws = new WebSocket("ws://192.168.0.20/data");

ws.onopen = function() {
    setInterval(send, 100);
}

ws.onmessage = function(m) {
    $(d).text(m.data);
}

ws.onclose = function() {
    $(d).html("An internal server error has occured.<br/>Please power cycle the robot and reload the page.");
}

function send() {
    ws.send(text);
}

function change(e) {
    x = e.pageX - $(window).width()/2;
    y = -1 * (e.pageY - $(window).height()/2);
    r = Math.sqrt(x*x + y*y);
    if(Math.abs(r) < 10) {
	r = 0;
    }
    else {
	r = r - 10;
    }
    theta = Math.atan2(y, x);
    text = theta + "," + r;
}

function down(e) {
    k = String.fromCharCode(e.which);
    switch(e.keyCode) {
    case 65:
    case 37:
	text = Math.PI+",50";
	break;
    case 87:
    case 38:
	text = (Math.PI/2)+",50";
	break;
    case 68:
    case 39:
	text = "0,50";
	break;
    case 83:
    case 40:
	text = -(Math.PI/2)+",50";
	break;
    }
}

function up(e) {
    k = String.fromCharCode(e.which);
    if((e.keyCode < 41 && e.keyCode > 36) || e.keyCode == 83 || e.keyCode == 68 || e.keyCode == 87 || e.keyCode == 65) {
	text = "0,0";
    }
}

$(document).ready(function() {
    var c=document.getElementById("can");
    var ctx=c.getContext("2d");
    ctx.beginPath();
    ctx.arc(25,25,10,0,2*Math.PI);
    ctx.stroke();
    $(document).mousemove(change);
    $(document).keydown(down);
    $(document).keyup(up);
});
