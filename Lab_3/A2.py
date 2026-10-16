def check_password(password):
    special_characters = {'*', '-', '#'}
    error = []

    has_upper = False
    has_lower = False
    has_digit = False
    has_spec = False
    has_invalid = False

    if len(password) != 8:
        error.append('Длина пароля не равна 8')

    for symbol in password:
        if symbol.isupper():
            has_upper = True
        elif symbol.islower():
            has_lower = True
        elif symbol.isdigit():
            has_digit = True
        elif symbol in special_characters:
            has_spec = True
        else:
            has_invalid = True

    if has_upper == False:
        error.append('В пароле отсутствуют заглавные буквы')
    if has_lower == False:
        error.append(' В пароле отсутствуют строчные буквы')
    if has_digit == False:
        error.append('В пароле отсутствуют цифры')
    if has_spec == False:
        error.append('В пароле отсутствуют специальные символы')
    if has_invalid == True:
        error.append('В пароле используются непредусмотренные символы')

    if not error:
        print('Надежный пароль')
    else:
        for error in error:
            print(error)

user_password = input('Введи пароль:')
check_password(user_password)