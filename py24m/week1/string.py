#el Case -> helloworld 

"""Строки(str))"""
# Строки - неизменямые тип данных, предназначены для хранения текста, заключаются в одинарные или двойные кавычки

# Син# Python - является динамически типизированным языком (Он определяет тип данных переменной исходя из значениия которое ей присвоено)

# 'строка с одинарной кавычкой'
# string2 = "строка с двойной' кавычкой"
# string3 = 'так делать нельзя"
# внутри двойных кавычек все одинарные- просто символы и наоборот 

# string4 = 
# Alt + Z -> сместить код 
 
# Название Переменных 
# 1. имя переменной не может начинаться с цифры 
# 2. нельзя использовать зарезервированные слова 

# 3. имя не может содержать спец символы (@.%,&...) Можно использовать '_'

# Snake Case -> hello_world 
# Camтаксис: 



#string1 ="""Многострочный текст,тут можно ставить любые кавычки"""

# Множественное присваивание 
# z, x, y, = 1, 4, 5 

# len() -> возвращает длину строки (кол-во символов в строке) 

# str_ = 'hello'
# print(len(str_))

"""Экранированные последовательности""" 
# это последовательности, которые начинаются с символа '\' за которым следует один или более символов 

"""Экранизация строк"""
# спец символы 
'\n'# перенос на новую строку
# str_ = 'hello\n'
# num = 4
# print(str_*num)
# умножение строки на число -> дублирование строк 

# 2. '\t' -> табуляция 
# str_ = 'hello\tworld'
# print(str_) 

 
# 3. '\\' -> отображение '\' 
# print('чтобы экранировать нужен \\') 

# 4. '\'' -> отображение "'"
# print('Don\'t') 

# 5. "\"" -> отображение '"'

# 6. '\r' -> возвращает каретку в начало строки 

# print('Hello, my name is \rhhhh')

# 7. '\v' -> перенос на новую строку со смещением вправо на длину предыдущей строки 

# print('hello\vworld')

# 8. '\a' -> гудок встроенного в систему динамика  


# Конкатенация строк
# str1 = 'hello'
# str2 = 'world'
# print(str1 + ' ' + str2)

"""Форматирование строк"""
# 1. с использование % 
# 2. с использование метода .format()
# 3. Интерполяция строк (f-строки)

# %
# name = input('enter your name:')
# result = 'Hello, %s' %name 
# print(result)

# .format(переменную )
# name = input('enter your name:')
# result = 'hello, {}'.format(name)
# print(result)

#f
# name = input('enter your name: ') 
# result = f'hello, {name}'
# print(result) 


"""Методы строк"""
# print(dir('hello'))

# Методы типов данных - функция, к которой обращаемся через точку 

# Методы на is
# str.isalpha() -> проверяет состоит ли строка только из букв 

# print('hello'.isalpha())
# str.islower() -> состоит ли строка из символов нижнего регистра 
# str.isalnum() -> состоит ли строка только из цифр и букв 
# print('hello'.islower()) 

# .lower() -> Переводит строку в нижний регистр 
# str1 = "Hello"
# str2 = str1.lower()
# print(str1.lower())

# ,upper() -> Переводит строку в верхний регистр 
# str = 'hello'
# print(str1.upper())

# .title() -> делает первую букву каждого слова заглавной 

# .strip() -> убирает пробельные символы в начале и в конце строки 
# a = '   hello'
# print(a)
# print(a.strip())

# .lstrip() -> убирает пробелы в начале строки 
 
# .rstrip() -> убирает пробелы в конце строки 

# .replace(old, new, [count]) -> Меняет old  в троке на new (count - кол-ва раз)
# a = 'ha ha ha ha'
# print(a.replace('ha', 'new'))
# print(a.replace('ha', 'new', 5)) (кол-во изменений)

# .split(разделитель) -> делит строку по разделителю 
# a = 'hello world'
# print(a.split('o')) # по умолчанию делит по пробелу 

"""Индексы"""
# индекс - порядковый номер символа в строке 

# 'h e l l o' 
# 0 1 2 3 4 

