class String(str):
    def __init__(self, value):
        self.value = str(value)

    def __add__(self, other):
        if isinstance(other, (int, float, str, list, tuple)):
            return String(str(self.value) + str(other))
        elif isinstance(other, String):
            return String(str(self.value) + other.value)
        else:
            return self

    def __sub__(self, other):
        if not isinstance(other, str):
            other = str(other)
        if other in self:
            return String(self.replace(other, '', 1))
        else:
            return self


print(String('New day') + 7)
print(type(String('New day') + 7))
print(String('New ') + 'day')
print(type(String('New ') + 'day'))
print(String('New') + True)
print(type(String('New') + True))
print(String('Type') + None)
print(type(String('Type') + None))
print(String(789045) + 9)
print(type(String(789045) + 9))
print(String('New') + ['s', ' ', 23])
print(type(String('New') + ['s', ' ', 23]))

print('-' * 50)

print(String('Ne7w day') - 7)
print(String('New day') - 'd')
print(String('New day') - 'new')
print(String('pineapple apple pine') - 'apple')
print(String('New day') - 'apple')
print(String('NoneType') - None)
print(String(789045) - 9)
