import re
try:
    with open('input.txt') as f1:
        lines = f1.readlines()
        n = 0
        for line in lines:
            number = re.sub("[^0-9]", "", line)
            n += int(number)
        if len(lines) != 0:
            avg = n // len(lines)
    with open('output.txt', 'w') as f2:
        for line in lines:
            number = re.sub("[^0-9]", "", line)
            if int(number) > avg:
                name = re.sub("[^a-zA-Z]", "", line)
                f2.write(name + '\n')
except FileNotFoundError:
    print('Файл input.txt не найден')
