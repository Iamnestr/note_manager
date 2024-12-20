# Функция поиска заметок
def search_notes(notes, keyword=None, status=None):
    notes_search = []
    if keyword != None and status != None:
        for i in range(len(notes)):
            note = notes[i]
            search_keyword = note['username'].lower() + " " + note['title'].lower() + " " + note['content'].lower()
            if (keyword.lower() in search_keyword.split()
                    and status.lower() == note['status'].lower()):
                notes_search.append(note)
    elif keyword != None:
        for i in range(len(notes)):
            note = notes[i]
            search_keyword =  note['username'].lower() + " " + note['title'].lower() + " " + note['content'].lower()
            if keyword.lower() in search_keyword.split():
                notes_search.append(note)
    elif  status != None:
        for i in range(len(notes)):
            note = notes[i]
            if status.lower() == note['status'].lower():
                notes_search.append(note)
    return notes_search

# Создание списка заметок, с которым будем работать
notes = [{'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю',
          'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
         {'username': 'Мария', 'title': 'Учеба, список', 'content': 'Подготовиться к экзамену',
          'status': 'в процессе', 'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
         {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект',
          'status': 'выполнено', 'created_date': '20-11-2024', 'issue_date': '26-11-2024'}]

print(f"Исходный список заметок:\nnotes = [\n{notes[0]}\n{notes[1]}\n{notes[2]}\n]")


print(search_notes(notes, keyword="СПИСОК"))

