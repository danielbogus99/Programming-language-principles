rates = {"(‘dollar’ ‘nis’)": 3.82, "(‘euro’,’nis’)": 4.07, "(‘euro’,’dollar’)": 1.06}

class Euro:
    def __init__(self, value):
        self.__value = float(value)

    def __str__(self):
        return f"{self.__value}€"

    def __repr__(self):
        return f"Euro({self.__value})"

    def __add__(self, other):
        return self.amount() + other.amount

    def __sub__(self, other):
        return self.amount() - other.amount()

    def amount(self):
        return float(self.__value * rates["(‘euro’,’nis’)"])

    def getValue(self):
        return self.__value
