class C:
    pass


obj = C()

class Rectangle:
    default_color = "green"

    def __init__(self, width, height):
        self.width = width
        self.height = height
# print(Rectangle.default_color)
r1 = Rectangle(1, 2)
r2 = Rectangle(10, 20)

r1.default_color = "blue"
Rectangle.default_color = "red"
print(r1.default_color, r2.default_color)
print(Rectangle.default_color)