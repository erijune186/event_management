from PIL import Image
path = input('Nhap duong dan file: ')
im = Image.open(path)
size = im.size
im.close()
print(f'Kich thuoc anh la {size[0]}x{size[1]}')