function solve() {
    let text = document.getElementById('input').value;
    let sentences = text.split('.').filter(s => s.length != 0);
    let result = document.getElementById('output');
    
    while (sentences.length > 0) {
        let paragraph = sentences.splice(0, 3).join('.') + '.';
        let p = document.createElement('p');
        p.textContent = paragraph;
        result.appendChild(p);
    }
}