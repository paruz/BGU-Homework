try:
    with open('cities.txt', 'r', encoding="utf-8") as f1:
        with open('filtered_cities.txt', 'w') as f2:
            dictionary = {}
            number = input('Минимальное количество жителей: ')
            while not number.isdigit():
                number = input('Минимальное количество жителей: ')
            number = int(number)
            for line in f1.readlines():
                words = line.split(':')
                dictionary[words[0]] = words[1].rstrip()
            for city in dictionary:
                if int(dictionary[city]) > number:
                    f2.write(city + ':' + dictionary[city] + '\n')
except FileNotFoundError:
    print('Файл cities.txt не найден')
