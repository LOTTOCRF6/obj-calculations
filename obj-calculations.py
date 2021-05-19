class Shapes:
    def __init__(self, name, side):
        self.name = name
        self.side = side

    def area(self):
        print("I am a :" + self.name + "\n" + "I have" + self.side + "sides")


obj_shape = Shapes("shape", "so many")
obj_shape.area()


class Rectangle(Shapes):
    def __init__(self, len1, wid1):
        self.length = len1
        self.width = wid1

    def area(self):
        result = self.length * self.width
        return result


obj_book = Rectangle(10, 7)
print(obj_book.area())


class Circle(Shapes):
    def __init__(self, radius1, pi):
        self.radius = radius1
        self.pi = 3.14

    def area(self):
        result = self.radius * self.pi
        return result


obj_book = Circle(15, 10)
print(obj_book.area())


class Triangle(Shapes):
    def __init__(self, base1, height1):
        self.base1 = base1
        self.height1 = height1

    def area(self):
        result = 0.5 * self.base1 * self.height1
        return result


obj_tri = Triangle(8, 4)
setattr(obj_tri, "base1", 5)
setattr(obj_tri, "height1",10)
print(obj_tri.area())





