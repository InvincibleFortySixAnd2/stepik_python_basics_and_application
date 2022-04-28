# Класс MoneyBox, для работы с виртуальной копилкой. Каждая копилка имеет
# ограниченную вместимость. Класс должен поддерживать информацию о
# количестве монет в копилке, предоставлять возможность добавлять монеты
# в копилку и узнавать, можно ли добавить в копилку ещё какое-то
# количество монет, не превышая ее вместимость.

class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.money = 0

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        if (self.money + v) > self.capacity:
            return False
        else:
            return True

    def add(self, v):
        # положить v монет в копилку
        if self.can_add(v):
            self.money += v
            print(f'Сейчас в копилке: {self.money}')
        else:
            print(f'Невозможно добавить {v} денег в копилку')


x = MoneyBox(100)
print(f'Вместимость копилки: {x.capacity}')
x.add(2)
x.add(2)
x.add(2)
x.add(2)
x.add(2)
x.add(80)
x.add(80)
