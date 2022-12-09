from math import sqrt 
from numpy import sign

class Vector2D():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def distance(self, vector: 'Vector2D'):
        difference = self - vector
        return sqrt(difference.x ** 2 + difference.y ** 2)
    
    def __repr__(self) -> str:
        return f"{self.x},{self.y}"

    def __add__(self, vector: 'Vector2D'):
        return Vector2D(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector: 'Vector2D'):
        return Vector2D(self.x - vector.x, self.y - vector.y)

class RopeSegment():
    def __init__(self, rope, x, y) -> None:
        self.rope = rope
        self.position = Vector2D(x, y)

class Rope():
    def __init__(self) -> None:
        self.segment_count = 2
        self.segments = [RopeSegment(self, 0, 0) for _ in range(self.segment_count)]
        self.head_segment = self.segments[0]
        self.tail_segment = self.segments[self.segment_count - 1]
        self.tail_history = [Vector2D(0, 0)]

    def updateSegments(self, direction):
        for index, segment in enumerate(self.segments[1:]):
            previous_segment = self.segments[index]
            distance = segment.position.distance(previous_segment.position)
            if abs(distance) >= 2:
                position_offset = previous_segment.position - segment.position
                new_position_delta = Vector2D(sign(position_offset.x), sign(position_offset.y))
                segment.position = Vector2D(segment.position.x + new_position_delta.x, segment.position.y + new_position_delta.y)

    def move(self, velocity, distance):
        for _ in range(distance):
            self.head_segment.position += velocity
            self.updateSegments(velocity)

            if not [history for history in self.tail_history if history.x == rope.tail_segment.position.x and history.y == rope.tail_segment.position.y]:
                self.tail_history.append(rope.tail_segment.position)

def velocityFromDirection(char) -> Vector2D:
    if char.upper() == 'U':
        return Vector2D(x=0, y=-1)
    elif char.upper() == 'D':
        return Vector2D(x=0, y=1)
    elif char.upper() == 'L':
        return Vector2D(x=-1, y=0)
    elif char.upper() == 'R':
        return Vector2D(x=1, y=0)

    return Vector2D(0,0)

lines = [line.strip() for line in open("Day 9/9_data.txt", "r").read().split('\n')]

rope = Rope()
for index, line in enumerate(lines):
    direction_char, distance = line.split(" ")
    rope.move(velocityFromDirection(direction_char), int(distance))

print(len(rope.tail_history))