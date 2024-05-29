from PIL import Image, ImageOps
img = Image.open('jellyfish.jpg')
resImg = img.reduce(3)
resImg = ImageOps.mirror(resImg)
resImg = ImageOps.flip(resImg)
resImg.save('jellyfish2.jpg')
resImg.show()
