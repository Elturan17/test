'Comprehension'
# a = a + a -> a += 1 
 
# генерация последовательностей в одну строчку используя цикл for, также называют синтаксическим сахаром 


"синтаксис"
# 1. результат for элемент in итерируемый обьект 
# 2. результат for элемент in итерируемый обьект if фильтр 

"""list comperehension"""

# 1 - 10 -> * 2 



# list_ = []
# for i in range(1, 11):
#     list_.append(i*2)
# print(list_)

# list_ = [i*2 for i in range(1, 11)]
# print(list_)



# imropt time: 


# start_time = time.time()
# list_2 = []
# for i in range(100):
#     list_2.append(i)
# time1 = time.time() - start_time

# start_time1 = time.time()
# list_3 = [i for i in range(100)]
# time2 = time.time()- start_time1

# print(time1, time2)  

"мсосздать список честные числа от 1до 10"
# number = [i for i in range(1, 11)if i%2 == 0]
# print(number)  

"hello 1 10 "

# list_ = ['hello' for i in range(10)]
# print(list_) 

# list_ = [input() for i in range(5)]
# print(list_) 

"""Если в условии есть else, то все пишется до for"""

# list_ = ['четное' if i%2==0 else 'нечетное' for i in range(1, 11)]
# print(list_) 

# list_1 = [1, 'hello', 3, 'a', 4, 7, 2.0, 'hw']
# 'четное' "нечетное"
# list_2 = ['нечетное' if i%2 else 'четное' for i in list_1 if type(i)== int or type(i)==float]
# print(list_2)

"""set comprehension"""
# set_ = {i for i in range(10)}
# print(set_) 

# list_ = [1, 1, 2, 3, 2, 4, 5, 5, 6]
# set_ = {i for i in list_}
# print(list_)

"""dict comprehension"""
# создается аналогично set и list comprehension, только дополнительным требованием - определение ключа:

# dict_ = {i: i*i for i in range(10)}
# print(dict_) 

#  list_ = [1, 2,, 3, , ,4]
# d = {i:list_.count(i) for i in list_}
# print(d)

# d = {'a':2, 'c':3}
# dict_ = {k:'четное' if v%2 == 0 else 'нечетное' for k, v in d.items()}
# print(dict_)  

# d = {i: str(i) for i in range(1, 11)}
# print(d) 

"""второго списка"""
# list_1 = [1, 2, 3, 4, 5]
# list_2 = ['a', 'b', 'c', 'd', 'e']

# dict_ = {list_1[index]:list_2[index] for index in range(len(list_1))}
# print(dict_) 

# dict_ = {'a': 1, 'b':2, 'c':3}
# # dict_2 = {k:v for k, v in dict_.items()}
# # print(dict_2) 
# dict_2 = {v:k for k, v in dict_.items()}
# print(dict_2)

"дан словарь, где значения - список с числами, создайте новый словарь, где значения - сумма тех чисел"
# dict1 = {"a":[1,2,3,4,5],
#          "b":[10,30,2,5],
#          "c":[74,28,47], 
#          "d":[4,6,2,92,9 ]
#          }


# dict_2 = {key:sum(value) for key, value in dict1.items()}
# print(dict_2) 


"""Вложенные comprehensions"""


# dict_ = {i:list(range(i+1)) for i in range (1, 6)}
# print(dict_)

# [['hello'], ['hello']]
# list_ = [['hello' for i in range(5)] for i in range(10)]
# print(list_)

# employees = {
#     'id1': {
#         'first name': 'Александр',
#         'last name' : 'Иванов',
#         'age': 30,
#         'job':'программист'
#             },
#     'id2': {
#         'first name': 'Ольга',
#         'last name' : 'Петрова',
#         'age': 35,
#         'job':'ML-engineer'
#     } 
# }
# for info in employees.values(): 
#     for k, v in info.items(): 
#         if k == 'age':
#             info[k] == float(v)
#             print(employees) 
"""Вставим второй dict comprehension в первый вместо переменной info. Напомню, info — это значения внешнего словаря, которые сами по себе являются словарями. Именно к ним мы и применим второй dict comprehension."""
# dict_ = {id:{k:(float(v) if k == 'age' else v) for k, v in info.items()} for id, info in employees.items()}
# print(dict_)


# {k:(float(v) if k == 'age' else v) for k, v in info.items()}




















name_of_list = int(input('helloworld'))
