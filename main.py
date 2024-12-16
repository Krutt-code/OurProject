import random
import unittest
    
def is_lucky(num) -> bool:
    '''
    :param num: int (0-100) - Шанс срабатывания
    :return bool
    '''
    return random.random() < (num / 100)

def lucky_test():
    '''
    Тестирование этой функции проходит несколько этапов.

    По сценаию "Черный ящик" нам извесно только то
    что эта функция принимает один аргумент и возвращает bool

    Этапы проверки:
    1. Проверка задуманной работы фунции (передача числа)
    2. Проверка результата при непральных значениях, например -1, 0 и по логике > 100
    3. Проверка при которой фунции подается случайный аргумент, например строка или массив
    '''

    # 1. Проверка задуманной работы фунции (передача числа)
    num = 10
    try:
        print(f'{num}: ')
        print(is_lucky(num))
        print('Завершено без ошибок')
    except Exception as e:
        print('Завершено с ошибкой')
        print(e)

    print()

    # 2. Проверка результата при непральных значениях, например -1, 0 и по логике > 100
    num = -1
    try:
        print(f'{num}: ')
        print(is_lucky(num))
        print('Завершено без ошибок')
    except Exception as e:
        print('Завершено с ошибкой')
        print(e)

    print()

    # 3. Проверка при которой фунции подается случайный аргумент, например строка или массив
    num = '10'
    try:
        print(f'{num} - {type(num)}: ')
        print(is_lucky(num))
        print('Завершено без ошибок')
    except Exception as e:
        print('Завершено с ошибкой')
        print(e)



# isinstance(x, str)

def get_unicode(char):
    """
    Эта функция получает символ с клавиатуры и возвращает его код Unicode.
    """
    
    return ord(char)

def unicode_test():
    char = 'a'
    print('Этап 1: Выводим unicode одного символа')
    try: 
        """Выводим unicode одного символа"""
        print(get_unicode(char)) 
        print('Завершено без ошибок')
    except Exception as e:
        print('Завершено с ошибкой')
        print(e)
    
    print()
            
    char = 'ad'
    print('Этап 2: Результат при двух символах')
    try:
        """Результат при двух символах"""
        print(get_unicode(char))
        print('Завершено без ошибок')
    except Exception as e:
        print('Завершено с ошибкой')
        print(e)
    
    print()

    char = 2
    print('Этап 3: Результат при вводе цифры')
    try:
        """Результат при вводе цифры"""
        print(get_unicode(char))
        print('Завершено без ошибок')
    except Exception as e:
        print('Завершено с ошибкой')
        print(e)    
