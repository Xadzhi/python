# # Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# # Пример:

# # - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# Решение
# A=[2, 3, 5, 9, 3]
# sum=0
# for i in range (1,len(A),2):
#     sum+=A[i]
# print(sum)

# # Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# # Пример:

# # - [2, 3, 4, 5, 6] => [12, 15, 16];
# # - [2, 3, 5, 6] => [12, 15]
# Решение
# A=[2, 3, 5, 9, 3, 6]
# B=[]
# if len(A)%2==0:
#     a=len(A)//2
# else :
#     a=len(A)//2+1
# for i in range(a):
#     B.append(A[i]*A[-i-1])
# print(B)
# # Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Решение
# a=[1.1, 1.2, 3.1, 5, 10.01]
# A=[]
# for i in range(len(a)):
#     if a[i] % 1 !=0:
#         A.append(a[i])
# print(A)
# for i in range(len(A)):
#     A[i]%=1
# print(A)

# maxA=max(A)
# minA=min(A)   
# print("разницa между максимальным и минимальным значением дробной части элементов = .") 
# print(maxA-minA)
# # Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Решение
# # n = int(input())
# # b = ''
# # while n > 0:
# #     b = str(n % 2) + b
# #     n = n // 2
# # print(b)

# # Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# # Пример:

# # - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Решение
a = a1 = b = b1 = 1
n = int(input( 'Введите число ----> :' ))
c = d = []
for i in range(2, n):
    a , b = -b, -a + -b
    c.append(-b)
cc=c[::-1]
for j in range(2, n):
    a1, b1 = b1, a1 + b1
    d.append(b1)
print(cc, end=',')
print(1, 0, 1, end=',')
print(d, end=',')