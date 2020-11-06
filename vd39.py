from io import SEEK_END
import sys


path1 = input('Nhap duong dan file 1: ')
path2 = input('Nhap duong dan file 2: ')
size1 = size2 = 0

f1 = open(path1, 'rb')
f2 = open(path2, 'rb')

s = f1.read()
size1 = f1.seek(0, SEEK_END)
size2 = f2.seek(0, SEEK_END)

if size1 != size2:
    print('Hai file co noi dung khac nhau.')
    f1.close()
    f2.close()
    sys.exit()

f1.seek(0)
f2.seek(0)
for i in range(size1):
    char1 = f1.read(1)
    char2 = f2.read(1)
    if not char1 or char2: break
    if char1 != char2:
        print('Hai file co noi dung khac nhau.')
        sys.exit()
print('Hai file co noi dung giong nhau.') 
f1.close()
f2.close()
