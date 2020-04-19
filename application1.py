import os

from flask import Flask, render_template, request, url_for
from flask_socketio import SocketIO, emit, send, join_room, leave_room

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretKey"
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template("index1.shtml")

@socketio.on('connected')
def connection(data):
    print(data)

if __name__ == '__main__':
    socketio.run(app, debug=True)