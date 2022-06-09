function getArticleGenerator(articles) {
    let parent = document.getElementById('content');

    function next() {
        let a = document.createElement('article');
        let article = articles.shift();
        if (article != undefined) {
            a.textContent = article;
            parent.appendChild(a);
        }
    }

    return next;
}