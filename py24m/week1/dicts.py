"""Тип данных Словари (dict())"""
# {'key':'value'}

# dict() - изменяемый, неиндексируемый, итерируемый, упорядоченный 

# литералы - {}
# hello = привет 
# синтаксис: {key:value}

# dict_ = {}
# print(type(dict))

# ключи должны быть уникальными 
# ключами в словарях могут быть только неизменяемым типы данных
# значениями в словаре могут быть любые типы данных 

# dict_ = {'one': 1, 2: 'two'}
# print(dict_['one']) 
# если такого ключа нет - КeyError 

# dict_ = {[]: 1} ошибка 


"""Создание словарей"""
# 1 -> {}
# dict_ = {'name': 'john', 'age': 25, 'hobby': ['football', 'swimming']}
# print(dict_['hobby']) 
# dict_['hobby'][1] = 'driving' 
# print(dict_ )  

# 2. dict()
# dict_ = dict([('hello', 'world'), ('name', 'Zhanat')]) 
# print(dict_) 

# a = dict(['ab', 'cd'])
# print(a) 
# print(type(a))

# a = dict(short = 'ds', name = 'smsvsv')
# print(a) 


"""Методы словарей"""
# clear() -> очищает словарь
# dict_ = {'name': 'john', 'age':25, 'hobby':['football', 'swimming']}
# dict_.clear()
# print(dict_)

# import copy 
# lis = [1, 2, 3, [0, 2, 3]]
# # copy() -> возвращает копию словаря 
# # dict2 = dict_.copy()
# # dict2 = copy.deepcopy(dict_)
# # dict2['hobby'][0] = 'hhh'
# # print(dict_)
# # print(dict2_)
# # l1 = lis.copy()
# l1 = copy.deepcopy(lis)
# lis[2]
# print(lis) 


# fromkeys(seq, value) -> создает словари, гле ключи будут элементы из seq? а значением value не укащать,то оно будет None по умолчанию)

# list_ = [1, 2, 3, 4]
# dict_ = dict.fromkeys(list_, 100)
# print(dict_)

"""Получение элементов из словаря"""
# get(key, message) -> возвращает значение по ключи, но если ключа нет - выдает None (если указан message - выдает его)
# dict_ = {'name': 'john', 'age': 25, 'hobby': ['football', 'swimming']}
# print(dict_.get('n', 'No such key'))

# print(dict_['name']) # выдает ошибку, если ключа нет 

"""изменение эл-во словаря"""
# dict_ = {'name': 'john', 'age': 25, 'hobby': ['football', 'swimming']}
# dict_['name'] = 'Zhanat'
# print(dict_)  

# update(английскому языку и литературе через запятую: new_dict) -> добавляет new_dict в наш словарь 
# dict_ = {'name': 'john', 'age': 25, 'hobby': ['football', 'swimming']}
# d = {'last name':'mmm'} 
# dict_.update(d)
# print(dict_) 


# setdefault(key, defaul_value) -> Работает как get(), но если ключа нет - создает новую пару (если не указать defaul_value - значение будет None)

# dict_ = {'name': 'john', 'age': 25, 'hobby': ['football', 'swimming']}

# # 1. Способ 
# # print(dict_.setdefault('name', 1)) 

# # 2. Способ 
# dict_.setdefault('last_name', 'd')
# print(dict_)  



# values() -> вызвращает все значение, которые есть в словаре 

# dict_ = {'name': 'john', 'age': 25, 'hobby': ['football', 'swimming']}
# values_ = dict_.values()
# print(values_) 

# keys() -> возвращеат все ключи словаря 
# print(dict_.keys())

# dict_ = {'name': 'john', 'age': 25, 'hobby': ['football', 'swimming']}


# # items() -> возвращает все пары в словаре 
# print(dict_.items()) 



# pop(key, message) -> удаляет пару ключ и значение - возвращает значение (если ключа нет, выдает ошибку, но если есть  message - возвращает его)


# dict_ = {'name': 'john', 'age': 25, 'hobby': ['football', 'swimming']}
# p = dict_.pop('name')

# # print(p)
# print(dict_)  


# popitem() -> удаляет и влзвращает пару ключ и значение (удаляет с конца) 

