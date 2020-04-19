document.addEventListener('DOMContentLoaded', () => {
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('connect', () => {
        socket.emit('connected', {'data':'connected'});
    }
})