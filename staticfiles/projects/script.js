const badges = document.querySelectorAll("#tags-list li");

badges.forEach((badge) => {
    const randomColor = `#${Math.floor(Math.random()*16777215).toString(16)}`;
    badge.style.backgroundColor = randomColor;
});