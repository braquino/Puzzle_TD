from kivy.utils import get_color_from_hex as hexc
from random import choice


class Resource:
    def __init__(self, name, color, chance):
        self.name = name
        self.color = color
        self.chance = chance


resources = {}

resources['wood'] = Resource('Wood', hexc('#663300'), 100)
resources['iron'] = Resource('Iron', hexc('#818181'), 190)
resources['food'] = Resource('Food', hexc('#990099'), 260)
resources['fire'] = Resource('Fire', hexc('#FF7700'), 320)
resources['magic'] = Resource('Magic', hexc('#F0FF12'), 370)


def rand_type():
    selection = choice(resources, 1, p=[x.chnce for x in resources.values()]
    print(selection)
    return selection

rand_type()