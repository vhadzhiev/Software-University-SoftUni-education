class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    @staticmethod
    def __get_object_by_id(objects, obj_id):
        for obj in objects:
            if obj.id == obj_id:
                return obj

    def subscription_info(self, subscription_id):
        subscription = self.__get_object_by_id(self.subscriptions, subscription_id)
        customer = self.__get_object_by_id(self.customers, subscription.customer_id)
        trainer = self.__get_object_by_id(self.trainers, subscription.trainer_id)
        plan = self.__get_object_by_id(self.plans, subscription.exercise_id)
        equipment = self.__get_object_by_id(self.equipment, plan.equipment_id)

        result = [subscription, customer, trainer, equipment, plan]

        return '\n'.join(str(x) for x in result)