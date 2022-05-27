function sortBy2(arr) {
    arr.sort(twoCrSort);
    
    function twoCrSort(current, next) {
        if (current.length === next.length) {
            return current.localeCompare(next);
        }
        return current.length - next.length;
    }    

    console.log(arr.join('\n'));
}

sortBy2(['alpha',
    'beta',
    'gamma'
]);
sortBy2(['Isacc',
    'Theodor',
    'Jack',
    'Harrison',
    'George'
]);
sortBy2(['test',
    'Deny',
    'omen',
    'Default'
]);