def rectangle(rows, columns, name1):
    print(f'Прямоугольник {rows}x{columns}:')
    for row in range(rows):
        for column in range(columns):
            print('#', end='')
        print()
    if name1 != 4:
        restart()

def right_triangle(rows, columns,name1):
    print(f'Правый треугольник {rows}x{columns}:')
    for row in range(1, rows + 1):
        for column in range(row):
            print('#', end='')
        print()
    if name1 != 4:
        restart()
def frame(rows, columns):
    print(f'Рамка {rows}x{columns}:')
    for row in range(rows):
        for column in range(columns):
            if row == 0 or row == rows - 1 or column == 0 or column ==  columns - 1:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    restart()
def restart():
    name2 = int(input('Вы хотите увидеть ещё фигуры?\nЕсли да введите 1, если нет введи 2:'))
    if name2 == 1:
        main()
    elif name2 == 2:
        print('Хорошего дня')
    else:
        print('Функии ещё нет')
def main():
    rows = int(input('Введите количество столбцов:'))
    columns = int(input('Введите количество рядов:'))
    name1 = int(input(
        f'Какую фигуру вы хотите увидеть?\nВведите 1 - если прямоугольник, 2 - если треугольник, 3 - если рамку, а 4 - если все:'))
    if name1 == 1:
        rectangle(rows, columns, name1)
    elif name1 == 2:
        right_triangle(rows, columns, name1)
    elif name1 == 3:
        frame(rows, columns)
    elif name1 == 4:
        rectangle(rows, columns, name1)
        right_triangle(rows, columns, name1)
        frame(rows, columns)
    else:
        print('функии ещё нет')
main()
