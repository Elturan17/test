"""Введение в функции. Позиционные и именованные аргументы. ards, kwargs. Аргумент по default.  Аннотации"""

"""Аннотации"""
# помогают сделать код информативным и избавиться от некоторых проблем с динамической типизацией 
# num: int = 10
# num = 'hello'
# num : int = 1
# num : int = 'hello' 
# a : int = 1
# b : int = 'hello'
# print(a+b)


"""==========Функции=========="""
# Функция - именованный блок кода, который выполняет одну задачу и может принимать аргументы и возвращает результаты. Функции можно использовать многократно, вызывая функцию по имени 

"""Синтаксис"""

# def <название функции>(параметры):
#     <тело функции>

# # вызов функции
# <название функции>(аргументы)

# def  print_hello():
#        print('hello')

# print_hello('hello')

# def my_sum(x: int, y: int):
#     print(x+y) 

# my_sum(10, 5)


# def my_len(obj):
#     count = 0 
#     for element in obj:
#         count += 1 #count = count + 1
#     print(count) 

# my_len([1, 2, 3, 4, 5, 6, 7])
# my_len('nvvbvaureupavre')
 

"""для чего нужны функции?"""
# чтобы код не повторялся и был универсальным 
# DRY - don't repeat yourself 

"""return"""
# return - используется для возвращения реззультата и на этом моменте функция завершает работу 


# def my_sum(x, y):
#     return x + y

# # print(my_sum(10, 56))

# z = my_sum(33, 54)
# print(z)  

"""Параметры и Аргументы"""
# Параметры - локальные переменные внутри функции, значения которым мы задаем при вызове функции


# Аргументы - значения, которые мы передаем праметрам при вызове функции

"""Виды параметров"""
# 1. обязательные
# 2. не обязательные 
#  2.1 с дефолтом (a=10)
# 2.2 args 
# 2.3 kwargs (b=11) (key word argument)

"""Ввиды аргументов"""
# 1. позиционные (по позиции)
# 2. именованные (my_sum(y=23, x=67))


# def info(name, last_name):
#     print(f'имя: {name} фамилия: {last_name}')

# info('Aiana', 'Usenova')
# info('Usenova', 'Aiana')
# info(last_name='Usenova', name='Aiana')

# def info(name, last_name, age = 18):
#     print(f'имя: {name} фамилия: {last_name} возраст: {age}')

# info('John', 'Show') # если дефолтный параметр указан, то можно передавать аргумент этому параметру 
# info('John', 'Show', 26)

"""Параметров может быть бесконечное кол-во Аргументов может быть столько, сколько параметров 
"""

"""args and kwargs"""

# *args - принимает не именнованые аргументы(все позиционные аргументы, кроме обязательных)

# **kwargs - принимает все именнованные аргументы (кроме обязательных именованных)(dict)

# def num_sum(a, b, *args, **kwargs):
#     return a+b+sum(args)+sum(kwargs.values())

# # print(num_sum(2, 3)) 
# print(num_sum(2, 6, 3, 4, 6, 7, 99))#args
# print(num_sum(5, 99, first=66, secon=55))#kwargs 

"""        *               """
# list1 = list(range(1, 11))
#print(list1)
# list2 = [*range(1, 11)]
# print(list2) 

# dict1 = {'a':1, 'b':2}
# dict2 = [*dict1]
# dict2 = {**dict1}
# print(dict2)

# list_ = ['fdgd', 'sdvfgs', 'dzsevs']
# list2 = []

# def up(a):
#     for i in a:
#         b = i.upper()
#         list2.append(b)
#     print(list2)
# up(list_)
# -> ['FDGD', 'SDVFGS', 'DZSEVS']

# list_ = [1, 2, 3, 'hello', 'world']
# # -> ['world', 'hello', 3, 2, 1]
# def rev(a):
#     a.reverse()
#     print(a)
# rev(list_)

# print(a[::-1])
# rev(list_) 

# def rev(a):
#     ls = []
#     for i in range(-1, -len(list_)-1, -1):
#         ls.append(a[i])
#     return ls 

# print(rev(list_))  

