class C:
    pass


obj = C()

class Figure:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.__color = c

    def info(self):
        print("Figure")
        print("Color: " + self.color)

class Rectangle(Figure):
    # def __new__(cls, *args, **kwargs):
    #     print("Hello from __new__")
    #     return super().__new__(cls)

    #    default_color = "green"

    def __init__(self, width, height,color):
        super().__init__(color)
        # print("Hello from __init__")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if h > 0:
            self.__height = h
        else:
            raise ValueError
    #
    # def get_width(self):
    #     return self._width
    #
    # def set_width(self, w):
    #     self._width = w
    #
    # def get_height(self):
    #     return self._height
    #
    # def set_width(self, h):
    #     self._height = h

    def info(self):
        print("Rectangle")
        print("Color: " + self.color)
        print("Width: " + str(self.width))
        print("Height: " + str(self.height))
        print("Area: " + str(self.are()))

    def area(self):
        return self.__width * self.__height


rect = Rectangle(10, 20)
#
# print(rect.get_width())
#
# print(rect._width)
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
