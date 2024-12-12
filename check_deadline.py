# Определяем текущую дату
from datetime import datetime
current_date = datetime.today().strftime('%d-%m-%Y')
print("Текущая дата:", current_date)
date_format = "%d-%m-%Y"
date_1 = datetime.strptime(current_date, date_format)
format_ = True

# Вводим дату дедлайна заметки и проверяем корректность ввода.
while format_ == True:
    issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")
    try:
        date_2 = datetime.strptime(issue_date, date_format)
        format_ = False
    except ValueError:
        print("Формат даты не верный. Попробуй еще раз.")

# Сравниваем дату дедлайна заметки с текущей датой.
if date_2 < date_1:
    date_difference = date_1 - date_2
    print(f"Внимание! Дедлайн истёк {date_difference.days} д. назад.")
elif date_2 > date_1:
    date_difference = date_2 - date_1
    print(f"До дедлайна осталось {date_difference.days} д.")
else:
    print("Дедлайн сегодня!")
