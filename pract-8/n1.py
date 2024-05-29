from PIL import Image
img = Image.open('postcard.jpg')
imgCrop = img.crop((0, 600, 1100, 1500))
imgCrop.show()
imgCrop.save('title.jpg')