'''
2. Дан список, заполненный произвольными числами. Получить список из элементов исходного, удовлетворяющих следующим условиям:
1. Элемент кратен 3,
2. Элемент положительный,
3. Элемент не кратен 4.
    Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.
'''
import random

rlist = [random.randint(-100,100) for element in range(0, 15)]
print('Random list = ', rlist)
result_list = [element for element in rlist if element % 3 == 0 and element>0 and element % 4 != 0]
print('Result List = ', result_list)
