class Car:
    FUEL_TYPES = ['gasoline', 'diesel', 'electric', 'hybrid']
    COLORS = []
    NUMBER_OF_CARS = 0


    def __init__(self, model, year, color, fuel_type):
        self.model = model
        self.year = year
        self.color = color
        self.flue_type = self.is_valid_fuel_type(fuel_type,Car.FUEL_TYPES)
        Car.NUMBER_OF_CARS+=1
        self.number = Car.NUMBER_OF_CARS
        if color not in Car.COLORS:
            Car.COLORS.append(color)

    @property
    def numbers(self):
        range(Car.NUMBER_OF_CARS)
    @staticmethod
    def is_valid_fuel_type(fuel_type,flue_types):
        if fuel_type  in Car.FUEL_TYPES:
            return fuel_type
        else:
            return Car.FUEL_TYPES
    @classmethod
    def get_used_colors(cls):
        return len(cls.COLORS)
    @classmethod
    def get_numbers_of_cars(cls):
        return cls. NUMBER_OF_CARS





car_1 = Car('Mercedas', 1980, 'дизель', 'black')
car_2 = Car('BMW', 2000, 'бензин', 'white')
car_3 = Car('Tesla', 2021, 'електрикаcccc', 'black')
print(car_1.__dict__)
print(car_2.__dict__)
print(car_3.__dict__)
print('COLORS:', Car.get_used_colors())
print('NUMBER_OF_CARS:', Car.get_numbers_of_cars())

