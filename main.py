import random

def print1():
    """
    Первонаальная фунция, от которой были сделан следующие
    """
    print('Print 1))')

def print1_1():
    """
    Краткое описание модуля.

    Более подробное описание модуля, если необходимо.
    """
    print('Print 1.1))')
    
def is_lucky_test(num) -> bool:
    '''
    Тестирование этой функции проходит несколько этапов.
    По задумке эта функция должна принимать шанс удачного исхода
    , и выдавать bool повезло или нет.

    По сценаию "Черный ящик" нам извесно только то
    что эта функция принимает один аргумент и возвращает bool

    Этапы проверки:
    1. Проверка задуманной работы фунции (передача числа)
    2. Проверка результата при репральных значениях, например -1, 0 и по логике > 100
    3. Проверка при которой фунции подается случайный аргумент, например строка или массив
    '''

    return random.random() < (num / 100)

def print2():
    print('Print 2')
    

def main():
    print1()
    print1_1()
    print2()


if __name__ == '__main__':
    main()