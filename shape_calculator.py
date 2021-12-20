
# Rectangle class
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):

        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""
        for i in range(self.height):
            for j in range(self.width):
                picture += "*"
            picture += "\n"
        return picture

    def get_amount_inside(self, shape):

        return (self.width // shape.width)*(self.height // shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

# Square class, objects with attributes and methods inherated from Rectangle class
class Square(Rectangle):

    def __init__(self, length):
        self.height = self.width = length

    def set_width(self, width):
        self.width = self.height = width

    def set_height(self, height):
        self.width = self.height = height

    def set_side(self, length):
        self.width = self.height = length

    def __str__(self):
        return f"Square(side={self.width})"
