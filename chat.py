# -*- coding: utf-8 -*-

"""
Chat Server
===========

This simple application uses WebSockets to run a primitive chat server.
"""


from flask import Flask, render_template
from flask_sockets import Sockets


app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/echo')
def echo_soc(ws):
    while not ws.closed:
        msg = ws.receive()
        print(ws)
        print(msg)
        if "hello".lower() in msg.lower() or "hi".lower() in msg.lower() or "привет".lower() in msg.lower() :
            ws.send("Приветствую")
        else:
            ws.send("Я не понимаю")



@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
