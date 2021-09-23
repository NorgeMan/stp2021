class C:
    pass


obj = C()


class Rectangle:
    def __new__(cls, *args, **kwargs):
        print("Hello from __new__")
        return super().__new__(cls)

    #    default_color = "green"

    def __init__(self, width, height):
        print("Hello from __init__")
        self.width = width
        self.height = height

    def get_width(self):
        return self._width

    def set_width(self, w):
        self._width = w

    def get_height(self):
        return self._height

    def set_width(self, h):
        self._height = h

    def area(self):
        return self.width * self.height


rect = Rectangle(10, 20)

# print(Rectangle.default_color)
# r1 = Rectangle(1, 2)
# r2 = Rectangle(10, 20)
#
# r1.default_color = "blue"
# Rectangle.default_color = "red"


# print(r1.default_color, r2.default_color)
# print(Rectangle.default_color)

# add methods

class MyClass:

    @staticmethod
    def ex_static_method():
        print("static method")

    @classmethod
    def ex_class_method(cls):
        print("class method")

    def ex_method(self):
        print("method")


MyClass.ex_static_method()

MyClass.ex_class_method()

m = MyClass()
m.ex_method()
