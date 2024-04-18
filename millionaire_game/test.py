class Example:
    def __init__(self, name):
        self.name = name

    def __str__(self): # __repr__
        return f'Jestem obiektem, a moje imie to: {self.name}'


obj_ex = Example('kubek')
print(obj_ex)

print(obj_ex.__class__.__name__)
if obj_ex.__class__.__name__ == 'Exmple':
    print('Prawda!')


# number = 3.0
# print(isinstance(number, float))

print(isinstance(obj_ex, int))