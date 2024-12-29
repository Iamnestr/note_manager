# Выбор формата файла
import json

# Функция для сохранения и загрузки заметок в формате json
def save_notes_json(notes, filename):

    # Смена ключей в словарях
    for note_keys in range(len(notes)):
        list_keys = ["Имя пользователя", "Заголовок", "Описание", "Статус", "Дата создания", "Дата дедлайна"]
        notes[note_keys] = dict(zip(list_keys, list(notes[note_keys].values())))

    # Сохранение и загрузка заметок в файл
    with open(filename, 'w', encoding='utf-8') as file:
        j_file = json.dump(notes, file, indent=4, ensure_ascii=False)


notes_all = [{'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты',
                  'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'}]

save_notes_json(notes_all, "notes.json")