#1,1
#Перевод с фарингейт в цельсию
F = int(input())
C = ((F - 32)*5)/9
print(C)

#1,2
#Сравнение длинны слов
a = input()
b = input()
if len(a)>len(b):
    print('Первое слово больше второго')
elif len(a)<len(b):
    print('Первое слово меньше второго')
else:
    print('Обе равны')