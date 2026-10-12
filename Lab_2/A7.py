x1 = int(input('Введите координату x1:'))
y1 = int(input('Введите координату y1:'))
x2 = int(input('Введите координату x2:'))
y2 = int(input('Введите координату y2:'))

sum_x1_y1 = x1 + y1
sum_x2_y2 = x2 + y2

if sum_x1_y1 % 2 == 0 and sum_x2_y2 % 2 == 0:
    print('Yes')
    print('White')
elif sum_x1_y1 % 2 == 1 and sum_x2_y2 % 2 == 1:
    print('Yes')
    print('Black')
else:
    print('No')
