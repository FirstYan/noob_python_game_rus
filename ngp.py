import random
import os
import time
while True:
    a = [1, 2, 3]
    random.shuffle(a)
    print("Выберете")
    print("1 Камень")
    print("2 Ножницы")
    print("3 Бумага")
    print("0 информация")
    p = int(input())
    os.system('cls||clear')
    if (p == 1):print("Вы выбрали КАМЕНЬ")
        
    elif (p == 2):print("Вы выбрали НОЖНИЦЫ")
            
    elif (p == 3):print("Вы выбрали БУМАГУ")

    else:print("ВЫ ВЫБРАЛИ НЕПРАВИЛЬНОЕ ЗНАЧЕНИЕ ! ПОПРОБУЙТЕ ЕЩЁ РАЗ!")
    #print(a[0])
    b = int(a[0])
    time.sleep(5)

    if (p == 1 and b == 1):
        print("Компьютер выбрал тоже КАМЕНЬ")
        print("У вас нечья")
    elif (p == 1 and b == 2):
        print("Компьютер выбрал НОЖНИЦЫ")
        print("Поздравляю, вы одержали победу")  
    elif (p == 1 and b == 3):
        print("Компьютер выбрал БУМАГУ")
        print("Вы проиграли") 

    elif (p == 2 and b == 1):
        print("Компьютер выбрал КАМЕНЬ")
        print("Вы проиграли")   
    elif (p == 2 and b == 2):
        print("Компьютер выбрал НОЖНИЦЫ")
        print("У вас нечья")
    elif (p == 2 and b == 3):
        print("Компьютер выбрал БУМАГУ")
        print("Поздравляю, вы одержали победу")

    elif (p == 3 and b == 1):
        print("Компьютер выбрал КАМЕНЬ")
        print("Поздравляю, вы одержали победу")
    elif (p == 3 and b == 2):
        print("Компьютер выбрал НОЖНИЦЫ")
        print("Вы проиграли")   
    elif (p == 3 and b == 3):
        print("Компьютер выбрал тоже БУМАГУ")
        print("У вас нечья")

    elif (p == 0 and b == 1, 2, 3):
        print("Разработчик ADRIAN, FirstYan")
        print("")
        print("")
        print("Компьютер выбирает вариант ответа ещё до вашего выбора")
        print("поетому шанс считерить невозможен")
        print("")
        print("")
        print("Практически вся логика игры прописана на if/elif/else")       
    input()