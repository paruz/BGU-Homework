n_str = input("Введите целое число: ")
while not n_str.isdigit():
    n_str = input("Введите целое число: ")
n = int(n_str)
while n > 9:
    n = sum(map(int, str(n)))
print(n)