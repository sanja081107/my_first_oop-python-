from datetime import datetime as dt

class Player:

    __LVL, __HEALTH = 1, 100
    __slots__ = ['__lvl', '__health', '__born']

    def __init__(self):
        self.__lvl = Player.__LVL
        self.__health = Player.__HEALTH
        self.__born = dt.now()

    def attac(self, target):
        target.__health -= 10
        target.__lvl -= 1
        self.__lvl += 1
        print('-----------')
        print(f'{self.__class__.__name__} attacs {target.__class__.__name__}',
              f'\nHis health downgraded to {target.__health}')
        print('-----------')

    def heals(self):
        self.__health += 30
        print('-----------')
        print(f'{self.__class__.__name__} heals himself',
              f'\nHis health upgraded to {self.__health}')
        print('-----------')

    @property
    def lvl(self):
        if self.__lvl > 100:
            self.__lvl = 100
        if self.__health > 100:
            self.__health = 100
        return self.__health, self.__lvl, f'{dt.now() - self.__born}'

    @lvl.setter
    def lvl(self, number):
        self.__lvl += Player.__type_value(number)
        if self.__lvl > 100:
            self.__lvl = 100
        if self.__health > 100:
            self.__health = 100

    @classmethod
    def change_values_cls(cls, lvl=1, health=100):
        cls.__LVL = Player.__type_value(lvl)
        cls.__HEALTH = Player.__type_value(health)

    @staticmethod
    def __type_value(value):
        if type(value) == int:
            return value
        else:
            raise TypeError('Value must be int')

Player.change_values_cls(10)
pl1 = Player()
print(pl1.lvl)

Player.change_values_cls()
pl2 = Player()
pl2.lvl = 5
print(pl2.lvl)

pl2.attac(pl1)
pl2.attac(pl1)
pl1.attac(pl2)
pl2.heals()

print(pl1.lvl)
print(pl2.lvl)

