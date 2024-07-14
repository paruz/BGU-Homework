def number_of_ways(n):
    if n == 0 or n == 1 or n == 2:
        return n
    else:
        return number_of_ways(n - 1) + number_of_ways(n - 2)
print(number_of_ways(int(input('Количество ступенек: '))))
