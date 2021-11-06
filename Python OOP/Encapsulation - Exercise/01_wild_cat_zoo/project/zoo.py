class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.budget = budget
        self.animal_capacity = animal_capacity
        self.workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        self.__budget = value

    @property
    def animal_capacity(self):
        return self.__animal_capacity

    @animal_capacity.setter
    def animal_capacity(self, value):
        self.__animal_capacity = value

    @property
    def workers_capacity(self):
        return self.__workers_capacity

    @workers_capacity.setter
    def workers_capacity(self, value):
        self.__workers_capacity = value

    def add_animal(self, animal, price):
        if self.budget < price:
            return "Not enough budget"

        if len(self.animals) == self.animal_capacity:
            return "Not enough space for animal"

        self.animals.append(animal)
        self.budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = 0
        for worker in self.workers:
            salaries += worker.salary

        if self.budget < salaries:
            return "You have no budget to pay your workers. They are unhappy"

        self.budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {self.budget}"

    def tend_animals(self):
        total_money_for_care = 0
        for animal in self.animals:
            total_money_for_care += animal.money_for_care

        if self.budget < total_money_for_care:
            return "You have no budget to tend the animals. They are unhappy."

        self.budget -= total_money_for_care
        return f"You tended all the animals. They are happy. Budget left: {self.budget}"

    def profit(self, amount):
        self.budget += amount

    def animals_status(self):
        result = [f'You have {len(self.animals)} animals']
        lions = [f'----- {len([animal for animal in self.animals if animal.__class__.__name__ == "Lion"])} Lions:']
        tigers = [f'----- {len([animal for animal in self.animals if animal.__class__.__name__ == "Tiger"])} Tigers:']
        cheetahs = [f'----- {len([animal for animal in self.animals if animal.__class__.__name__ == "Cheetah"])} Cheetahs:']

        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                lions.append(repr(animal))
            elif animal.__class__.__name__ == 'Tiger':
                tigers.append(repr(animal))
            elif animal.__class__.__name__ == 'Cheetah':
                cheetahs.append(repr(animal))

        return '\n'.join(result + lions + tigers + cheetahs)

    def workers_status(self):
        result = [f'You have {len(self.workers)} workers']
        keepers = [f'----- {len([worker for worker in self.workers if worker.__class__.__name__ == "Keeper"])} Keepers:']
        caretakers = [f'----- {len([worker for worker in self.workers if worker.__class__.__name__ == "Caretaker"])} Caretakers:']
        vets = [f'----- {len([worker for worker in self.workers if worker.__class__.__name__ == "Vet"])} Vets:']
        for worker in self.workers:
            if worker.__class__.__name__ == 'Keeper':
                keepers.append(repr(worker))
            elif worker.__class__.__name__ == 'Caretaker':
                caretakers.append(repr(worker))
            elif worker.__class__.__name__ == 'Vet':
                vets.append(repr(worker))

        return '\n'.join(result + keepers + caretakers + vets)
