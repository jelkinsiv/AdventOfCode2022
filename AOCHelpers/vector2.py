from math import sqrt

class Vector2():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def manhattanDistanct(self, vector: 'Vector2'):
        return abs(self.x - vector.x) + abs(self.y - vector.y)

    def distance(self, vector: 'Vector2'):
        difference = self - vector
        return sqrt(difference.x ** 2 + difference.y ** 2)
    
    def __repr__(self) -> str:
        return f"{self.x},{self.y}"

    def __add__(self, vector: 'Vector2'):
        return Vector2(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector: 'Vector2'):
        return Vector2(self.x - vector.x, self.y - vector.y)

    def __eq__(self, vector: 'Vector2') -> bool:
        return (self.x == vector.x and self.y == vector.y)