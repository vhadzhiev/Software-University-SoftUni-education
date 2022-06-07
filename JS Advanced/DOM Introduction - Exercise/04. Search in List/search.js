function search() {
    let list = document.querySelectorAll('ul#towns li');
    let result = document.getElementById('result');
    let search = document.getElementById('searchText').value;
    let matches = 0;

    for (let element of list) {
        element.style.fontWeight = 'normal';
        element.style.textDecoration = '';
    }

    for (let element of list) {
        let text = element.textContent;

        if (text.match(search)) {
            matches++;
            element.style.fontWeight = 'bold';
            element.style.textDecoration = 'underline';
        }
    }

    result.textContent = `${matches} matches found`
}