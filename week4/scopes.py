"""Области видимости и постранство имен"""
# область видимости определяет, когда и где мы можем использовать свои переменные или функции.

"""Существует 4 постранства имен:"""

# 1. builtints(встроенное п. и.) -> (print, input, sum, int...)

# 2. Global (глобальные п. и.) -> все переменные и функции, которые мы создаем внутри файла 
# a = 10
# # 3. enclose(не локальным/замкнутое п. и.) -> пространство между двумя постранствами 
# # 4. local (локальное п. и.) -> переменный и функции внутри функций 
# print(dir(_builtins_)) # -> возвращает список встроенных классов обиьектов и функций

# num = 10
# b = 'Hello'
"""globals() -> возвращает все глобальные переменные в типе данных словаря. ключ = название переменой, значение - обьект"""
# print(globals())
# локальное перенные -> переменные в функциях 
# def func():
#     x = 100
#     print(x) 
# # print(x)

"""locals() -> возвращает словарь со всеми локальным переменными"""

# def func():
#     a = 10 
#     print(locals())

# func()
# # print(locals()) # -> когда применяем на глобальном уровне, то она возвращает глобальные переменные 

"""enclose -> возникает только в тех случаях, когда есть вложенность в функциях"""

# x = 'глобальная'

# def some_func():
#     x = 'это enclose переменная'
#     def some_func_2():
#         x = 'локальная переменная'
#         print(x)
#         print(locals())
#     some_func_2()
#     print(locals())
# some_func_()
# # print(x) 

'''LEGB -> local -> enclose -> global -> builtint'''

# import this -> краткий гайд по Дзен Питону 

# list_ = [1, 2, 3, 4]

# def func():
#     list_[0] = 0



"""global -> позволяет менять значение глобально переменной, находясь в локальной области видимости"""

# x = 0 

# def func():
#     try:
#         global x
#         print(x)
#         x +=1
#     except:
#         print('f')

# def func():
#     global x # доступ на изменение глобально переменной "x"
#     print(x)
#     x+=1
# func()
# func()
# func()

# a = 4
# def outer_function():
#     global a
#     a = 20
#     def inner_function():
#         global a
#         a = 30
#         print('inner a =', a)
#     inner_function()
#     print('outer a = ', a) 

# outer_function()
# print(a)  

"""nonlocals - доступ на чнение и изменение локальных переменных"""

# def func():
#     a = '1'
#     print(a)
#     def inner_func():
#         nonlocal a 
#         a = 1
#         print(type(a))
#     inner_func()
#     print(type(a))

# func() 

"""
1. Изнутри функции мы видим переменные, которые определены и внутри и снаружи 
"""
"""
2. Снаружи функци не видны переменные определенные внутри функции 
"""
"""
3. Изнутри функции можно изменить глобальную переменную с помощь. global
"""
"""
4. Внутри вложенной можно изменить значение не локальной переменной с помощью nonlocal, но глобальные нельзя!
"""

# def counter():
#     num = 0
#     def add_():
#         nonlocal num
#         num+=1
#         return num
#     return add_
   
# c = counter()
# c1 = counter()
# c2 = counter() 
# print(c())
# print(c())
# print(c()) 

# def counter(i):
#     counter = 0
#     def add():
#         nonlocal counter
#         print(counter)
#         counter+=1
#     for x in range(i):
#         add()

# counter(5) 












list_ = []
for i in range(1, 50):
    print(i)
