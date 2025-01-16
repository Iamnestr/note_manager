filename = 'corrupted_file.yml'
try:
    with open(filename) as file:
        print(file.read())
except FileNotFoundError:
    print(f'Файл {filename} не найден. Создан новый файл')
    file = open(filename, 'x')
except UnicodeDecodeError:
    print(f'Не удалось декодировать файл {filename}')
except PermissionError:
    print('Ошибка доступа')
except Exception as e:
    print(f"Ошибка: {e}")
finally:
    print('Проверка ошибок проведена')
