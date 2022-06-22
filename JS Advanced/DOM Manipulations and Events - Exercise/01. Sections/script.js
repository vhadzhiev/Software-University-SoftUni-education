function create(words) {
   let parent = document.getElementById('content');

   for (let word of words) {
      let newDiv = document.createElement('div');
      let newP = document.createElement('p');

      newP.style.display = 'none';
      newP.textContent = word;
      
      newDiv.appendChild(newP);
      parent.appendChild(newDiv);

      newDiv.addEventListener('click', click)
   }

   function click(event) {
      event.currentTarget.children[0].style.display = '';
   }
}