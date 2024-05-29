from PIL import Image
image = Image.open('jellyfish.jpg')
image.show()
print(f'Размер файла: {image.size}')
print(f'Формат файла: {image.format}')
print(f'Цветовая модель файла: {image.mode}')