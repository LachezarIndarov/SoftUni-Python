from calendar import month_name


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        separated_dates = cls.separate_date(date)
        return cls(name, id, int(separated_dates[2]), month_name[int(separated_dates[1])], age_restriction)

    def check_if_rented(self):
        if self.is_rented is True:
            return 'rented'
        else:
            return 'not rented'

    @staticmethod
    def separate_date(date: str):
        date_list = date.split('.')
        return date_list

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year})" \
               f" has age restriction {self.age_restriction}. Status: {self.check_if_rented()}"

