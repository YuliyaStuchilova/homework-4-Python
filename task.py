# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, 
# сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

n = int(input())

pi=0

for k in range(n):
    pi+=(1/(16**k))*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))

print(round(pi,n))