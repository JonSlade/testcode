document.addEventListener("DOMContentLoaded", () => {
    
    var socket = io();
    // socket_login.on('connect', () => {
    //     socket_login.emit('newTab');
    // });
    document.querySelector('button').onclick = () => {
        var username = document.querySelector('#login').value;
        socket.emit('username', {'username':username});
    };
    socket.on('redirect', data => {
        localStorage.setItem('user',data.data[0].user);
        window.location=data.data[0].url;
    });
});