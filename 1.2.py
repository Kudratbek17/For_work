#2,1
#Определение четности и нечетности числа

while True:
    a = int(input())
    if a % 2 == 0:
        print('Четное число')
    else:
        print('Нечетное число')

#2,2
#Сокращение слово до цифр в промежутке
a = input()
if len(a) > 4:
    b = a[0]
    c = a[-1]
    d = len(a)-2
    e = b+str(d)+c
    print(e)
else:
    print(a)

#2,3
#Определение високосный или не високосный год
a = int(input())
if a % 4 == 0:
    print('Високосный год')
elif a % 100 == 0:
    print('Не високосный')
else:
    print('Не високосный')