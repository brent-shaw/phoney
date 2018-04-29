#!flask/bin/python
from app import app, socketio

try:
    socketio.run(app, host='0.0.0.0', debug=True)
except KeyboardInterrupt:
    print('\nDone.')