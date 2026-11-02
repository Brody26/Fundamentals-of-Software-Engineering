import random
import time


def table():
    number1 = random.randint(1,10)
    number2 = random.randint(1,10)
    start = time.time()
    while True:
        try:
            answer_user = int(input(f'{number1} * {number2} = '))
            break
        except ValueError:
            print('Пожалуйста, введите целое число!')
    end = time.time()

    if answer_user == number1 * number2:
        print(f'Верно.(Время:{end-start:.1f}сек)')
    else:
        print(f'Неверно! Правильный ответ: {number1 * number2} (Время:{end-start:.1f}сек)')


def counter(n):
    for i in range(1,n+1):
        print(f'Вопрос {i}/{n}')
        table()


def main():
    c = int(input('Введите количество примеров: '))
    counter(c)


main()


