import random
import time



def table():
    number1 = random.randint(1,10)
    number2 = random.randint(1,10)
    while True:
        try:
            answer_user = int(input(f'{number1} * {number2} = '))
            break
        except ValueError:
            print('No')

    answer_robot = number1 * number2

    if answer_user == answer_robot:
        print('Верно')
    else:
        print(f'Неверно, правильный ответ: {answer_robot}')


def counter(n):
    while n != 0:
        n -= 1
        table()

def time1():
    start = time.time()
    end = time.time()
    cor = end - start
    print(f'{cor:.1f}')

def main():
    c = int(input('Введите количество примеров: '))
    counter(c)

main()

