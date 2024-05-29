import random

def generate_an_exercise():
    symbols = ['+', '-']
    numA = random.randint(1, 10)
    numB = random.randint(1, 10)
    symb = random.choice(symbols)

    exercise = f"{numA} {symb} {numB}"

    return exercise
error = 0
correct = 0
while True:
    exercise = generate_an_exercise()
    print(exercise)
    otv = input()
    if otv == str(eval(exercise)):
        print('Правильно!')
        correct += 1
    else:
        print('Неправильно!')
        error += 1
        if error >= 3:
            print('Вы проиграли')
            break


print(f'Игра окончена, правильных ответов: {correct}')