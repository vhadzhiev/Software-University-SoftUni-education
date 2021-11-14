from project.animals.animal import Bird


class Owl(Bird):
    _allowed_foods = ['Meat']
    _weight_multiplier = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Hoot Hoot'


class Hen(Bird):
    _allowed_foods = ['Vegetable', 'Fruit', 'Meat', 'Seed']
    _weight_multiplier = 0.35

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Cluck'
