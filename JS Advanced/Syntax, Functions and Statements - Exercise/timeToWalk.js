function timeToWalk(distanceInSteps, stepInMeters, speedInKmH) {
    let distanceInMeters = distanceInSteps * stepInMeters;
    let speedInMs = speedInKmH / 3.6;
    let restingMinutes = Math.floor(distanceInMeters / 500);
    let time = distanceInMeters / speedInMs + restingMinutes * 60;

    let timeHr = Math.floor(time / 3600);
    let timeMin = Math.floor(time / 60);
    let timeSec = Math.round(time - timeMin * 60);

    console.log(
        (timeHr < 10 ? '0' : '') + timeHr + ':' + (timeMin < 10 ? '0' : '') + timeMin + ':' + (timeSec < 10 ? '0' : '') + timeSec);
}

timeToWalk(4000, 0.60, 5);
timeToWalk(2564, 0.70, 5.5);