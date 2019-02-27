class Rectangle:
    def __init__(self, x=0, y=0):
        Rectangle.length = x
        Rectangle.width = y
    def get_area (self):
        return self.length * self.width

    def get_perimeter (self):
        return (self.length * 2) + (self.width * 2)

r = Rectangle(6,8)
print ("Lenght: " + str(r.length))
print ("Width: " + str(r.width))
print("Area: " + str(r.get_area()))
print("Perimeter: " + str(r.get_perimeter()))