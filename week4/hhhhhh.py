













# def func1(func):
    # #   тело
    # def inner_func():
    #     тело
    # return inner_func

"""декоратор - это функция высшего порядка, которая оборачивает другую функция для расширения ее функционала не изменяя ее кода"""

# def a():
#     print('function')


# def b(func):
#     print(f'функция - {func._name_}')
#     func() 

# (b) 

# def benchmark(func):
#     import time
#     start = time.time()
#     func()
#     finish = time.time()
#     print(f'Время выполнения функции {finish - start}')

# def loop():
#     i = 0 
#     range_number = 100000
#     while i <= range_number:
#         print(i)
#         i+=1

# benchmark(loop) 


# def decorator(func):
#     def wrapper():
#         print('Функция обертки')
#         print('Оборачиваемая функция: {}'.
#         format(func))
#         print('Выполняем обертывание функции')
#         func()
#         print('Выходим из обертки')
#     return wrapper 

# @decorator 
# def say_hello():
#     print('Hello')        
# say_hello() 

# say_hello()
# say_hello = decorator(say_hello)
# say_hello()

# """@ - синтаксический сахар - позволяет явно указать какой декоратор применить для данной функции"""

"""выражение @decorator вызывает decorator() с say_hello в качестве аргумента и присваивает имени say_hello возвращенную функцию"""

# def uppercase_decorator(func):
#     def wrapper():
#         f = func()
#         make_uppercase = f.upper()
#         return make_uppercase
#     return wrapper 

# @uppercase_decorator
# def func():
#     return 'Всем привет!'

# print(func()) 


# def benchmark(func):
#     def wrapper():
#         import time 
#         start  = time.time()
#         func()
#         finish = time.time()
#         print(f'время выполнения функции{finish - start}')
#     return wrapper 

# @benchmark
# def loop():
#     i = 0 
#     range_number = 100000
#     while i <= range_number:
#         print(i)
#         i+=1 

# loop() 

# def add_in_list():
#     range_number = 100000
#     ls = []
#     for i in range(range_number):
#         ls.append(i)
#     # print(ls)

# add_in_list() 

"""декараторы с аргумениами"""
# если мы используем аргумент в функции, то также должны добавить аргумент и в декеракторе 

# def decorator(func):
#     def wrapper(arg1):
#         print(f'I got {arg1}')
#         func(arg1)
#     return wrapper 

# @decorator
# def func1(word):
#     print(f'He said a word {word}')

# func1('No')

"""универсальный декоратор"""

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f'args - {args}')
#         print(f'kwaargs - {kwargs}')
#         func(*args, **kwargs)
#     return wrapper 
# @decorator
# def func_without_params():
#     print('function without params')

# func_without_params() 
 

# def func_with_params(first, second):
#     print('function with params')
#     print(f'params: {first} {second}')

# func_with_params('word', 2) 

# def smart(func):
#     def wrapper(a, b):
#         print('Функция обертки')
#         if b == 0:
#             print('На 0 делить нельзя')
#             return 
#         return func(a, b)
#     return wrapper


# @smart
# def division(a, b):
#     return a/b 

# print(division(9, 0)) 

# def decorator(num):
#     def inner_decor(func):
#         def wrapper():
#             for i in range(num):
#                 func()
#         return wrapper
#     return inner_decor


# @decorator(3)
# def hello():
#     print('hello world')

# hello() 

"""====================="""

# def div(func):
#     def wrapper():
#         return '<div>' + func() + '</div>'
#     return wrapper 

# @div
# def func():
#     return 'Питониски в тесте'
# print(func())