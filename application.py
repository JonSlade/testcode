import os

from flask import Flask, render_template, request, url_for, session, redirect
from flask_socketio import SocketIO, emit, send, join_room, leave_room

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
socketio = SocketIO(app)

users = {'admin':'1234'}
@app.route("/", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['name'] = request.form.get("username")
        session['room'] = request.form.get("room")
        return redirect(url_for('.index'))
    else:
        user = session['name'] = ''
        room = session['room'] = ''
        if not user or not room:
            return render_template("login.html")
        else:
            return redirect(url_for('.index'))
        # print(session.get('name'))
        # print(session.get('name', ''))

@app.route("/index")
def index():
    name = session['name']
    room = session['room']
    # join_room(room)
    # print(name)
    if not name or not room:
        return redirect(url_for('./'))
    return render_template("index.html", name=name, room=room)
#some reason need namespace to work?
# @socketio.on('connected', namespace='/index')
@socketio.on('connected')
def connected():
    name = session['name']
    room = session['room']
    print("dsdsdf")
    print(room)
    # join_room(room)
    emit('new_user', {'msg':name + ': ' + 'has connected to'+ ' ' + room}, room=room)

# @socketio.on("submitted", namespace='/index')
@socketio.on("submitted")
def submit(info):
    message = info['data']
    name = session['name']
    room = session['room']
    emit("addEvent", {'msg':"["+name+"]" +": " + message}, room=room)
# # @socketio.on("newTab")
# # def newTab():   
# #     print(request.sid)


# @socketio.on("connectionEvent") 
# def test(info):
#     message = info['data'][0]
#     id = message['id']
#     user = message['user']
#     # user = ''
#     # for key,value in users.items():
#     #     if value == request.sid:
#     #         user = key
#     #         break
#     #     else:
#     #         users[user] = request.sid
#     # print(users)
#     connection = message['connect']
#     user_info = {'user':user, 'connection':connection}
#     emit("addConnection", user_info, broadcast=True)


# @socketio.on("username")
# def user(username):
#     user = username["username"]
#     if user not in users.keys():
#         users[user] = request.sid
#     emit('redirect', {'data':[{'url':url_for('index'), 'user':user}]}, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True)