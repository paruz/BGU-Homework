try:
    with open('input.txt', 'r', encoding="utf-8") as f1:
        with open('output.txt', 'w') as f2:
            products = {}
            for line in f1.readlines():
                if ':' in line:
                    words = line.split(':')
                    if any(char.isdigit() for char in words[1]):
                        words[0] = words[0].strip('" ')
                        words[1] = words[1].strip('\n, ')
                        if words[0] in products:
                            products[words[0]] += int(words[1])
                        else:
                            products[words[0]] = int(words[1])
            for product in products:
                f2.write(product + ': ' + str(products[product]) + '\n')
except FileNotFoundError:
    print('Файл input.txt не найден')
