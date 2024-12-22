from datetime import datetime

# Создание меню действий
def menu():
    while True:
        print("\nМеню действий:")
        print("1. Создать новую заметку")
        print("2. Показать все заметки")
        print("3. Обновить заметку")
        print("4. Удалить заметку")
        print("5. Найти заметки")
        print("6. Выйти из программы")
        your_choice = int(input("\nВаш выбор: "))
        if your_choice == 6:
            print("Программа завершена. Спасибо за использование!")
            break
        elif your_choice == 1:
            create_note()
        elif your_choice == 2:
            display_notes()
        elif your_choice == 3:
            update_note()
        elif your_choice == 4:
            delete_note()
        elif your_choice == 5:
            search_notes()
        else:
            print("Неверный выбор. Пожалуйста, выберите действие из списка.")

# Функция создания заметки
def create_note():
    note = {'Имя пользователя': 'Алексей', 'Заголовок': 'Список покупок', 'Описание': 'Купить продукты на неделю',
            'Статус': 'новая', 'Дата создания': '27-11-2024', 'Дата дедлайна': '30-11-2024'}
    print("Новая заметка:")
    for key, value in note.items():
        print(f"{key.capitalize()}: {value}")
    print("Новая заметка создана!")

# Функция отображения заметок
def display_notes():
    notes = [{'Имя пользователя': 'Алексей', 'Заголовок': 'Список покупок', 'Описание': 'Купить продукты на неделю',
              'Статус': 'новая', 'Дата создания': '27-11-2024', 'Дата дедлайна': '30-11-2024'},
             {'Имя пользователя': 'Мария', 'Заголовок': 'Учеба', 'Описание': 'Подготовиться к экзамену',
              'Статус': 'в процессе', 'Дата создания': '25-11-2024', 'Дата дедлайна': '01-12-2024'},
             {'Имя пользователя': 'Иван', 'Заголовок': 'План работы', 'Описание': 'Завершить проект',
              'Статус': 'выполнено', 'Дата создания': '20-11-2024', 'Дата дедлайна': '26-11-2024'}]
    print("\nСписок заметок:")
    print("-----------------")
    for i in range(len(notes)):
        print(f"Заметка № {i+1}:")
        note = notes[i]
        for key, value in note.items():
            print(f"{key.capitalize()}: {value}")
        print("-----------------")

# Функция обновления заметки
def update_note():
    # Выводим текущие данные заметки
    note = {'username': 'Алексей',
            'title': 'Список покупок',
            'content': 'Купить продукты на неделю',
            'status': 'новая',
            'created_date': '27-11-2024',
            'issue_date': '30-11-2024'}

    # Создаем список ключей, значения которых будем менять
    note_key = ['username', 'title', 'content', 'status', 'issue_date']

    # Выбираем поле для обновления
    while True:
        update = input('\nКакие данные вы хотите обновить? (username, title, content, status, issue_date): ')

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
    print(note)
    print("Заметка обнавлена!")

# Функция удаления заметки
def delete_note():
    note_1 = {'Имя': 'Алексей', 'Заголовок': 'Список покупок', 'Описание': 'Купить продукты на неделю'}
    note_2 = {'Имя': 'Мария', 'Заголовок': 'Учеба', 'Описание': 'Подготовиться к экзамену'}
    note_3 = {'Имя': 'Алексей', 'Заголовок': 'Учеба', 'Описание': 'Оно мне надо)'}
    notes = [note_1, note_2, note_3]
    notes_del = []
    caunt = 3  # кол-во заметок
    caunt_del = 0  # кол-во заметок для удаления

    # Отображаем текущие заметки:
    print('Текущие заметки:')
    for i in range(caunt):
        print(f"{i + 1}.", end=' ')
        note = notes[i]
        for key, value in note.items():
            print(f"{key.capitalize()}: {value}")

    # Пользователь вводит критерий для удаления:
    delete = input('\nВведите имя пользователя или заголовок для удаления заметки: ')

    #  Поиск и сбор заметок соответствующих критерию в отдельный словарь
    for i in range(caunt):
        note = notes[i]
        if (note['Имя'].casefold() == delete.casefold() or
                note['Заголовок'].casefold() == delete.casefold()):
            caunt -= 1
            notes_del.append(note)
            caunt_del += 1

    # Если заметок по критерию не найдено
    if not notes_del:
        print('Заметок с таким именем пользователя или заголовком не найдено')

    # Удаление заметок соответствующих критерию после разрешения
    else:
        yes_or_no = input("\nВы уверены, что хотите удалить заметки? (да/нет): ")
        if yes_or_no == "да":
            for t in range(caunt_del):
                notes.remove(notes_del[t])
            print('Успешно удалено. Остались следующие заметки:')

            # Вывод обновленного списка
            for j in range(caunt):
                print(f"{j + 1}.", end=' ')
                note = notes[j]
                for key, value in note.items():
                    print(f"{key.capitalize()}: {value}")
        else:
            print('Заметки не удалены.')

# Функция поиска заметок
def search_notes():
    notes = [{'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю',
                  'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
                 {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену',
                  'status': 'в процессе', 'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
                 {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект',
                  'status': 'выполнено', 'created_date': '20-11-2024', 'issue_date': '26-11-2024'}]
    keyword = 'Иван'
    notes_found = []

    # Функция для сбора значений заметки 'username', 'title', 'content' в одну строку
    def values_all():
        values = ''
        for v in note.values():
            values += v.lower()
            if values == 'created_date':
                break
        return values.find(keyword.lower())

    # Поиск по ключевому слову и статусу
    if keyword is not None:
        for j in range(len(notes)):
            note = notes[j]
            if values_all() >= 0:
                notes_found.append(note)
    print("Найдена заметка:", notes_found)

# Создаем точку входа
if __name__ == '__main__':
    menu()