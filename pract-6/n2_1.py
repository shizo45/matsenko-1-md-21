
group1 = "АВЕИНОРСТ"
group2 = "ДКЛМПУ"
group3 = "БГЬЯ"
group4 = "ЙЫ"
group5 = "ЖЗХЦЧ"
group6 = "ЩЭЮ"
group7 = "ФЩЪ"

charPrice = { group1: 1, group2: 2, group3: 3, group4: 4, group5: 5, group6: 8, group7: 10 }

def getCharPrice(char):
    res = 0
    for i in char:
        for j in charPrice:
            if i in j:
                print(i, charPrice[j])
                res += charPrice[j]
    return res

word = str(input('Введите слово капсом: '))

print(getCharPrice(word))

