# Функция создания заметки
# Определяем текущую дату
from datetime import datetime
current_date = datetime.today().strftime('%d-%m-%Y')

# Создаем словарь для хранения информации о заметке
create_note = {}

# Сбор данных от пользователя
create_note["username"] = input("Введите имя пользователя: ")
create_note["title"] = input("Введите заголовок заметки: ")
create_note["content"] = input("Введите описание заметки: ")
create_note["status"] = input("Введите статус заметки (новая, в процессе, выполнено): ")
create_note["created_date"] = current_date

# Вводим дату дедлайна заметки и проверяем корректность ввода.
while True:
    create_note["issue_date"] = input("Введите дату дедлайна (день-месяц-год): ")
    try:
        datetime.strptime(create_note["issue_date"], "%d-%m-%Y")
        break
    except ValueError:
        print("Формат даты не верный. Попробуй еще раз.")

# Вывод данных
print("Заметка создана:", create_note)