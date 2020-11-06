a = []

f = open('C:\\test\\float.dat', 'w')
n = int(input('Nhap so phan tu n = '))

f.write(f'{n}\n')
for i in range(n):
    a.append(int(input(f'a[{i}] = ')))
    f.write(str(a[i]) + '\n')

f = open('C:\\test\\float.dat', 'r')
n = int(f.readline())

a.clear()
for i in range(n):
    a.append(int(f.readline()))

a.sort()
f = open('C:\\test\\float_sx.dat', 'w')
f.write(str(n) + '\n')
for i in range(n):
    f.write(str(a[i]) + '\n')