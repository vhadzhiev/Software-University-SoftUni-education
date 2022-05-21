function roadRadar(speed, area) {
    let drivingSpeed = Number(speed);
    let drivingArea = area;
    let speedLimit = 0;
    let speedDiff = 0;
    let result = '';
    let status = ''


    if (drivingArea == 'motorway') {
        speedLimit = 130
        if (drivingSpeed >= speedLimit) {
            speedDiff = drivingSpeed - speedLimit
        }
    } else if (drivingArea == 'interstate') {
        speedLimit = 90
        if (drivingSpeed >= speedLimit) {
            speedDiff = drivingSpeed - speedLimit
        }
    } else if (drivingArea == 'city') {
        speedLimit = 50
        if (drivingSpeed >= speedLimit) {
            speedDiff = drivingSpeed - speedLimit
        }
    } else {
        speedLimit = 20
        if (drivingSpeed >= speedLimit) {
            speedDiff = drivingSpeed - 20
        }
    }

    if (speedDiff > 40) {
        status = 'reckless driving'
    } else if (speedDiff > 20) {
        status = 'excessive speeding'
    } else if (speedDiff > 0) {
        status = 'speeding'
    } else {
        console.log(`Driving ${drivingSpeed} km/h in a ${speedLimit} zone`)
    }

    if (status) {
        console.log(`The speed is ${speedDiff} km/h faster than the allowed speed of ${speedLimit} - ${status}`)
    }
}

roadRadar(40, 'city');
roadRadar(21, 'residential');
roadRadar(120, 'interstate');
roadRadar(200, 'motorway');