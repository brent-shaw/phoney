from flask import Flask
from flask_socketio import SocketIO

print('Hit \'Ctrl+C\' when done playing with your phone!')

app = Flask(__name__)
socketio = SocketIO(app, logger=False, engineio_logger=False)

from app import views
