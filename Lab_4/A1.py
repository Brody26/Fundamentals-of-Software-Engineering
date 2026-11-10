import random
import time

def table(n):
    has_True = 0
    all_times = 0
    for _ in range(1, n+1):
        number1 = random.randint(1, 10)
        number2 = random.randint(1, 10)
        start = time.time()
        print(f'Вопрос:{_}/{n}')
        while True:
            try:
                answer_user = int(input(f'{number1} * {number2} = '))
                break
            except ValueError:
                print('Пожалуйста, введите целое число!')
        end = time.time()

        time_taken = end - start
        all_times += time_taken

        if answer_user == number1 * number2:
            print(f'Верно.(Время:{time_taken:.1f}c)')
            has_True += 1
        else:
            print(f'Неверно! Правильный ответ: {number1 * number2} (Время:{time_taken:.1f}сек)')

    return has_True, all_times

def stats(n):
    has_True, all_times = table(n)
    print('-' * 80)
    print('СТАТИСТИКА:')
    print('-' * 80)
    print(f'Общее время:{round(all_times,1)}')
    print(f'Среднее время на вопрос:{round(round(all_times,1) / n,1)}')
    print(f'Правильных ответов:{has_True}/{n}')
    print(f'Процент правильных:{round((has_True / n) * 100,1)}%')

def main():
    while True:
        try:
            user = int(input('Введите количество примеров:'))
            break
        except ValueError:
            print('Пожалуйста, введите целое число!')
    stats(user)

main()