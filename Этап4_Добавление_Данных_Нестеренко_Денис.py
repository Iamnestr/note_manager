# Добавление заметок
import yaml

# Функция для добавления заметок в файл
def append_notes_to_file(notes, filename):

    # Смена ключей в словарях
    for note_keys in range(len(notes)):
        list_keys = ["Имя пользователя", "Заголовок", "Описание", "Статус", "Дата создания", "Дата дедлайна"]
        notes[note_keys] = dict(zip(list_keys, list(notes[note_keys].values())))

    # Добавление заметок в файл
    with open(filename, 'a', encoding='utf-8') as file:
        try:
            file.write(yaml.dump(notes, allow_unicode=True, sort_keys=False))
        except FileNotFoundError:
            file = open(filename, 'x', encoding='utf-8')
            file.write(yaml.dump(notes, allow_unicode=True, sort_keys=False))

# Пример списка заметок
new_notes = [{"username": "Мария", "title": "План работы", "content": "Подготовить отчёт",
              "status": "в процессе", "created_date": "27-11-2024", "issue_date": "28-11-2024"}]

# Вызов функции для добавления заметок в файл
append_notes_to_file(new_notes, "notes.txt")