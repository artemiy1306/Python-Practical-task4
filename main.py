# Задача 22: 
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
numb_first_sets= int(input("Введите кол-во элементов 1-го множества: "))
data_1 = {int(i) for i in input("Введите числа: ").split()}
numb_second_sets= int(input("Введите кол-во элементов 2-го множества: "))
data_2 = {int(i) for i in input("Введите числа: ").split()}

same_digits = data_1.intersection(data_2)
print(sorted(same_digits))



# Задача 24: 
# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, 
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть 
# ровно два соседних. Всего на грядке растёт N кустов.Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит 
# из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь 
# непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход 
# собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input("Введите количество кустов N: "))
print('Введите количество ягод, собранных с каждого куста')
array = [int(i) for i in input() .split()][ :n]
max_summa = 0
for i in range(1, len(array) - 1):
  if max_summa < array[i - 1] + array[i] + array[i + 1]: 
    max_sumina = array[i - 1] + array[i] + array[i + 1]
  if max_summa	<	array[0]	+	array[i] + array[len(array) - 1]:
    max_summa	=	array[0]	+	array[i] + array[len(array) - 1]
  if max_summa	<	array[0]	+	array[len(array) - 1] + array[len(array)	-	2]:
    max_summa	=	array[0]	+	array[len(array) - 1] + array[len(array)	-	2]
print(f' максимальное число ягод = {max_summa}')