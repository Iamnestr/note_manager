# Создаем список заголовков заметки
titles = []
range_ = 0
while True:
    title = str(input('Введите заголовок заметки (или оставьте пустым для завершения): '))
    if bool(title) == False:
        break
    range_ += 1
    titles.append(title)

# Выводим все заголовки
print('\nЗаголовки заметки:')
for i in range(range_):
    print("-", titles[i])

