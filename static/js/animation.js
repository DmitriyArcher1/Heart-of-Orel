const boxes = document.querySelectorAll('.animation');

function checkBoxes() {
    const triggerBottom = window.innerHeight / 5 * 4; // Определяем, когда элемент попадет в видимую область

    boxes.forEach(box => {
        const boxTop = box.getBoundingClientRect().top;

        if (boxTop < triggerBottom) {
            box.classList.add('show');
        } else {
            box.classList.remove('show');
        }
    });
}

window.addEventListener('scroll', checkBoxes);
checkBoxes();