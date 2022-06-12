# Вам необходимо найти в папке main все директории, в которых есть хотя бы
# один файл с расширением ".py". Ответом на данную задачу будет являться файл
# со списком таких директорий, отсортированных в лексикографическом порядке.

import os

answer = []

# Поиск всех необходимых директорий
for current_dir, dirs, names in os.walk('main'):
    for name in names:
        if '.py' in name and current_dir not in answer:
            answer.append(current_dir)

# Запись ответа в файл
answer.sort()
with open('2.4_os.txt', 'w') as file:
    for line in answer:
        file.write(line + '\n')
