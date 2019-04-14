'''1. Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
my_favourite_group = {
‘name’: ‘Г.М.О.’,
‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
{‘name’: ‘Шапито’,‘year’: 2014}]}
С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.
'''
import json
import pickle


my_favourite_group = {
'name': 'Г.М.О.',
'tracks': ['Последний месяц осени', 'Шапито'],
'Albums': [{'name': 'Делать панк-рок','year': 2016},
{'name': 'Шапито','year': 2014}]}



with open('group.pickle','wb') as picklefile:
    data = pickle.dumps(my_favourite_group)
    print('To pickle = ', data)
    pickle.dump(my_favourite_group,picklefile)

with open('group.json', 'w', encoding='utf-8') as jsonfile:
    data = json.dumps(my_favourite_group)
    print('To json = ', data)
    json.dump(my_favourite_group,jsonfile)

