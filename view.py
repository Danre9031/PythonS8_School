def get_op():
    op =  int(input("\
Что вы хотите сделать?\n\
1 - Добавление Ученика\n\
2 - Добавление Предмета\n\
3 - Добавление Оценки\n\
4 - Показать весь список Учеников\n\
5 - Показать оценки конкретного Ученика\n\
6 - Выход\n\
\n\
Ваш выбор: "))
    return op
    

def input_student():
    name = input("Введи имя фамилию: ")
    return name

def input_less():
    less = input("Введи предмет: ")
    return less

def get_mark():
    name = input("Введи фамилию: ")
    less = input("Введи предмет: ")
    mark = input("Введи оценку: ")
    return name,less,mark

def input_student_table():
    name = input("Введи имя фамилию ученика для просмотра оценок: ")
    return name