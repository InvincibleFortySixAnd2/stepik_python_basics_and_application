# Вам дается текстовый файл, содержащий некоторое количество непустых строк.
# На основе него сгенерируйте новый текстовый файл, содержащий те же строки
# в обратном порядке.
# Пример входного файла:
# ab
# c
# dde
# ff
# ﻿Пример выходного файла:
# ff
# dde
# c
# ab

with open('2.4_open_write_files.txt', 'r') as f_in, open('test_out.txt', 'w') as f_out:
    lines = f_in.read().splitlines()
    lines = lines[::-1]
    contents = '\n'.join(lines)
    f_out.write(contents)
