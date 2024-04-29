# def example_function(a="closure "):
#     def nest_function(b):
#         print(a * b)
#     return nest_function
#
# alias_for_exp = example_function('eee-')
# alias_for_exp(4)


# def sound_decorator(func_as_param):
#     def nested():
#         print('~hau~hau~hau~')
#         func_as_param()
#         print('~hau~hau~hau~')
#
#     return nested

#
#
# @sound_decorator(30)
# def quote_pet():
#     print("Pies to najlepszy przyjeciel człowieka")
#quote_pet()


# from typing import Iterable
# def get_something(seq: Iterable) -> str:
#
#     text = ""
#     for i in seq:
#         text += f'~ {i}'
#     return text
#
#
# print(get_something([1,2,3]))
# print(get_something(('a', 'ala', 'b')))
# print(get_something("abcdefg"))

def print_example(poz1, poz2, poz3):
    pass

def print_example(*args):

    for argument in args:
        print(argument, end=" ~ ")
    print()
    print('-----------------------')


print_example('ela', 13, 'hahaha')
print_example(1)
print_example(1,2,3,4,5,6,7,8,9)

def print_example(age, num):
    print(f'AGE: {age}, NUM {num}')


print_example(num=3, age=5)

def grant_bonus(name, surname, salary_base=4200, bonus=0):
    print(f'Employee {name} {surname} gets {salary_base} PLN + bonus: {bonus}')


grant_bonus('Jan', 'Kowalski', bonus=5000, salary_base=6000)

def grant_bonus(*args, **kwargs):
    print('args:')
    for a in args:
       print(a)
    print('kwargs')
    for key, value in kwargs.items():
        print(key, '-', value)


grant_bonus('Jan', 'Kowalski', bonus=5000, salary_base=6000)