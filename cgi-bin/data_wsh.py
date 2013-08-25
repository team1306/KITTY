from mod_pywebsocket import msgutil
import socket
import math

_GOODBYE_MESSAGE = 'Goodbye'

def web_socket_do_extra_handshake(request):
    pass  # Always accept.

def web_socket_transfer_data(request):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 50007))
    while True:
        line = request.ws_stream.receive_message()
        if line is None:
            return
        request.ws_stream.send_message(line)

        s.send(line)
        if line[:4] == "mod:":
            return
