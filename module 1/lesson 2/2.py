'''
2. Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
'''

def get_max(num1,num2,num3):
    max = num1
    if num2 > max:
        max = num2
    if num3 > max:
        max = num3
    return max

if __name__ == '__main__':
    print('MAX is: ', get_max(4,5,3))