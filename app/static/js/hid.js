function val_map(value, oldMin, oldMax, newMin, newMax) {
    oldSpan = oldMax - oldMin;
    newSpan = newMax - newMin;

    valueScaled = (value - oldMin) / (oldSpan);

    return newMin + (valueScaled * newSpan);
}

function gyro_to_xy(alpha, beta, gamma){
    x = val_map(beta, -30, 30, 0, 1919)
    y = val_map(gamma, -30, 30, 0, 1079)
    return {x, y};
}

function touch_to_xy(x, y){
    x = val_map(y, 0, 1500, 0, 1919)
    y = val_map(x, 0, 500, 0, 1079)
    return {x, y};
}

function send_mouse(x, y){
    socket.emit('tilt event', {mouse: {x: x, y: y}});
}