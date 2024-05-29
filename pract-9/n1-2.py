from PIL import Image, ImageFilter
from pathlib import Path
imagePath = ('C:/Users/Машуля/Documents/python-laby/pract-9/save')
p = Path('C:/Users/Машуля/Documents/python-laby/pract-9/photo')
for i in p.rglob('*.jpg'):
    img = Image.open(i)
    fil = img.filter(ImageFilter.EMBOSS)
    file_name = str(i).split("\\")[-1 ]
    print(file_name)
#    fil.show()
    fil.save(f'{imagePath}/{file_name}')
  