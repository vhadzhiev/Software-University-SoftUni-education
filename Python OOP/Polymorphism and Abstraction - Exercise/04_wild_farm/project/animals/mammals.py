from project.animals.animal import Mammal


class Mouse(Mammal):
    _allowed_foods = ['Vegetable', 'Fruit']
    _weight_multiplier = 0.10

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Squeak'


class Dog(Mammal):
    _allowed_foods = ['Meat']
    _weight_multiplier = 0.40

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Woof!'


class Cat(Mammal):
    _allowed_foods = ['Vegetable', 'Meat']
    _weight_multiplier = 0.30

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Meow'


class Tiger(Mammal):
    _allowed_foods = ['Meat']
    _weight_multiplier = 1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'ROAR!!!'
