function attachEventsListeners() {
    let convertBtn = document.getElementById('convert');
    convertBtn.addEventListener('click', onClick);

    let metrics = {
        km: 1000,
        m: 1,
        cm: 0.01,
        mm: 0.001,
        mi: 1609.34,
        yrd: 0.9144,
        ft: 0.3048,
        in: 0.0254,
    }

    function onClick(event) {
        let input = Number(document.getElementById('inputDistance').value);
        let inputUnits = document.getElementById('inputUnits').value;
        let outputUnits = document.getElementById('outputUnits').value;
        let outputEl = document.getElementById('outputDistance');

        let valueInM = input * metrics[inputUnits];
        let convertedValue = valueInM / metrics[outputUnits];
        outputEl.value = convertedValue
    }
}