'''
4. Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр — armor = 1.2 (величина брони персонажа)
Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
Следовательно, у вас должно быть 2 функции:
1. Наносит урон. Это улучшенная версия функции из задачи 3.
2. Вычисляет урон по отношению к броне.
Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа.
'''
player = {
    'health': 100,
    'damage': 50,
    'armor': 1.2,
}

enemy = {
    'health': 100,
    'damage': 50,
    'armor': 2,
}


def get_damage(damage,armor):
    return damage/armor

def get_names(name1='player1',name2='player2'):
    global enemy, player
    if len(name1) ==0:
        player['name'] = input('Input player`s name: ')
    if name2 == '':
        enemy['name'] = input('Input enemy`s name: ')


def attack(person1, person2):
    person2['health'] -= get_damage(person1['damage'], person2.get('armor'))


def main():
    get_names()
    attack(player,enemy)
    print(player)
    print(enemy)

if __name__ == '__main__':
    main()