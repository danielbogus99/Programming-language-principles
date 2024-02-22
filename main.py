
def factorSum(x):
    """
        Calculates the sum of prime factors of a given integer.

        :param x: Integer to find the sum of prime factors for.
        :return: Sum of prime factors.
        """
    w = 0
    factorArr = []
    while x > 1:
        for i in range(2, int(x + 1)):
            if x % i == 0:
                w = i
                x = x / w
                break
        if w in factorArr:
            pass
        else:
            factorArr.append(w)
    return sum(factorArr)

def interceptPoint(tuple1, tuple2):
    """
        Calculates the intersection point of two lines.

        :param tuple1: Tuple representing the first line (a1, b1).
        :param tuple2: Tuple representing the second line (a2, b2).
        :return: Intersection point (x, y) or None if lines are parallel.
        """

    a1, b1 = tuple1
    a2, b2 = tuple2

    if a1 == a2:
        return None

    x = (b2 - b1) / (a1 - a2)
    y = a1 * x + b1
    return (x, y)



def onlyPositive(f1):
    """
        Decorator function to ensure the input to a function is always positive.

        :param f1: Function to decorate.
        :return: Decorated function.
        """
    def inner(x):
        if x < 0:
            x *= -1
        return f1(x)

    return inner
def f1(x):
    """
        Simple function that returns x + 1.

        :param x: Input value.
        :return: x + 1.
        """
    return x + 1


def printNumbers(x, y, z):
    """
       Prints numbers from x to y (excluding z).

       :param x: Starting number.
       :param y: Ending number.
       :param z: Number to exclude.
       """
    if(x >= y):
        if (x == z):
            pass
        elif (x == y):
            print(y)
            return
        else:
            print(x)
        printNumbers(x  -1, y, z)
    else:
        if (x == z):
            pass
        elif (x == y):
            print(y)
            return
        else:
            print(x)
        printNumbers(x + 1, y, z)


def listProduct(list1, list2):
    """
        Combines two lists based on element counts.

        :param list1: List of elements.
        :param list2: List of counts corresponding to elements in list1.
        :return: Combined list based on counts.
        """
    list3 = []
    for i in range(len(list1)):
        count = list2[i]
        for j in range(count):
            list3.append(list1[i])
    return list3


def analyze(str):
    """
        Analyzes a string of comma-separated numerical values and counts those greater than or equal to 85.

        :param str: String of comma-separated numerical values.
        :return: Count of numbers greater than or equal to 85.
        """
    count = 0

    num = str.split(',')
    print(num)
    for i in num:
        if float(i) >= 85:
            count += 1

    return count

if __name__ == '__main__':
    x = int(input("please enter a number for factorSum function:"))
    print(f"the factor sum of the number {x} is:", factorSum(x))
    x = float(input("please enter number for only positive function:"))
    g = onlyPositive(f1)
    print("the result is:",g(x))
    x = float(input("please enter numbers to tuple number 1 for function interceptPoint:"))
    y = float(input())
    w = float(input("please enter numbers to tuple number 2 for function interceptPoint:"))
    z = float(input())
    tuple1 = (x,y)
    tuple2 = (w,z)
    print("the result of the function:",interceptPoint(tuple1,tuple2))
    print("please enter 3 number for function printNumbers the first number for start,the second for end,and the number do you want no to print")
    x = int(input())
    y = int(input())
    z = int(input())
    (printNumbers(x,y,z))
    x = int(input(("please enter a size for the lists for the ListProduct function:")))
    print("please enter 2 list")
    print("list 1:")
    list1 = []
    list2 = []
    for i in range(x):
        list1.append(int(input(f"please enter a number:")))
    for i in range(x):
        list2.append(int(input(f"please enter a number:")))
    print(listProduct(list1,list2))
    string = str(input("please enter string with numbers to analyze between every number put ',':"))
    print("the number of grades that higher than 85 are:",analyze(string))


