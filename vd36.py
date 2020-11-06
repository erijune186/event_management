x = float(input('Nhap x = '))
n = int(input("Nhap n = "))

def power(x, n):
    if n == 1: return x
    tmp = power(x, n // 2)
    if n % 2 == 1: return tmp*tmp*x
    return tmp*tmp

print(f'{round(x, 2)} ^ {n} = {round(power(x, n), 2)}')