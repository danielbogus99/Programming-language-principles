rates = {"(‘dollar’ ‘nis’)": 3.82, "(‘euro’,’nis’)": 4.07, "(‘euro’,’dollar’)": 1.06}
from EuroC import Euro
from DollarC import Dollar
from ShekelC import Shekel


def add(a, b):
    return a.amount() + b.amount()


def sub(a, b):
    return a.amount() - b.amount()


def isShekel(types):
    return type(types) == Shekel


def isEuro(types):
    return type(types) == Euro


def isDollar(types):
    return type(types) == Dollar


def apple(operator, a, b):
    if operator == 'add':
        if isShekel(a):
            return Shekel(add(a, b))
        if isEuro(a):
            return Euro(add(a, b) / rates["(‘euro’,’nis’)"])
        if isDollar(a):
            return Dollar(add(a, b) / rates["(‘dollar’ ‘nis’)"])
    if operator == 'sub':
        if isShekel(a):
            return Shekel(sub(a, b))
        if isEuro(a):
            return Euro(sub(a, b) / rates["(‘euro’,’nis’)"])
        if isDollar(a):
            return Dollar(sub(a, b) / rates["(‘dollar’ ‘nis’)"])


def dollar_to_shekel(amounts):
    return amounts.getValue() * 3.82


def euro_to_shekel(amounts):
    return amounts.getValue() * 4.07


def dollar_to_euro(amounts):
    return amounts.getValue() * 1.06


def euro_to_dollar(amounts):
    return amounts.getValue() / 1.06


coercions = {
    (Dollar, 'nis'): dollar_to_shekel,
    (Euro, 'nis'): euro_to_shekel,
}


def coerce_apply(operator_name, a, b):
    ta, tb = type(a), type(b)
    if ta == Dollar:
        a = Shekel(coercions[(ta, 'nis')](a))
    elif tb == Dollar:
        b = Shekel(coercions[(tb, 'nis')](b))
    if ta == Euro:
        a = Shekel(coercions[(ta, 'nis')](a))
    elif tb == Euro:
        b = Shekel(coercions[(tb, 'nis')](b))

    return Shekel(coerce_apply.implementations[(operator_name, ta)](a, b))


coerce_apply.implementations = {('add', Shekel): add, ('add', Dollar): add, ('add', Euro): add,
                                ('sub', Shekel): sub, ('sub', Dollar): sub, ('sub', Euro): sub}
if __name__ == '__main__':
    print(coerce_apply('add', Shekel(50), Dollar(20)))
    print(coerce_apply('add', Dollar(50), Euro(20)))
    print(coerce_apply('sub', Dollar(50), Euro(20)))
