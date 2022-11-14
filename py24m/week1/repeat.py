"""List"""
# a = ('football')
# b = len([4:])
# c = len([:6])
# print(b + c) 

# list_ = 'helloooooworld'
# strl = ''.join(list_)
# l = len(strl)+1
# p1 = strl[0:l//2]# [0:7]
# p2 =  strl[l//2:]# [7:-1]
# print(p1) 
# print(p2)

# list_ = ['helloooooworld']
# for i in list_:
#     l = len(i)+1
#     p1 = i[:l//2]
#     p2 = i[l//2:]
# print(p1)
# print(p2)


# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBazz')
#     elif i % 3:
#         print('Fizz')
#     elif not i % 5:
#         print('Bazz')
#     else:
#         print(i) 
    




"""6) Напишите программу которая будет находить наибольшую цифру натурального числа Натурального число вводится с клавиатуры Найти его наибольшую цифру"""
# m = 0
# num = int(input("numbers"))
# while num > 0 :
#     if num % 10 > m: 
#         m = num % 10 

#     num = num // 10 #3456789398765

# print(m)

# numbers_str = input('Введите цифры через запятую:').split(', ')
# numbers_int = []
# for number in numbers_str: 
#     numbers_int.append(int(number)) 
 
# print(numbers_int[0], numbers_int[-1]) 


# numbers_int[-1] = 'Makers'
# print(numbers_int) 

#  numbers_str = input('Введите цифры через запятую:').split(', ')



# list_length = int(input('hello world: '))
# words = []
# words_length = [] 
# for i in range(list_length):
#     word = input('hello world: ')
#     words.append(word)

# for i in words:
#     words_length.append(len(i))
# print(words)
# print(words_length) 



#  numbers_str = input('Введите цифры через запятую:').split(', ')
# numbers_int = []
# for number in numbers_str: 
#     numbers_int.append(int(number)) 
 
# print(numbers_int[0], numbers_int[-1]) 


# numbers_int[-1] = 'Makers'
# print(numbers_int) 
 
name_of_list = ('helloworld')
strl = ''.join(name_of_list)
l = len(name_of_list)+1
p1 = strl[0:l//2]# [0:7]   
p2 =  strl[l//2:]# [7:-1]     
print(p1)
print(p2)
