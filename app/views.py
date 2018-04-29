from flask import render_template, request
from flask_socketio import emit
from app import app, socketio
import mouse
import socket
import hashlib

last_x = 0
last_y = 0

def getIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('1.0.0.1', 0))
    return s.getsockname()[0]

hostIP = getIP()

tempHash = hashlib.md5()
tempHash.update(hostIP.encode('utf8'))
siteAddress = '/'
siteAddress += tempHash.hexdigest()

@app.route('/')
@app.route('/getConnected')
def getConnected():
    connectAddress = 'http://'+hostIP+':5000'+siteAddress
    return render_template("getConnected.html", address=connectAddress)

@app.route(siteAddress)
def tilt_mouse():
    return render_template("tilt_mouse.html")

@socketio.on('move event', namespace=siteAddress)
def tilt_message(message):
    global count, last_x, last_y

    x = message['mouse']['x']
    y = message['mouse']['y']

    if (x != last_x or y != last_y):
        mouse.move(x,y)
        last_x = x
        last_y = y


@app.route('/test2')
def test2():
    return render_template("keyboard.html")

@app.route('/touch_mouse')
def touch_mouse():
    return render_template("touch_mouse.html")


@socketio.on('move event', namespace='/touch_mouse')
def touch_message(message):
    global count, last_x, last_y

    x = message['mouse']['x']
    y = message['mouse']['y']

    if (x != last_x or y != last_y):
        #mouse.move(x,y)
        last_x = x
        last_y = y
