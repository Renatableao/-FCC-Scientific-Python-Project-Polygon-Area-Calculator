class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
    
  def set_width(self, width):
    self.width = width
    return self.width

  def set_height(self, height):
    self.height = height
    return self.height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      return ("*" * self.width + "\n") * self.height

  def get_amount_inside(self, shape):
    amount = int(self.get_area() / shape.get_area())
    return amount


class Square(Rectangle):
  
  def __init__(self, side):
     super().__init__(side, side)

  def __str__(self):
    return f"Square(side={self.height})"

  def set_side(self, side):
    super().set_height(side)
    super().set_width(side)

  def set_width(self, width):
    self.set_side(width)
    
  def set_height(self, height):
    self.set_side(height)


