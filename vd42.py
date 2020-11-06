path = input('Nhap duong dan file: ')

f = open(path, 'r')

c = w = s = l = 0 # char word sentence line

for line in f:
    for word in line.split():
        w += 1
    
    for sentence in line.split('.'):
        if sentence!='' : s += 1
    l += 1
    if line[len(line)-1] == '.': s -= 1
c = f.tell() - l

f.close()
print(f'so ky tu: {c}')
print(f'so tu: {w}')
print(f'so cau: {s}')