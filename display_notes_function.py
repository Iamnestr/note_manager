# Функция обновления заметки
from datetime import datetime
# Задаем пример заметки
note = {'username': 'Алексей',
            'title': 'Список покупок',
            'content': 'Купить продукты на неделю',
            'status': 'новая',
            'created_date': '27-11-2024',
            'issue_date': '30-11-2024'}

# Вызываем функцию для обновления заметки
def update_note():
    # Выводим текущие данные заметки
    print('Текущие данные заметки:\n', note)

    # Создаем список ключей, значения которых будем менять
    note_key = ['username', 'title', 'content', 'status', 'issue_date']

    # Выбираем поле для обновления
    while True:
        update = input('Какие данные вы хотите обновить? (username, title, content, status, issue_date): ')

        # Проверяем корректность ввода
        if update not in note_key:
            print('Некорректный выбор поля. Попробуйте еще раз.')
        elif update == note_key[4]:
            while True:
                note[update] = input(f'Введите новое значение для {update} (день-месяц-год): ')
                try:
                    datetime.strptime(note[update], "%d-%m-%Y")
                    break
                except ValueError:
                    print('Формат даты неверный. Попробуйте ввести заново.')
            break
        else:
            note[update] = input(f'Введите новое значение для {update}: ')
            break
    return note

# Вывод обновленной заметки
print('Заметка обновлена:\n', update_note())