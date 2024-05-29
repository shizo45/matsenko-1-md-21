from PIL import Image
imgBirthday = Image.open('Birthday.jpg')
imgNewYear = Image.open('NewYear.jpg')
imgHalloween = Image.open('Halloween.jpg')
dictionary = { 'Birthday' : imgBirthday, 'NewYear' : imgNewYear,'Halloween' : imgHalloween}
holiday = input('Введите название праздника: ')
if holiday in dictionary:
    img = dictionary[holiday]
    img.show()


