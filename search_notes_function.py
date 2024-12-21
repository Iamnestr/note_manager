# Функция поиска заметок
def search_notes(notes, keyword=None, status=None):
    notes_found = []

    # Проверяем какой критерий для поиска задан, потом ищем и собираем их в один лист
    if keyword is not None and status is not None:
        for i in range(len(notes)):
            note = notes[i]
            search_keyword = note['username'].lower() + " " + note['title'].lower() + " " + note['content'].lower()
            if (keyword.lower() in search_keyword.split()
                    and status.lower() == note['status'].lower()):
                notes_found.append(note)
    elif keyword is not None:
        for i in range(len(notes)):
            note = notes[i]
            search_keyword =  note['username'].lower() + " " + note['title'].lower() + " " + note['content'].lower()
            if keyword.lower() in search_keyword.split():
                notes_found.append(note)
    elif  status is not None:
        for i in range(len(notes)):
            note = notes[i]
            if status.lower() == note['status'].lower():
                notes_found.append(note)
    return notes_found

# Функция для вывода данных
def display_notes(notes_):
    if not notes_:
        print("Заметки, соответствующие запросу, не найдены.")
    else:
        print("\nНайденные заметки:")
        for i in range(len(notes_)):
            print(f"Заметка № {i+1}:")
            note = notes_[i]
            keys = ["Имя пользователя", "Заголовок", "Описание", "Статус", "Дата создания", "Дата дедлайна"]
            keys_index = 0
            for value in note.values():
                print(f"{keys[keys_index]}: {value}")
                keys_index += 1
            print("-----------------")

# Создание списка заметок, с которым будем работать
notes = [{'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю',
          'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
         {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену',
          'status': 'в процессе', 'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
         {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект',
          'status': 'выполнено', 'created_date': '20-11-2024', 'issue_date': '26-11-2024'}]

# Отображение исходного списка
print(f"Исходный список заметок:\nnotes =", end= " ")
if not notes:
    print("[]")
else:
    print("[")
    for i in range(len(notes)):
        print(notes[i])
    print("]")

# Выбор метода поиска
keyword_ = None
status_ = None
print("\nМетоды поиска:")
print("\t1. Поиск по ключевому слову.")
print("\t2. Поиск по статусу.")
print("\t3. Поиск по ключевому слову и статусу.")
search_method = int(input("Введите номер метода: "))
if search_method == 1:
    keyword_ = input("Поиск по ключевому слову: ")
elif search_method == 2:
    status_ = input("Поиск по статусу: ")
elif search_method == 3:
    keyword_ = input("Введите ключевое слово: ")
    status_ = input("Введите статус: ")
else:
    print("Не выбран метод поиска")

notes_total = search_notes(notes, keyword=keyword_, status=status_)

display_notes(notes_total)
