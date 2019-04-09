#1. Создайте модуль (модуль — программа на Python, т.е. файл с расширением .py).
# В нем напишите функцию, создающую директории от dir_1 до dir_9 в папке, из которой запущен данный код.
# Затем создайте вторую функцию, удаляющую эти папки. Проверьте работу функций в этом же модуле.
import os

def create_dirs():
    for i in range(1,10):
        os.mkdir('dir_'+str(i))

def del_dir():

    for i in range(1,10):
        dirname = 'dir_'+str(i)
        if os.path.exists(dirname):
            os.rmdir('dir_'+str(i))




if __name__ == '__main__':
    del_dir()