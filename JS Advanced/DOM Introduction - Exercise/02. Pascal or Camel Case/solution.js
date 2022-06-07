function solve() {
    let text = document.getElementById('text').value;
    let convention = document.getElementById('naming-convention').value;
    
    let result = text.toLowerCase().split(' ');
    
    for (let i = 1; i < result.length; i++) {
        result[i] = result[i][0].toUpperCase() + result[i].slice(1);
    }
    
    if (convention == 'Camel Case') {
        
    } else if (convention == 'Pascal Case') {
        result[0] = result[0][0].toUpperCase() + result[0].slice(1);
    } else {
        return document.getElementById('result').textContent = 'Error!'
    }

    document.getElementById('result').textContent = result.join('')
}