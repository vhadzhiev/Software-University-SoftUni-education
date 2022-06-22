function encodeAndDecodeMessages() {
    let textAreas = document.querySelectorAll('textarea');
    let buttons = document.querySelectorAll('button');

    buttons[0].addEventListener('click', encode);
    buttons[1].addEventListener('click', decode);

    function encode(event) {
        let input = textAreas[0].value;
        let encodedMessage = '';

        for (let i = 0; i < input.length; i++) {
            encodedMessage += String.fromCharCode(input[i].charCodeAt(0) + 1);
        }

        textAreas[1].value = encodedMessage;
        textAreas[0].value = '';
    }

    function decode(event) {
        let input = textAreas[1].value;
        let decodedMessage = '';

        for (let i = 0; i < input.length; i++) {
            decodedMessage += String.fromCharCode(input[i].charCodeAt(0) - 1);
        }

        textAreas[1].value = decodedMessage;
    }
}