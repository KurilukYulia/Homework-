import time
from home21 import Auto


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color='black', weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        super().move()
        print('attention')

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed,color='black', weight=None):
        super().__init__(brand, age, mark,color,weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'max_speed is {self.max_speed}')


truck_1 = Truck('Mercedes', 2019, 'E-laass', 80)
print(truck_1.__dict__)
truck_1.move()
truck_1.stop()
truck_1.birthday()
truck_2 = Truck('BMW', 2018, 'X5', 70)
print(truck_2.__dict__)
truck_2.move()
truck_2.stop()
truck_2.birthday()
truck_2.load()
car_1 = Car('Mercedes', 2019, 'E-laass', 180)
print(car_1.__dict__)
car_1.move()
car_1.stop()
car_1.birthday()
car_2 = Car('BMW', 2018, 'X5', 200)
print(car_2.__dict__)
car_2.move()
car_2.stop()
car_2.birthday()