"""срезы"""
# str [start:stop:step]
# a = 'hello world'
# print(a[::]) # все слово [:]
# print (a[0]) # первая элемент строки 
# print (a[-1]) # последний элемент строки [index]

# print(a[::-1]) # переворачивает строку 
# print(a[;5]) #hello 
# print(a[::2]) # через один элемент 

# print(a[3:]) # начиная с 3 индекса
# print(a[:6]) # до 6 индекса (не включая его)





'================================='
# срезы - нахождение подстроки, step по умолчанию 1
# a = 'hello world'
# print(a[1::2])
# print(a[-1]+a[1:-1]+a[0])

# endswish(substring) -> Возвращает True,если строка заканчивается на substring 
# text = 'hello world!'
# b = text.endswith('world!')
# print(b)

# startswith(substring, [start], [end])-> возвращает True, если строка начинается с substring

# b = text.startswith('world!',6)
# b = text.startswith('He')
# print(b)

# count(substring) -> Считает кол-во вхождений substring в строке
# text = 'hello world'
# b = text.count('!!')
# print(b)

# index(substring, start end) -> принимает подстроку и возвращает индекс в строке 
# text = 'hello world!'
# b = text.index('l', 5)
# text[b] = 'd'# TypeError ()
# print(text) 

# find(substring, start, end) -> аналогично index(), Разница: если substring нет в строке - возвращает -1 
# text = 'hello world1'
# b = text.find(' ') 
# print(b) 

# zfill(width) -> Делает длину строки не меньше width, по необходимости заполняет первые символы нулямия
# text = 'hello'
# print(text.zfill(10)) 

# isdigit() -> проверяет состоит ли строка из чисел 
# a = input('введите число: ')
# b = a.isdigit()
# print(b)  
# if a.isdigit():
    # print(int(a))


# isnumeric()
# isdecimal()



# 'разделитель'.join(iterable) -> соединяет строку по разделителю, которая находится в iterable 



# text = 'milk, water, bread'
# list_text.split(', ') #['milk', 'water', 'bread']

# join_ = ''.join(list_)
# print(join_) 

'========================'

# id() -> возвращает номер ячеки памяти 
# text = 'hello'
# text2 = 'hello'
# print(id(text))
# print(id(text2))
# text2 = text.replace('h', 'o')
# print(text1)
# print(text2)
# print(id(text))
# print(id(text2))

# list_ = ['hello', 'world']
# list_ [0] = 'hi'
# print(id(list_)) 


# text = 'coder' #rodec
# print(text[1:4])
# text[0]
# text[-1]
# print(text[-1]+text[1:-1]+text[0]) 

# command = "g()()()()(al)"
# a = command
# name = input('name')
# last_name = input('last_name')
# age = input('age')
# city = input('city')
# print(f'Вас зовут {name} {last_name}, Ваш возраст: {age}, Вы проживаете {city}') 6+








































'=====================================---------------------------------'

# >= - Больше или ровно 
# 5 >= 6 #False
# 5 >= 4 #True
# 5 >=



'===And, or, not==='
# 1. and - логическое и
# 2. or - логическое или 
# 3. not - логическое отрицание 

# and   используется для обьединения  
# or      логических выражений
 
  
# a = 5
# b = 6
# #True   #True
# a == 5 and b == 6 #True
# #True     #False 
# a ==5 and b == 5 #False
# a == 4 and b == 5 #False

# если хотя бы одна часть выражения False - будет False 

# если все выражения True - будет True 




# a == 5 or b == 6 #True 
# a == 6 or b == 6 #True 
# a == 7 or b == 7 #True 
# # если хотя бы одна часть выражение возвращает True - будет True 

"""отрицательный логический оператор"""
# превращает правду в ложь и ложь в правду 
# not False # True 
# not True # False 
# not a == 5 # False 
# not a == 4 # True 

# Операторы идентификации 
# 1. in -> проверяет наличие элемента 
# a = 'h'
# b = 'hello' 
# if a in b: 
#           print('Данная буква есть в строке')
# else: 
    #   print('Данной буквы нет в строке')

# 2. сравнение 
    # == -> сравнение по значению 
    # is - сравнивает по ячейке в памяти 


