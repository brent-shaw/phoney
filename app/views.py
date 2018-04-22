from flask import render_template
from flask_socketio import emit
from app import app, socketio
import mouse

last_x = 0
last_y = 0

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

@app.route('/')
@app.route('/tilt_mouse')
def tilt_mouse():
    return render_template("tilt_mouse.html")


@socketio.on('move event', namespace='/tilt_mouse')
def tilt_message(message):
    global count, last_x, last_y

    x = message['mouse']['x']
    y = message['mouse']['y']

    if (x != last_x or y != last_y):
        mouse.move(x,y)
        last_x = x
        last_y = y