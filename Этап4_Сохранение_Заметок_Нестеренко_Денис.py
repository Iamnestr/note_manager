# Файловый ввод
import yaml

# Функция для сохранения и загрузки заметок в файл
def save_notes_to_file(notes, filename):

    # Смена ключей в словарях
    for note_keys in range(len(notes)):
        list_keys = ["Имя пользователя", "Заголовок", "Описание", "Статус", "Дата создания", "Дата дедлайна"]
        notes[note_keys] = dict(zip(list_keys, list(notes[note_keys].values())))

    # Сохранение и загрузка заметок в файл
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(yaml.dump(notes, allow_unicode=True, sort_keys=False))

# Пример списка заметок
notes_all = [{'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю',
          'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
          {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену',
           'status': 'в процессе', 'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
          {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект',
           'status': 'выполнено', 'created_date': '20-11-2024', 'issue_date': '26-11-2024'}]

# Вызов функции для сохранения и загружения заметок
save_notes_to_file(notes_all, 'notes.yml')





