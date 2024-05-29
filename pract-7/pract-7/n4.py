from PIL import Image
imgZnak = Image.open('znak.png')
imgShar = Image.open('shar.jpg')
imgShar.paste(imgZnak.resize((300,100)))
imgShar.save('watermark.jpg')