'''
3. Создайте модуль main.py. Из модулей, реализованных в заданиях 1 и 2, сделайте импорт в main.py всех функций. Вызовите каждую функцию в main.py и проверьте, что все работает как надо.
Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1), так и отдельные функции из модуля.'''

from first import del_dir
import second
import first
import time

if __name__ == '__main__':
    print(second.rchoise([1,3,4,2]))
    first.create_dirs()
    time.sleep(10)
    del_dir()