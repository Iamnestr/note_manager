# Сохраненные заметки
note_1 = {'Имя': 'Алексей', 'Заголовок': 'Список покупок', 'Описание': 'Купить продукты на неделю'}
note_2 = {'Имя': 'Мария', 'Заголовок': 'Учеба', 'Описание': 'Подготовиться к экзамену'}
notes = [note_1, note_2]
caunt = 2 # кол-во заметок
note_faund = True # для определения результата поиска

# Отображаем текущие заметки:
print('Текущие заметки:')
for i in range(caunt):
    print(f"{i+1}.", end=' ')
    note = notes[i]
    for key, value in note.items():
        print(f"{key.capitalize()}: {value}")

# Пользователь вводит критерий для удаления:
delete = input('\nВведите имя пользователя или заголовок для удаления заметки: ')

#  Поиск и удаление заметки соответствующей критерию
for i in range(caunt):
    note = notes[i]
    if (note['Имя'].casefold() == delete.casefold() or
            note['Заголовок'].casefold() == delete.casefold()):
        notes.remove(note)
        caunt -= 1
        note_faund = False
        break

# Если заметок по критерию не найдено
if note_faund:
    print('Заметок с таким именем пользователя или заголовком не найдено')

# Вывод обновленного списка
else:
    print ('Успешно удалено. Остались следующие заметки:')
    for j in range(caunt):
        print(f"{j + 1}.", end=' ')
        note = notes[j]
        for key, value in note.items():
            print(f"{key.capitalize()}: {value}")

