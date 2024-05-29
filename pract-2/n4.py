cv1, cv2 = input(), input()
print ()
if cv1 != 'красный' and cv1 != 'желтый' and cv1 != 'синий':
   print('ошибка')
elif cv2 != 'красный' and cv2 != 'желтый' and cv2 != 'синий':
   print('ошибка')
elif cv1 == 'красный' and cv2 == 'синий' or cv1 == 'синий' and cv2 == 'красный':
    print('фиолетовый')
elif cv1 == 'красный' and cv2 == 'желтый' or cv1 == 'желтый' and cv2 == 'красный':
    print('оранжевый')
elif cv1 == 'синий' and cv2 == 'желтый' or cv1 == 'желтый' and cv2 == 'синий':
    print('зеленый')
elif cv1 =='красный' and cv2 =='красный':
    print('красный')
elif cv1 =='синий' and cv2 =='синий':
    print('синий')
elif cv1 =='желтый' and cv2 =='желтый':
    print('желтый')