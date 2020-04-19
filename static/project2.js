document.addEventListener('DOMContentLoaded', () => {

    var socket = io();
    socket.on('connect', function () {
        socket.emit('connectionEvent', {'data':[{'connect':'Connected'}]});
    });
    socket.on('addConnection', msg => {
        alert("hello");
        const li = document.createElement('li');
        li.innerHTML = msg.user + ' ' + msg.connection;
        document.querySelector('#messages').append(li);
    });
    socket.on('addEvent', msg => {
        const li = document.createElement('li');
        var user = localStorage.getItem('user');
        // li.innerHTML = user.bold() + ': ' + msg;
        li.innerHTML = `${socket.id}` + ': ' + msg;
        document.querySelector('#messages').append(li);
    });
    document.querySelector('button').onclick = submit;
    function submit() {
        var msg = document.querySelector('#myMessage').value;
        socket.emit('submitted', {'data':msg} );
        document.querySelector('#myMessage').value='';
    };
});
