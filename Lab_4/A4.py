def check_card(code):

    if code.startswith(("34", "37")):
        if len(code) == 15:
            return 'Тип карты: American Express'
        else:
            return 'Карта недействительна (неверная длина для American Express)'

    elif code.startswith(('51', "52", "53", "54", "55")):
        if len(code) == 16:
            return 'Тип карты: MasterCard'
        else:
            return 'Карта недействительна (неверная длина для MasterCard)'

    elif code.startswith('4'):
        if len(code) in (13,16):
            return 'Тип карты: Visa'
        else:
            return 'Карта недействительна (неверная длина для Visa)'
    else:
        return 'Карта недействительна (неизвестный тип карты / неверные начальные цифры)'

def luna(code):
    total_sum = 0
    for i in code[-2::-2]:
        d = int(i)*2
        if d > 9:
            d -= 9
        total_sum += d

    for q in code[-1::-2]:
        s = int(q)
        total_sum += s

    if total_sum % 10 == 0:
        print('Карта действительна')
        print(check_card(code))
    else:
        print('Карта недействительна')

def main():
    user = input('Введи номер банковской карты: ')
    luna(user)
main()