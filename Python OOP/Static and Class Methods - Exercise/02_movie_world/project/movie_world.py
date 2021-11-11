class MovieWorld:
    _dvd_capacity = 15
    _customer_capacity = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @classmethod
    def dvd_capacity(cls):
        return cls._dvd_capacity

    @classmethod
    def customer_capacity(cls):
        return cls._customer_capacity

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def __get_customer(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer

    def __get_dvd(self, dvd_id):
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                return dvd

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.__get_customer(customer_id)
        dvd = self.__get_dvd(dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return 'DVD is already rented'

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.__get_customer(customer_id)
        dvd = self.__get_dvd(dvd_id)

        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        dvd.is_rented = False
        customer.rented_dvds.remove(dvd)
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        result = []
        for customer in self.customers:
            result.append(customer.__repr__())
        for dvd in self.dvds:
            result.append(dvd.__repr__())

        return '\n'.join(result)


