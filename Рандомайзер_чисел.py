def count_digit():
    from random import randint
    num = randint(1, 100)  # Перменной присваивается случайное значение
    return num

def is_valid():
    n = input('Введите число от 1 до 100 - ')
    flag = False
    while flag != True:
        if n.isdigit() == False or float(n) - int(n) != 0 or not 1 <= int(n) <= 100:
            n = input('Пожалуйста, введите целое число от 1 до 100 - ')
        else:
            flag = True
    return n  # функция для валидации данных

def digit_random(n, num):
    count = 1
    while n != num:  # Цикл для определения нужного значения
        if int(n) < num:
            n = input('Не совсем! Попробуйте число побольше - ')
            count += 1
        elif int(n) > num:
            n = input('Не-а! Попробуйте число поменьше - ')
            count += 1
        elif int(n) == num:
            break
    return count

def game_results(count):
    if count == 1:
        print(f'Ура! Вы угадали число с первой попытки! Вы молодец!)')
    else:
        print(f'Ура! Вы угадали число за {count} попыток! Поздравляю вас)')

def game_continue(cont):
    flag = True
    while flag == True:
        if cont not in ('да', 'нет', 'lf', 'ytn'):
            cont = input('Пожалуйста, введите "да" или "нет" -' )
        elif cont in ('ytn', 'нет'):
            print('Спасибо за игру! До новых встреч!' )
            flag = False
            break
        elif cont in ('да', 'lf'):
            print('Тогда продолжим!' )
            break
    return flag

def game_start():
    flag = True
    while flag == True:
        print('Приветствую в моей игре "Числовая Угадайка"!' )
        num = count_digit()
        n = is_valid()
        count = digit_random(n, num)
        game_results(count)
        cont = input('Хотите сыграть ещё раз? Введите "да", а если нет - "нет" -' )
        flag = game_continue(cont)

game_start()



