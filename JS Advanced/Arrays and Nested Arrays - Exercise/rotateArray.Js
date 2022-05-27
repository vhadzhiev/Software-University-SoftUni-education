function rotate(arr, turns) {
    for (let i = 0; i < turns; i++) {
        let num = arr.pop();
        arr.unshift(num);
    }

    console.log(arr.join(' '));
}

rotate(['1',
        '2',
        '3',
        '4'
    ],
    2
);
rotate(['Banana',
        'Orange',
        'Coconut',
        'Apple'
    ],
    15
);