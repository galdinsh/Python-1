n = int(input('Введите шестизначное число билета: '))
summa2 = summa1 = 0
k = s = 1
while k <= 3:
    x = n % 10
    summa2 = summa2 + x
    n = n // 10
    k += 1
while s <= 3:
    m = n % 10
    summa1 = summa1 + m
    n = n // 10
    s += 1
if summa1 == summa2:
    print("Билетик счастливый")
else:
    print("Билетик не счастливый")