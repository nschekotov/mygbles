'''Решить с помощью генераторов списка.
1. Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
    Примечание: Списки фруктов создайте вручную в начале файла.
'''

first_list = ['apple', 'raspberrry', 'strawberry', 'cherry']
second_list = ['wildberry', 'cherry', 'apple', 'lemon']

third_list = [fruit for fruit in first_list if fruit in second_list]
print(third_list)
