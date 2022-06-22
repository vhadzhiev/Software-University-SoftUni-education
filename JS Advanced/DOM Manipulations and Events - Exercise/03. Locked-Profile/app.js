function lockedProfile() {
    Array.from(document.querySelectorAll('.profile button')).forEach(b => b.addEventListener('click', toggle))

    function toggle(event) {
        const profile = event.target.parentElement;
        const isUnlocked = profile.querySelector('input[type="radio"][value="unlock"]').checked;

        if (isUnlocked) {
            let div = profile.querySelector('div');
                
            if (event.target.textContent == 'Show more') {
                div.style.display = 'block';
                event.target.textContent = 'Hide it';
            } else {
                div.style.display = 'none';
                event.target.textContent = 'Show more';
            }
        }
    }
}