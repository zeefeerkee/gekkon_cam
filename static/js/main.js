// Функция отправки POST-запроса
function sendPostRequest(action) {
    fetch('/update_values', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
            'move': action,
        })
    });
}

// Обработчики событий для радиокнопок
document.querySelectorAll('.btn-check').forEach(radio => {
    radio.addEventListener('change', function() {
        if (this.checked) {  // Проверяем, выбрана ли кнопка
            const action = this.id;
            sendPostRequest(action);
        }
    });
});