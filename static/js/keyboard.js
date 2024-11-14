// Переменная для хранения текущего состояния
let currentClass = "keyboard";
let hidden = 1;

// Функция для изменения стиля на основе нажатой клавиши
document.addEventListener("keydown", function (event) {
    const keyboard = document.getElementById("keyboard");

    if (keyboard) {
        // Проверяем, существует ли элемент
        // Сброс стиля перед изменением
        keyboard.classList.remove("turn-w", "turn-a", "turn-s", "turn-d");

        // Изменение в зависимости от нажатой клавиши
        switch (event.key) {
            case "w":
            case "ц": // Английская "w" и русская "ц"
                keyboard.classList.add("turn-w"); // Добавляем класс "turn-w"
                break;

            case "a":
            case "ф": // Английская "a" и русская "ф"
                keyboard.classList.add("turn-a"); // Добавляем класс "turn-a"
                break;

            case "s":
            case "ы": // Английская "s" и русская "ы"
                keyboard.classList.add("turn-s"); // Добавляем класс "turn-s"
                break;

            case "d":
            case "в": // Английская "d" и русская "в"
                keyboard.classList.add("turn-d"); // Добавляем класс "turn-d"
                break;

            case "f":
            case "а": // Английская "f" и русская "а"
                if (hidden % 2) {
                    keyboard.classList.remove("visible"); // Удаляем класс "visible"
                    keyboard.classList.add("hidden"); // Добавляем класс "hidden"
                } else {
                    keyboard.classList.remove("hidden"); // Удаляем класс "hidden"
                    keyboard.classList.add("visible"); // Добавляем класс "visible"
                }
                hidden += 1;
                break;

            default:
            // Дефолтное поведение можно не трогать
        }
    }
});

// Возвращаем стиль к дефолту при отпускании клавиши
document.addEventListener("keyup", function (event) {
    const keyboard = document.getElementById("keyboard");

    if (keyboard) {
        // Проверяем, существует ли элемент
        // Сброс всех классов поворота и возврат к дефолту
        keyboard.classList.remove("turn-w", "turn-a", "turn-s", "turn-d");
        keyboard.classList.add("keyboard"); // Возвращаем класс "keyboard"
    }
});
