try:
    with open('input.txt') as f1:
        with open('output.txt', 'w') as f2:
            symbols = input('Введите символы для удаления с правого края строки:')
            for line in f1.readlines():
                line = line.rstrip(symbols + '\n') + ';'
                f2.write(line[::-1] + '\n')
except FileNotFoundError:
    print('Файл input.txt не найден')