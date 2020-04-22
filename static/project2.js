document.addEventListener('DOMContentLoaded', () => {

    var socket = io.connect('http://' + document.domain + ':' + location.port + '/index');
    socket.on('connect', function () {
        socket.emit('connected');
    });
    // console.log(io.sockets.adapter.rooms);
    // var rooms =  io.sockets.manager.roomClients[socket.id];
    // var clients = io.adapter.allRooms( (err, rooms) => {
    //     console.log(rooms)
    // });
    socket.on('new_user', msg => {
        const li = document.createElement('li');
        li.innerHTML = msg.msg
        document.querySelector('#messages').append(li)
    });
    // socket.on('newMessage', msg => {

    // })
    // });
    socket.on('addEvent', msg => {
        const li = document.createElement('li');
        // var user = localStorage.getItem('user');
        // li.innerHTML = user.bold() + ': ' + msg;
        li.innerHTML = msg.msg;
        document.querySelector('#messages').append(li);
    });
    document.querySelector('button').onclick = submit;
    function submit() {
        var msg = document.querySelector('#myMessage').value;
        socket.emit('submitted', {'data':msg} );
        document.querySelector('#myMessage').value='';
    };
// });
});
