class Rectangle:
    def __init__(self, x=0, y=0):
        self.length = x
        self.width = y
    def get_area (self):
        return self.length * self.width

    def get_perimeter (self):
        return (self.length * 2) + (self.width * 2)

    def __repr__(self):
        return "Lenght: " + str(self.length) + " Width: " + str(self.width)

    def __eq__(self, other):
        return self.width == other.width and self.length == other.length

#dddd


r = Rectangle(6,8)
r1 = Rectangle(5,9)
r2 = Rectangle(6,8)
print("Lenght: " + str(r.length))
print("Width: " + str(r.width))
print("Area: " + str(r.get_area()))
print("Perimeter: " + str(r.get_perimeter()))
print("r-> " + str(r))
print("r1-> " + str(r1))
print("r2-> " + str(r2))
print(r == r1)
print(r == r2)