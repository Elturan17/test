"""==================="""
# def func(a, b=4, *args, **kwargs):
#     print('a - ', a)
#     print('b - ', b)
#     print('args - ', args)
#     print('kwargs - ', kwargs)

# func(6)

# func(3, 4, 5, 6, v='ggsdf', c=4, hello='hello')
"""==============Калькулятор=============="""

# def culc(num1: int, num2: int) -> float:
#     while True:
#         # num1 = int(input('введите число: '))
#         # num2 = int(input('введите число: '))
#         operation = input('выберите операциюя: +, -, *, /, **, %, //: ')
#         if operation == '+':
#             print(num1 + num2)
#         elif operation == '-':
        #     print(num1 - num2)
        # elif operation == '*':
        #     print(num1 * num2)
        # elif operation == '/':
        #     print(num1 / num2)
        # elif operation == '**':
        #     print(num1 ** num2)
        # elif operation == '%':
        #     print(num1 % num2)
        # elif operation == '//':
        #     print(num1 // num2)
        # else:
        #     print('Такой операции нет')
        # res = input('Продолжить? Да/Нет')
        
        # if res == 'Нет':
        #     break
        # if res == 'Да':
        #    culc(num1 = int(input("ВВедите число: ")), num2 = int(input('Введите число: ')))


            
            
        
        
'''GIT - это система контроля версий (записывает изменения файла или набора в течении времени). Предназначен для отслеживания ведения истории изменений файлов в проекте. Благодаря ему, можем вернуть старую версию программы'''

'''github - это онлайн сервис, предлогает услуги по хранению репозиториев м управления доступом'''

'''команды'''
# git init - иницализация нашего обьекта и создание папки .git(в ней содержатся все необходимые файлы нашего репозитория)

# git add (./<filename>) - добавляет файлы с рабочей директории в промежуточное пространство - индекс (специальное промежуточное пространства, в котором хранится изменения файлов на пути от рабочей папки до репозитория 


#  git commit - добавляет все файлы которые находятся в индексе во внутреннюю бд и сохраняет их состояние на данный момент 

# git remote add origin url(https or ssh) - добавляет удаленный репозиторий который находится на каком-нибудь сервере 

#  git push -u origin <branch name> - отвечает отправка кода в удаленный репозиторий 

# git branch - показывает список веток 

#  git branch <branch name> - создает ветку с название <branch name>

# git checkout <branch name> - переключает на ветку <branch name> 

# git pull origin <branch name> - стягиваем изменения с ветки <branch name> к себе на локалку 

# git status - показывает статус проекта 

# git log -журнал коммитов 

# git clone ссылка на удаленный репозиторий - склониова/скопирова/скачать удаленный репозиторий  