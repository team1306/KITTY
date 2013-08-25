var x = 0;
var y = 0;
var drive = false;
var base = 0; // 1 for right, -1 for left
var bjoint = 0; // 1 for up, -1 for down
var tjoint = 0; // 1 for up, -1 for down
var claw = 0; // 1 for in, -1 for out
var disable = false;
var width = $(window).width();
var height = $(window).height();
var ws = new WebSocket("ws://10.42.0.35/data");
//var gamepadsupport = Modernizr.gamepads;

ws.onopen = function() {
    setInterval(send, 100);
    ws.send("mod:base");
}

ws.onmessage = function(m) {
    $("#d").text(m.data);
}

ws.onclose = function() {
    $("#d").html("An internal server error has occured.<br/>Please power cycle the robot and reload the page.");
    var ws = new WebSocket("ws://10.42.0.35/data");
}

function send() {
    theta = Math.atan2(y, x);
    r = Math.sqrt(x*x + y*y);
    text = theta.toString() + "," + r.toString() + "," + base.toString() + "," + bjoint.toString() + "," + tjoint.toString() + "," + claw.toString()+";";
    ws.send(text);
}

function down(e) {
    k = String.fromCharCode(e.which);
    switch(e.keyCode) {
	//Left Arrows
	case 65:
    case 37:
	x = -50;
	y = 0;
	break;
	//Up Arrows
    case 87:
    case 38:
	x = 0;
	y = 50;
	break;
	//Right Arrows
    case 68:
    case 39:
	x = 50;
	y = 0;
	break;
	//Down Arrows
    case 83:
    case 40:
	x = 0;
	y = -50;
	break;
	// Q disables
    case 81:
	x = 0;
	y = 0;
	if(disable) {
	    disable = false;
	}
	else {
	    disable = true;
	}
	break;
    }
}

function up(e) {
    k = String.fromCharCode(e.which);
    if((e.keyCode < 41 && e.keyCode > 36) || e.keyCode == 83 || e.keyCode == 68 || e.keyCode == 87 || e.keyCode == 65) {
	x = 0;
	y = 0;
    }
}

function denable(e) {
    if(!drive) {
	drive = true;
	move(e);
    }
}

function brdown(e) {
    base = 1;
}

function bldown(e) {
    base = -1;
}

function baudown(e) {
    bjoint = 1;
}

function baddown(e) {
    bjoint = -1;
}

function taudown(e) {
    tjoint = 1;
}

function taddown(e) {
    tjoint = -1;
}

function codown(e) {
    claw = -1;
}

function ccdown(e) {
    claw = 1;
}

function ddisable(e) {
    drive = false;
    x = 0;
    y = 0;
}

function bup(e) {
    base = 0;
}

function baup(e) {
    bjoint = 0;
}

function taup(e) {
    tjoint = 0;
}

function cup(e) {
    claw = 0;
}

function move(e) {
    if(drive) {
	x = e.pageX - $("#drive").offset().left - 100;
	y = -(e.pageY - $("#drive").offset().top - 100);
    }
}

function panic(e) {
    drive = false;
    x = 0;
    y = 0;
    base = 0;
    bjoint = 0;
    tjoint = 0;
    claw = 0;
}

$(document).ready(function() {
    $("#drive").mousedown(denable);

    $("#br").mousedown(brdown);
    $("#bl").mousedown(bldown);

    $("#bau").mousedown(baudown);
    $("#bad").mousedown(baddown);

    $("#tau").mousedown(taudown);
    $("#tad").mousedown(taddown);

    $("#co").mousedown(codown);
    $("#cc").mousedown(ccdown);

    $("#drive").mouseup(ddisable);

    $("#br").mouseup(bup);
    $("#bl").mouseup(bup);

    $("#bau").mouseup(baup);
    $("#bad").mouseup(baup);

    $("#tau").mouseup(taup);
    $("#tad").mouseup(taup);

    $("#co").mouseup(cup);
    $("#cc").mouseup(cup);

    $("#drive").mousemove(move);
    $("#drive").mouseleave(ddisable);

    $("#panic").mousedown(panic);

    $(document).keydown(down);
    $(document).keyup(up);
});
