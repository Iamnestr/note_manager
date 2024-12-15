# Удаление заметок
# Сохраненные заметки
note_1 = {'Имя': 'Алексей', 'Заголовок': 'Список покупок', 'Описание': 'Купить продукты на неделю'}
note_2 = {'Имя': 'Мария', 'Заголовок': 'Учеба', 'Описание': 'Подготовиться к экзамену'}
note_3 = {'Имя': 'Алексей', 'Заголовок': 'Учеба', 'Описание': 'Оно мне надо)'}
notes = [note_1, note_2, note_3]
notes_del = []
caunt = 3 # кол-во заметок
caunt_del = 0 # кол-во заметок для удаления

# Отображаем текущие заметки:
print('Текущие заметки:')
for i in range(caunt):
    print(f"{i+1}.", end=' ')
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
        print ('Успешно удалено. Остались следующие заметки:')

        # Вывод обновленного списка
        for j in range(caunt):
            print(f"{j + 1}.", end=' ')
            note = notes[j]
            for key, value in note.items():
                print(f"{key.capitalize()}: {value}")
    else:
        print('Заметки не удалены.')


