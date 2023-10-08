from dataclasses import dataclass


@dataclass(order=True)
class Point:
    x: int
    y: int


@dataclass
class Rectangle:
    point: Point
    height: float
    width: float

    def __post_init__(self):
        assert self.height > 0 and self.width > 0, 'Height and width of rectangle have to be positive'

    @property
    def square(self):
        return self.height * self.width

    @property
    def perimeter(self):
        return 2 * (self.height + self.width)


class Square(Rectangle):
    def __init__(self, point: Point, side: float):
        super().__init__(point, side, side)
