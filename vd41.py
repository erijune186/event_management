path1 = input('Nhap duong dan file nguon: ')
path2 = input('Nhap duong dan file dich: ')

f1 = open(path1, 'rb')
f2 = open(path2, 'ab+')

while 1:
    char = f1.read1()
    if not char:
        break
    f2.write(char)

f1.close()
f2.close()