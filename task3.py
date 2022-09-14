# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

arr=list(map(int,input().split()))

arr_new = []

for i in arr:
    if i not in arr_new:
        arr_new.append(i)

print(arr_new)