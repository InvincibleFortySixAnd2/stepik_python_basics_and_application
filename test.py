# Вам необходимо найти в папке main все директории, в которых есть хотя бы
# один файл с расширением ".py".Ответом на данную задачу будет являться файл
# со списком таких директорий, отсортированных в лексикографическом порядке.

import os
import os.path

content = []

for current_dir, dirs, files in os.walk('main'):
    for file in files:
        if 'py' in file:
            content.append(current_dir)
            # print(current_dir, dirs, files)


print(content)
# print(current_dir, dirs, files)
