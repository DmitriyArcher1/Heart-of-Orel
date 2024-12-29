// document.addEventListener('DOMContentLoaded', () => {
//     const modal = document.getElementById('modal');
//     const modalImage = document.getElementById('modal-image');
//     const thumbnails = document.querySelectorAll('.thumbnail');
//     const closeButton = document.querySelector('.close');
//     const body = document.querySelector('body'); // Получаем ссылку на body

//     thumbnails.forEach(thumbnail => {
//         thumbnail.addEventListener('click', () => {
//             modal.style.display = 'flex'; // Показываем модальное окно (используем flex)
//             modalImage.src = thumbnail.src;
//             modalImage.alt = thumbnail.alt;
//             body.style.overflow = 'hidden'; // Отключаем прокрутку страницы
//         });
//     });

//     closeButton.addEventListener('click', () => {
//         modal.style.display = 'none';
//         body.style.overflow = 'auto'; // Включаем прокрутку страницы
//     });

//     window.addEventListener('click', (event) => {
//         if (event.target === modal) {
//             modal.style.display = 'none';
//             body.style.overflow = 'auto'; // Включаем прокрутку страницы
//         }
//     });
// });
