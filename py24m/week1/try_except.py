"""Оборотка """




# Ошибки -> проблемы с синтаксисом 
# 1. SyntaxErr<or: (забыли двоеточие или скобочку .....)
# 2. IndentationError: (неправильный отступ )
# a = 7
# 3. TabError: неверная табуляция (смеживание пробелы и табов)



# Исключения: 
# 1. ZeroDivisionError
# 2. NameError
# 3. IndexError 
# 4. KeyError 
# 5. ImportError 
# 6. ValueError 
# 7. TypeError 
# 8. AttributeError 
# 9. BaseException (прородитель)
# 


# ZeroDivisionError # возникает при делении на 0 
# 45/0 
# 33/0
# 4%0

# NameError  # возникает, когда обращаемся к не существующей переменной 
# # print(a)

# IndexError # возникает, когда обращаемся по несуществующему индексу 
# # list_ = [1, 2, 3, 4]
# # lisr_[10]

# KeyError # когда обращаемся по несуществующему ключу 
# dict_ = {'a':1, 'b':2}
# dict_['c']

# ImportError # неправильный импорт 
# # from math import pi2 

# ValueError # когда при распаковке не совпадает кол-во переменнных и элементов, когда в функцию передаем некорректные данные 
# # a = '10c'
# int(a)

# a, b, c, = 'qb' 

# TypeError # когда пытаемся использовать методы не свойственные типу данных 
# for i in 1234567: 
#     print(i)
# '5' + 5
# {[1, 2]:9}
# [].append()

# AttributeError # вознкает, когда обращаемся к несуществующему аттриббуту или методу обьекта 
# [].replace('a', '')
# ''.pop(0)

"""Обработка исключений """
# операторы: try except 

# try: 
#     # код, который может вызвать ошибку 

# except (название ошибки, которая может возникнуть)::
#     # код, который сработает, если в try выщла ошибка 
# try:
#     age = int(input('Введите ваш возраст: ')) 
#     print(age) 
# except ValueError: 
#     print('нужно ввести число')

# try:
#     raise NameError
# except:
#     print('была обработана ошибка') 

# raise -> Исскуственно вызывает ошибку 

# n = int(input())
# if n <= 0:
#     raise 'Значение не может быть равным или меньше 0 '
# print(n) 

# a = 10 
# b = 0 
# try:
#     a/b 
# except ZeroDivisionError: 
#     print('на 0 делить нельзя!!!')


# try: 
#     int('k')
# except ValueError:
#     print('неверный ввод')
#     try:
#         3/0
#     except ZeroDivisionError:
#         print('на ноль делить нельзя!!')

"""Попытайтесь в блоке try ввести 2 числа 'num1', 'num2', распеччатав деление их между собой. В блоке except обработайте сразу 2 возможных исключения и распечатайте 'Произошла ошибка'"""
# try:
#     num1 = int(input('введите число: '))
#     num2 = int(input("введите число "))
#     print(num1/num2)

# except (ValueError, ZeroDivisionError):
#     print('Произошла ошибка')


# try:
#     num1 = int(input('введите число: '))
#     num2 = int(input("введите число "))
#     print(num1/num2)
# except ValueError:
#     print('введите числа')
# except ZeroDivisionError:
#     print('на ноль делить нельзя')


"""else в обработке исключений"""

# dict_ = {'a':3, 'b':2, 'c':1}
# try:
#     k = input('Enter: ')
#     dict_[k]
# except KeyError: 
#     print('такого ключа нет')
# else:
#     print('ошибки не было') 

# в блоке else - код сработает, если в try не вышла ошибка 


"""оператор finally"""

# try:
#     код, может вызвать ошибку 
# except ошибка: 
#     код, если в try ошибка 
# else: 
#     код, код сработает, если в try не вышла ошибка
# finally:
#     код, который сработает в любом случае 

# try: 
#     res = a * 2 
#     print(res) 
# except NameError: 
#     print('a не определена')
# finally:
#     a = 5
#     res = a * 2 
#     print(res, 'Блок finally') 


"""Exception as e"""
# try:
#     a = int(input())
#     a1 = int(input())
#     print(a/a1)
# except Exception as error: 
#     print('общее исключение', error._class_) 

# error._class_ -> показывает класс ошибки 


# import sys 
# list_ = [1, 2, 3, 4]

# try:
#     index = int(input())
#     res = list_[index]
#     print(res)
# except:
#     print(sys.exc_info()[0]) 


# Exception as e -> отлавливает все ошибки + мы их записываем в переменную "e"

# try:
#     if 2 > 1: 
#         raise ValueError 
# except:
#     print('oops') 

# fruits = {'apple': 32, 'banana': 80, 'tangerin': 65}
# print(sum(fruits.values()))

# res = {k: v for k, v in fruits.items() if v % 2 != 0}

# copy_fruits = fruits.copy()
# for fruit, price in copy_fruits.items():
#     if price % 2 == 0:
#         fruits.pop(fruit)
# print(fruits)


# name = {'id': {'name': 'Vasya', 'exp': {'teacher': 4, 'it': 2, 'engineer': 10}}}

# name['id'] # {'name': 'Vasya', 'exp': {'teacher': 4, 'it': 2, 'engineer': 10}}
# name['id']['exp'] # {'teacher': 4, 'it': 2, 'engineer': 10}
# name['id']['exp']['it'] # 2 




# name_of_friends = ['hello', 'world', 'python', 'makers', 'bootcamp']
# elturan = []
# for name in name_of_friends:
#     elturan.append(name)
# print(elturan)
# a = {'a':1, 'b':2}
# for i in a.items():
#     print(i)   

# labels = ['Honda', 'Kawasaki']
# for a in labels:
#     print('I like brand', a) 