# dict_ = {'name': 'john', 'age': 25, 'hobby': ['football', 'swimming']}
# dict_.popitem() 
# print(a) 
# print(dict_)




# n = 123457897654

# l = 0 
# sum = 0 
# while l < len(str(n)):
#     print(str(n)[l])
#     sum = sum + int(str(n)[l])
#     l +=1 
# print(sum)

# list_ = [1, 2, 3]
# for i in list_:
#     print(i)
#     list_.append(i)


"""Ключевые слова в циклях"""
# break - полностью выйти из цикла, досрочно прерывает цикл 
# continue -> перейти к следующей итерации 
# оператор continue начинает следующей проход цикла, минуя оставшуюся часть тела цикла 


# for i in range(10):
#     print(i)
#     if i == 3:
#         break 


# for i in range(11):
#     if i == 3:
#         continue 
#     print(i)




# while True: 
    #   print(1)
    #   continue 


# i = 0 
# while i < 6: 
#     i+=1
#     if i == 4: 
#         print('пропускаем 4')
#         continue 
#         print('Это никто не увидит')

#     print('Текущее значение:', i)    


"""else"""
# Слово else, применненое в циклах, проверяет, был ли произведен из цикла оператором break, или "естественным" образом 

# блок кода внутри else будет выполняться в том случае, если выход из цикла произошел без помощи break 


# for i in 'hello world':
#     print(i)
#     if i == 'a': 
#         break 
# else:
#     print('Буквы "a" нет')


"""Итерирование словарей"""





#     print(a, b, c) 



# a = {'a': 1, 'b': 2, 'c': 1}
# for i in dict_:  
#     print(i)
# print(dict_.items())
# for i in dict_.items():  
#     print(i)  

GREEN CARD'===================================
DV-2024 Submission Confirmation: Entry Received

Success!

Your entry for the 2024 Diversity Visa program was received on
Tuesday, November 8, 2022 at 1:01:44 AM EST. Please do NOT close this
window until you have printed this confirmation page or made a record
of your Confirmation Number.

Entrant Name:
DAVLETALIEVA, FATIMA
Confirmation Number:
2024A59VGHHIWRNX
Year of Birth:
1975
Digital Signature:
7381C0E8539659644853E20C86138FD024DF2F87

Thank you for your entry for the 2024 Diversity Visa Program.

Please either print this page or make a record of the confirmation
number before closing this window. You will not be able to retrieve
this number after you close this window.

You must retain your confirmation number in order to check your entry
status via Entrant Status Check between May 6, 2023 and September 30,
2024 to determine whether your entry was selected for further
processing in the 2024 Diversity Visa Program. You will be REQUIRED to
enter your confirmation number in combination with other personal
information in order to check on your entry status.

Selectees will not receive selectee notifications or letters by
regular postal mail from the Kentucky Consular Center (KCC).

Do not submit additional Entry Forms with this person as the Primary
Entrant! Multiple entries will disqualify the Entrant from
participation in the 2024 Diversity Visa Program.

GREEN CARD
DV-2024 Submission Confirmation: Entry Received

Success!

Your entry for the 2024 Diversity Visa program was received on
Tuesday, November 8, 2022 at 12:57:17 AM EST. Please do NOT close this
window until you have printed this confirmation page or made a record
of your Confirmation Number.

Entrant Name:
NIIAZBEKOV, ELTURAN
Confirmation Number:
2024A57HOTVFYQ3B
Year of Birth:
2004
Digital Signature:
C1A6B436F9AF09865F2B5F695AE2C8877D2A3393

Thank you for your entry for the 2024 Diversity Visa Program.

Please either print this page or make a record of the confirmation
number before closing this window. You will not be able to retrieve
this number after you close this window.

You must retain your confirmation number in order to check your entry
status via Entrant Status Check between May 6, 2023 and September 30,
2024 to determine whether your entry was selected for further
processing in the 2024 Diversity Visa Program. You will be REQUIRED to
enter your confirmation number in combination with other personal
information in order to check on your entry status.

Selectees will not receive selectee notifications or letters by
regular postal mail from the Kentucky Consular Center (KCC).

Do not submit additional Entry Forms with this person as the Primary
Entrant! Multiple entries will disqualify the Entrant from
participation in the 2024 Diversity Visa Program.



