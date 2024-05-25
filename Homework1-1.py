n_str = input("Введите целое число: ")
while not n_str.isdigit():
    n_str = input("Введите целое число: ")
n = int(n_str)
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
