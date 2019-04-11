'''
2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию. Получить объект — словарь из предыдущего задания.
'''
import pickle
import json


with open('group.pickle','rb') as picklefile:
    data = pickle.load(picklefile)
    print('From pickle = ', data)

with open('group.json','r') as jsonfile:
    data = json.load(jsonfile)
    print('From json = ', data)