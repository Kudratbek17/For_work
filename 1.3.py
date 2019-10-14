#3,1
#Игра угадай цифру
import random
b = random.randint(1, 10)
while True:
    a = int(input('Введите число'))
    if a == b:
        print('Ты выиграл')
        break
    else:
        print("Не верно")
        continue

#3,2
#Треугольник из звезд
for w in range(1, 6):
    print(w * '*')
for x in range(4, 0, -1):
    print('*' * x)