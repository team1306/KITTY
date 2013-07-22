var drive = false;
var base = 0; // 1 for right, -1 for left
var bjoint = 0; // 1 for up, -1 for down
var tjoint = 0; // 1 for up, -1 for down
var claw = 0; // 1 for in, -1 for out
var disable = false;
var width = $(window).width();
var height = $(window).height();
var ws = new WebSocket("ws://192.168.1.248/data");

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

/*function change(e) {
    if(!disable) {
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
    else {
	text = "0,0"
    }
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
    case 81:
	text = "0,0";
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
	text = "0,0";
    }
}*/

function denable(e) {
    if(!drive) {
	drive = true;
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

function 
$(document).ready(function() {
    $("#drive").mousedown(denable);

    $("#br").mousedown(brdown);
    $("#bl").mousedown(bldown);

    $("#bau").mousedown(baudown);
    $("#bad").mousedown(baddown);

    $("#tau").mousedown(taudown);
    $("#tau").mousedown(taddown);

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

    //$(document).mousemove(change);
    //$(document).keydown(down);
    //$(document).keydown(down);
});
