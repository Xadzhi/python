
# Вычислить число Пи c заданной точностью d  Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001
# !!ВНИМАНИЕ  !!! не использовать константу math.pi
# ---------------------------------------------------------------------------------------------------------
# РЕШЕНИЕ
# d=input('Введите точность числа Пи : ')
# d=float(d)
# k = 1
# x = 0
# coont = 0
# while not d == 1:
#         d = d * 10
#         coont += 1
# print (coont)
# for k in range(1, 1000000):
#     x = x+4*((-1)**(k+1))/(2*k-1)
# print(round(x, coont))
# ---------------------------------------------------------------------------------------------------------
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# ---------------------------------------------------------------------------------------------------------
# РЕШЕНИЕ

A=int(input("Задайте натуральное число N: "))
print('множители числа N: ')
for i in range(1, A+1):
    if(A%i==0):
        print(i)
# ---------------------------------------------------------------------------------------------------------
# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []
# ---------------------------------------------------------------------------------------------------------
# РЕШЕНИЕ
# st='47756688399943'
# li={}
# red=''
# for i in st:
#     if not li.get(i):
#         li[i]=st.count(i)
# print(li)
# for item in li:
#     if li[item] == 1:
#      print(item) 
# ---------------------------------------------------------------------------------------------------------
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
# Записываем результат в файл.

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0    
# ---------------------------------------------------------------------------------------------------------
# РЕШЕНИЕ
# from random import randint
# import itertools

# k = randint(2, 7)

# def get_ratios(k):
#     ratios = [randint(0, 10) for i in range (k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10) 
#     return ratios

# def get_polynomial(k, ratios):
#     var = ['*x^']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')


# ratios = get_ratios(k)
# polynom1 = get_polynomial(k, ratios)
# print(polynom1)

# with open('t.txt', 'w') as data:
#     data.write(polynom1)
# ---------------------------------------------------------------------------------------------------------
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x + 53 = 0
# ---------------------------------------------------------------------------------------------------------
# РЕШЕНИЕ
# # # # # # # НЕ ХВАТИЛО ВРЕМЕНИ