# Файловый вывод
import yaml

# Функция для выгрузки заметок из файла
def load_notes_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        notes = yaml.safe_load(file.read())

    # Смена ключей в словарях
    for note_keys in range(len(notes)):
        list_keys = ["username", "title", "content", "status", "created_date", "issue_date"]
        notes[note_keys] = dict(zip(list_keys, list(notes[note_keys].values())))
    print(notes)

# Функция для выгрузки заметок из файла
load_notes_from_file('notes.yml')