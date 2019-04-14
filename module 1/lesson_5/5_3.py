'''
3. Напишите функцию, которая принимает на вход список. Функция создает из этого списка новый список из квадратных корней чисел (если число положительное) и самих чисел (если число отрицательное) и возвращает результат (желательно применить генератор и тернарный оператор при необходимости). В результате работы функции исходный список не должен измениться.
Например:
old_list = [1, -3, 4]
result = [1, -3, 2]
Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.
'''
import random
import math

# example1 = [1, -3, 4]
example1 = [random.randint(-100,100) for element in range(0, 15)]


def my_func(oldlist):
    return [math.sqrt(element) if element > 0 else element for element in oldlist]


if __name__ == '__main__':
    print('Old List: ', example1)
    print('New List: ', my_func(example1))
