$(document).ready(function () {
    // Берем из разметки элемент по id - оповещения от django
    var notification = $('#notification');

    // И через 7 сек. убираем
    if (notification.length > 0) {
        setTimeout(function () {
            notification.fadeOut();
        }, 2000);
    }
});

