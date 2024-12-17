# Функция создания заметки
from datetime import datetime

def create_note():
    # Определяем текущую дату
    current_date = datetime.today().strftime('%d-%m-%Y')

    # Создаем словарь для хранения информации о заметке
    note = {}

    # Сбор данных от пользователя
    note["username"] = input("Введите имя пользователя: ")
    note["title"] = input("Введите заголовок заметки: ")
    note["content"] = input("Введите описание заметки: ")
    note["status"] = input("Введите статус заметки (новая, в процессе, выполнено): ")
    note["created_date"] = current_date

    # Вводим дату дедлайна заметки и проверяем корректность ввода.
    while True:
        note["issue_date"] = input("Введите дату дедлайна (день-месяц-год): ")
        try:
            datetime.strptime(note["issue_date"], "%d-%m-%Y")
            break
        except ValueError:
            print("Формат даты неверный. Попробуй еще раз.")
    return note

# Выводим собранную информацию
print("Заметка создана:", create_note())