x1 = float(input('Введите координату x1:'))
y1 = float(input('Введите координату y1:'))
x2 = float(input('Введите координату x2:'))
y2 = float(input('Введите координату y2:'))

if (x1 > 0 and y1 > 0) and (x2 > 0 and y2 > 0):
    print('Yes, I')
elif (x1 < 0 and y1 > 0) and (x2 < 0 and y2 > 0):
    print('Yes, II')
elif (x1 < 0 and y1 < 0) and (x2 < 0 and y2 < 0):
    print('Yes, III')
elif (x1 > 0 and y1 < 0) and (x2 > 0 and y2 < 0):
    print('Yes, IV')
else:
    print('NO')