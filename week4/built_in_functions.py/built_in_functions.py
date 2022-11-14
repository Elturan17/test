






















# res = lambda a, b, c: (a*b)%c
# print(res(2, 6, 4))

# dict_ = {1:'sd', 2:'gf', 3:'as'}
# get_keys  = lambda x: x.keys()
# print(get_keys(dict_))

# list_ = [1, 2, 3, 4, 'fd', 'asdf']
# last_el = lambda x: x[-1]
# print(last_el(list_))



# map(function, iteration) -> функция принимает первым аргументом функцию, вторым отерируемый обьектом. Она применяет function к каждому элементу iterable 

# a = map(int, ['1', '2', '3'])
# #print(a) -> <map object> 
# print(list(a))

# int('1') -> 
# int('2') -> 
# int('3') -> 

# def square(number):
#     return number ** 2

# list_ = [1, 2, 3, 4, 5]
# # result = list(map(square, list_))
# # print(result) 

# res = list(map(lambda x: x ** 2, list_))
# print(res) 

"""map на цикле for"""
# func = lambda e: e + 1

# res = []
# for e in [1, 2, 3, 4]:
#     res.append(func(e))
# print(res) 
"filter(function, iterable)" # -> фильтрует. Если функция возвращает True 

# num = [1, 3, 4, 5, 7, 6, 9, 11]

# # def filter_nums(number):
# #     if number % 2 == 0:
# #         return True 

# # # result = list(filter(filter_nums, num))
# # print(result) 
# filter_lambda = lambda num: num % 2 == 0
# print(list(filter(filter_lambda, num)))

names = ['Жанат', 'Нурайым', 'Санжар', 'Тима', "Амалия", 'Аяна', 'Азирет', 'Айдана']

# def startswith_vowel(name):
#     vowels = 'фцжвуф'
#     return name.upper().startswith(tuple(vowels))
# # print(startswith_vowel('Andy')) 

# res = list(filter(startswith_vowel, names))
# print(res) 

# vowels = 'AASAEEAFP'
# res = list(filter(lambda name: name.upper(). startswith(tuple(vowels)), names))
# print(res)
"""filter на цикле for"""

# def startswith_vovel(name):
#     vowels = 'SAHFUAEI'
#     return name.upper().startswith(tuple(vowels))

# res = []
# for name in names:
#     if startswith_vovel(name):
#         res.append(name)

# print(res) 

"reduce(function, iterable)" # -> нужно импортировать с functools. возращает одно значение


# from functools import reduce 

# list_ = [1, 2, 4, 5, 6, 7, 8]
# result = reduce(lambda x, y: x + y, list_)
# print(result)
# res = reduce(lambda x, y: x*y, list_)
# print(res) 

# def mul(x, y):
#     return x * y

# # res = list_[0]
# # for e in list_[1:]:
# #     res = mul(res, e)
# # print(res) 

# res =1
# for e in list_:
#     res = mul(res, e)
# print(res) 

"enumerate(iterable, [start])" #-> нумерует элементы tuple-(number, element) по дефолту нумерация начинается с нуля, но можно передать с какого числа начать ([start])

list_ = ['a', 'b', 'c', 'd']

# for i in enumerate(list_):
#     print(i)

# res = list(enumerate(list_))
# print(res)

# for index, element in enumerate(list_):
#     print('index - ', index, 'element - ', element)

# res = list(enumerate(list_))
# print(res)

"zip(iterable, iterable -> *iterable)"

# соединяет две последовательности (сопостовляет каждый элемент их iterable со следующим)

# list_1 = [1, 2, 3, 4, 5]
# list_2 = ['a', 'b', 'c', 'd', 'e']
# print(list(zip(list_1, list_2)))


# list_1 = [1, 2, 3, 4, 5]
# list_2 = ['a', 'b', 'c', 'd', 'e']
# list_3 = [98, 534, 35]
# list_4 = [(1, 2), (3, 4)]
# print(list(zip(list_1, list_2, list_3, list_4)))

"изменить тип данных словаря"

# dict_ = {1:1, 2:2, 3:3}
# def conver_value(value):
#     return str(value)

# result = list(map(conver_value, dict_.values()))
# print(result)

# new_dict = dict(zip(dict_.keys(), result))
# print(new_dict)


"""заменить значения чисел в списке (четное/нечетное)"""

list_ = [1, 2, 3, 4, 5, 6, 7]
def str_(num):
    if num % 2 == 0:
        return 'четное'
    else:
        return 'нечетное'

# result = list(map(str_, list_))
# print(result) 
result = list(map(lambda x: 'четное' if x % 2 == 0 else 'нечетное', list_))
print(result) 