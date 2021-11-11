import calendar


class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        date = date.split('.')
        creation_year = int(date[2])
        creation_month = calendar.month_name[int(date[1])]
        return cls(name, id, creation_year, creation_month, age_restriction)

    def __repr__(self):
        if self.is_rented:
            status = 'rented'
        else:
            status = 'not rented'
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {status}"
