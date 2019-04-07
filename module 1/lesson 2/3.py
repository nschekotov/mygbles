'''3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
name — строка, полученная от пользователя,
health = 100,
damage = 50.

Поэкспериментируйте с значениями урона и жизней по желанию.
Теперь надо создать функцию attack(person1, person2).
Примечание: имена аргументов можете указать свои.
Функция в качестве аргумента будет принимать атакующего и атакуемого.
В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого. Функция должна сама работать со словарями и изменять их значения.
'''


player = {
    'health': 100,
    'damage': 50,
}


enemy = {
    'health': 100,
    'damage': 50,
}


def get_names():
    global enemy, player
    player['name'] = input('Input player`s name: ')
    enemy['name'] = input('Input enemy`s name: ')


def attack(person1, person2):
    person2['health'] -= person1['damage']


def main():
    get_names()
    attack(player,enemy)
    print(player)
    print(enemy)

if __name__ == '__main__':
    main()