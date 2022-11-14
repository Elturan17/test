# import random

# name = input('Введите свое имя: ')
# answer = input('Хотите поиграть? да/нет: ')
# i = 0
# while i ==0:
#     if answer == 'да' or answer == 'Да':
#         num = random.randint(0, 10)
#         print(num)
#         j = 0
#         count = 0
#         while j==0:
#             user_num = input('Введите число от 1 до 10: ')
#             if user_num.isdigit():
#                 user_num = int(user_num) 
#                 if user_numport random

# name = input('Введите свое имя: ')
# answer = input('Хотите поиграть? да/нет: ')
# i = 0
# while i ==0:
#     if answer == 'да' or answer == 'Да':
#         num = random.randint(0, 10)
#         print(num)
#         j = 0
#         count = 0
#         while j==0:
#             user_num = input('Введите число от 1 до 10: ')
#             if user_num.isdigit():
#                 user_num = int(user_num) 
#                 if user_num == num:
#                     answer = input(f'Вы угадали за {count+1} n попыток \nХотите поиграть еще?:')
#                     j = 1 
#                 elif user_num != num:
#                     count += 1

#             else:
#                 print('Вы ввели не число')

#     elif answer == 'нет' or answer == 'Нет':
#         print('программа закрыта')
#         i = 1
#     else:
#         print('Введите именно да или нет: ')
#         answer = input('Хотите поиграть? (да/нет): ')

# inp1 = input()
# ls = inp1.split()
# list_ = [] 
# try:
#     for i in ls: 
#         try:
#             list_.append(int(i))
#         except ValueError:
#             raise Exception('Данный элемент не является числом!') 
# except Exception as e:
#     print(e)
# else:
#     print(list_) 

# print(all([True, True, True])
list_ = [1, 2, 3, 4, 5, 6,  7, 8, 9]

# print(any(num > 0 for num in [1, 2, -9, -4]))
