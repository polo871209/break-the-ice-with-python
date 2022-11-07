# Q41
def q41(s):
    return s**2
# print(list(map(q41, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Q42
def q42(lst):
    return list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, lst)))


# Q43
def q43():
    return list(filter(lambda x: x % 2 == 0, range(1, 21)))


# Q44
def q44():
    return list(map(lambda x: x**2, range(1, 21)))


# Q45
class American():
    @staticmethod
    def printNationality():
        print("This is America.")


# american = American()
# american.printNationality()


# Q46
class American():
    pass


class NewYorker(American):
    pass


# american = American()
# newyorker = NewYorker()
# print(isinstance(newyorker, American))


# Q47
class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return 3.1416*(self.radius**2)


# circle = Circle(5)
# print(circle.area())


# Q48
class Rectangle ():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length*self.width


# rectangle = Rectangle(10, 5)
# print(rectangle.area())


# Q49
class Shape():

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, l=0):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length


# square = Square(5)
# print(square.area())
# print(Square().area())


# Q50
raise RuntimeError('something wrong')