# a = 2
# b = 2
# print(id(a), id(b))
# print(a is b.lower())
# print(a == b.lower())

"""Boolean Type"""
# неизменяемый 
# имеет два значения True\False 

# bool() - функция, переводит в тип данных boolean 
# print(bool(1))#True 
# print(bool(0))#False
# print(bool(-277))#True 
# print(bool(''))#False


"""NoneType"""
# тип данных с одним значением None, используется для обозначения пустых значений или отсустсвия значения 
# print(bool(None)) # False 




"""Условные операторы"""
# ныжны для того, чтобы при разных входных данных код работал по разному 

# if условие:
#     тело 
    # будет работать, если условие верно 

#будет работать, если условие1 не верно 

# if условие1: 
#     тело 
#     # будет работать, если условие1 верно 
# elif условие2: 
#     тело2 
        # будет работать, если условие1 верно


# в одной конструкции мы можем использовать только один if 
# в одной конструкции мы можем использовать неограниченное кол-во elif 
# else мы можем использовать только один раз или не использовать вообще 

# age = input('age')
# if age >= 18: 
#     print('Вам есть 18, можете пройти')
# else: 
#     print('Вы не можете пройти') 


"""задача 1: четное/нечетное""" 
# number = int(input('Number: '))
# if number % 2 == 0: 
# print('четное')
# else: 
#     print('нечетное') 

# if a < 0:
#     print('-')
# elif a > 0:
#     print('+')
# else: 
#     print('0')

"""Тернарные операторы"""
# условие в одну строку 

# тело1 if условие else тело2 
# a = 6 
# res = 'hello' if a == 5 else 'bye'
# print(res) 

# num = int(input())
# res = 'четное' if num % 2 == 0 else 'нечетное'
# print(res) 






"""set() - Множества. Изменяемый, итерируемый, неиндексируемый, неупорядоченный.
Множества могут хранить в себе только неизменяемые типы данных, если используем tuple(), то в нем должны быть неизменяемые типы данных 
"""
# литералы - {}
# set1 = {1, 2, 'hello', (1, 2)}
# set2 = {1, 1, 2, 3, 2, 4}
# print(set2) 



"""Создание множества"""
# 1. set()
# a = set('hello world')
# a = set([1, 2, 3, 4])
# a = set({1:2, 6:'y'})
# print(a) 

# 2. {}
# set_ = {1, 2, 3} # нельзя помещать изменяемые типы данных 


"""Методы set"""
# add(element) -> добавляет element в множество 
# my_set = {1, 2, 3}
# my_set.add(1)
# print(my_set) 
# my_set.add(4)
# my_set.add((1, 2, 3))
# print(my_set) 

# my_set.add('hh', (1, 2, 3)) # добавляет только по одному элементу, нельзя передавать больше одного
# print(my_set)

# update(iterable) -> добавляет несколько эл-во, но не повторяет их

# my_set = {1, 2}
# # my_set.update([1, 2, 3, 4], 'hello')
# print( 
"""Удаление эл-во из множества"""
# clear() -> очищает множество
# remove(element) -> удаляет элемент, но если такого эл-та нет - выдает ошибку 
# pop() -> удаляет случайный эл-т FIFO (first in first out)
# discard(element) -> работает как remove, но не выдает ошибку, если передать не существующий эл-т

# set_ = {1, 2, 'hello', (1, 2)} 
# print(set_)
# print(set_.pop())
# print(set_)  

# set_a.difference(set_b) -> выводит элементы которые есть в set_a, но нет в set_b 
# set_a - set_b
set1 = {1, 2, 3, 6, 7}
set2 = {1, 2, 3, 4, 5}
# print(set1.difference(set2)) 
# print(set2.difference(set1))  

# set_a.symmetric_difference(set_b) -> выводит уникальные эл-ты в обоих множествах 
# set_a ^ set_b 
#print(set1 ^ set2)

# set_a.intersection(set_b) -> выводит c[j;bt эл-ты, set_a и set_b 
# set_a & set_b 

# print(set1.intersection(set2))


# union()
# copy()
# difference_update()
# intersection_update()
# symetric_difference_update()
# isdisjoint()
# issuperset() 
# issubset() 
