# Напишите реализацию функции closest_mod_5, принимающую в качестве
# единственного аргумента целое число x и возвращающую самое
# маленькое целое число y, такое что:
# y больше или равно x
# y делится нацело на 5

# С помощью математики
def closest_mod_5_math(x):
    b = 5
    y = ((x + b - 1) // b) * b
    print(y)

# Через цикл
def closest_mod_5_while(x):
    while x % 5 != 0:
        x = x + 1
    print(x)

x = int(input())
closest_mod_5_while(x)
closest_mod_5_math(x)
