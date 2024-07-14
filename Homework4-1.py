def balance_check(text):
    if len(text) == 0:
        return True
    elif '[]' in text or '<>' in text or '{}' in text or '()' in text:
        return balance_check(text.replace('[]', '').replace('<>', '').replace('{}', '').replace('()', ''))
    else:
        return False


try:
    with open('input.txt') as f1:
        with open('output.txt', 'w') as f2:
            for line in f1.readlines():
                line = ''.join(i for i in line.strip() if not i.isalpha())
                f2.write(str(balance_check(line)) + '\n')
except FileNotFoundError:
    print('Файл input.txt не найден')
