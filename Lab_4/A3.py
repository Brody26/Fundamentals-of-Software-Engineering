def check(packets):
    lost_packets = 0
    origin = 0
    final = 0
    if not all(char in '01' for char in packets):
        print('Неверный ввод(были введены не подобающие символы)')
        return False

    if len(packets) < 5:
        print('Неверный ввод(длина меньше 5)')
        return False

    for packet in packets:
        if packet == '0':
            lost_packets += 1

    for packet in packets:
        if packet == '0':
            origin += 1
        elif packet == '1':
            if origin > final:
                final = origin
            origin = 0

    percentage_losses = (lost_packets / len(packets)) * 100
    connection_quality = None
    if percentage_losses <= 1:
        connection_quality = 'Отличное качество'
    elif 1 < percentage_losses <= 5:
        connection_quality = 'Хорошее качество'
    elif 5 < percentage_losses <= 10:
        connection_quality = 'Удовлетворительное качество'
    elif 10 < percentage_losses <= 20:
        connection_quality = 'Плохое качество'
    elif percentage_losses > 20:
        connection_quality = 'Критическое состояние сети'


    stats(packets, lost_packets, final,percentage_losses,connection_quality)
    return None


def stats(packets,lost_packets,final,percentage_losses,connection_quality):
    print('Вывод результатов:')
    print(f'Общее количество пакетов:{len(packets)}')
    print(f'Количество потерянных пакетов:{lost_packets}')
    print(f'Длина самой длинной последовательности потерянных пакетов:{final}')
    print(f'Процент потерь: {percentage_losses:.1f}%')
    print(f'Качество связи: {connection_quality}')

def main():
    packets = input(f'Ввод(0 и 1):\n')
    check(packets)

main()