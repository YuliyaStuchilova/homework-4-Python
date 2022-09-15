# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
#  и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
k = int(input())

arr = []
flag = True
f = open('file.txt', 'a')
while flag:
    n = randint(0, 100)
    if k > 0:
        if n == 0:
            f.write('')
        else:
            if n == 1:
                f.write(f'x^{k}')
                k -= 1
            else:
                f.write(f'{n}*x^{k}+')
                k -= 1
    elif k == 0:
        if n != 0:
            f.write(f'{n}')
            k -= 1
        else:
            f.write('')
    elif k == -1:
        f.write('=0')
        flag = False


f.close()
