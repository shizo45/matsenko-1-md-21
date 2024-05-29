from PIL import Image, ImageDraw, ImageFont
imgBirthday = Image.open('Birthday.jpg')
imgNewYear = Image.open('NewYear.jpg')
imgHalloween = Image.open('Halloween.jpg')
name = str(input('Введите имя человека, которого поздравляете: '))
def congrtln():
    font = ImageFont.truetype("arial.ttf", 25)
    drawer = ImageDraw.Draw(img)
    drawer.text((0, 0), name + ', поздравляю!', font=font, fill='white')
    drawer.text((1, 1), name + ', поздравляю!', font=font, fill='white')
dictionary = { 'Birthday' : imgBirthday, 'NewYear' : imgNewYear,'Halloween' : imgHalloween}
holiday = input('Введите название праздника: ')
if holiday in dictionary:
    img = dictionary[holiday]
    congrtln()
    img.show()



