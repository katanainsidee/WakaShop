document.addEventListener('DOMContentLoaded', function () {
    var currentImageIndex = 0;
    var images = document.querySelectorAll('.slider-image');
    var totalImages = images.length;

    // Скрываем все изображения, кроме первого
    hideAllImages();
    showImage(currentImageIndex);

    // Обработчик события для кнопки "Вперед"
    document.getElementById('next-btn').addEventListener('click', function () {
        hideImage(currentImageIndex);
        currentImageIndex = (currentImageIndex + 1) % totalImages;
        showImage(currentImageIndex);
    });

    // Обработчик события для кнопки "Назад"
    document.getElementById('prev-btn').addEventListener('click', function () {
        hideImage(currentImageIndex);
        currentImageIndex = (currentImageIndex - 1 + totalImages) % totalImages;
        showImage(currentImageIndex);
    });

    // Функция скрытия всех изображений
    function hideAllImages() {
        images.forEach(function (image) {
            image.style.display = 'none';
        });
    }

    // Функция скрытия изображения по индексу
    function hideImage(index) {
        images[index].style.display = 'none';
    }

    // Функция показа изображения по индексу
    function showImage(index) {
        images[index].style.display = 'block';
    }
});