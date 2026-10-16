x1 = int(input('Введите предыдущие значение:'))
x2 = int(input('Введите текущие значение:'))
average_kub_m = 0
pay_uses_kub_m = 0
uses_kub_m = x2 - x1

if uses_kub_m < 0:
    uses_kub_m += 10000

if uses_kub_m <= 300:
    pay_uses_kub_m = 21
elif 300 < uses_kub_m <= 600:
    pay_uses_kub_m = 21 + (uses_kub_m - 300) * 0.06
    average_kub_m = pay_uses_kub_m / uses_kub_m
elif 600 < uses_kub_m <= 800:
    pay_uses_kub_m = 21.0 + (600 - 300) * 0.06 + (uses_kub_m - 600) * 0.04
    average_kub_m = pay_uses_kub_m / uses_kub_m
else:
    pay_uses_kub_m =  21.0 + (600 - 300) * 0.06 + (800 - 600) * 0.04 + (uses_kub_m - 800) * 0.025
    average_kub_m = pay_uses_kub_m / uses_kub_m

print(f'Предыдущее:{x1}\nТекущее:{x2}\nИспользовано:{uses_kub_m}\nК оплате:{pay_uses_kub_m:.2f}\nСр. цена m^3:{average_kub_m:.2f}')