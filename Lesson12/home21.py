def move():
    print('move')


class Auto:
    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1
        print(self.age)


auto_1 = Auto('Mercedes', 2019, 'E-Class')
print(auto_1.__dict__)
auto_1.move()
auto_1.stop()
auto_1.birthday()