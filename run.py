#!flask/bin/python
from app import app, socketio

try:
    socketio.run(app, host='0.0.0.0', debug=False)
except KeyboardInterrupt:
    print('\nDone.')