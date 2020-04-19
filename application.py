import os

from flask import Flask, render_template, request, url_for
from flask_socketio import SocketIO, emit, send, join_room, leave_room

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

users = {'admin':'1234'}
@app.route("/")
def login():
    return render_template("login.html")

@app.route("/index")
def index():
    return render_template("index.html")

# @socketio.on("newTab")
# def newTab():
#     print(request.sid)


@socketio.on("connectionEvent") 
def test(info):
    message = info['data'][0]
    id = message['id']
    user = message['user']
    # user = ''
    # for key,value in users.items():
    #     if value == request.sid:
    #         user = key
    #         break
    #     else:
    #         users[user] = request.sid
    # print(users)
    connection = message['connect']
    user_info = {'user':user, 'connection':connection}
    emit("addConnection", user_info, broadcast=True)

@socketio.on("submitted")
def submit(info):
    message = info['data']
    emit("addEvent", message, broadcast=True)

@socketio.on("username")
def user(username):
    user = username["username"]
    if user not in users.keys():
        users[user] = request.sid
    emit('redirect', {'data':[{'url':url_for('index'), 'user':user}]}, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True)