try:
    with open('input1.txt') as f1:
        try:
            with open('input2.txt') as f2:
                with open('output.txt', 'w') as f3:
                    lines = (f1.readlines() + f2.readlines())
                    arr = []
                    for line in lines:
                        line = line.rstrip()
                        arr.append(line)
                    arr = sorted(arr)
                    for word in arr:
                        f3.write(word + '\n')
        except FileNotFoundError:
            print('Файл input2.txt не найден')
except FileNotFoundError:
    print('Файл input1.txt не найден')
