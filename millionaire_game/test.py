class Example:
    def __init__(self, name):
        self.name = name

    def __str__(self): # __repr__
        return f'Jestem obiektem, a moje imie to: {self.name}'


obj_ex = Example('kubek')
print(obj_ex)