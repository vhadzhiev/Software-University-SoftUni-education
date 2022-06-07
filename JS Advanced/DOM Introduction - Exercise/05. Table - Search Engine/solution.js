function solve() {
    document.querySelector('#searchBtn').addEventListener('click', onClick);

    let rows = document.querySelectorAll('tbody tr');
    let searchText = document.getElementById('searchField');

    function onClick() {
        for (let row of rows) {
            row.classList.remove('select');
            if (searchText.value != '' && row.innerHTML.includes(searchText.value)) {
                row.className = 'select';
            }
        }

        searchText.value = '';
    }
}