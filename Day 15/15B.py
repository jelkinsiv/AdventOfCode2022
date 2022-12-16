from AOCHelpers.vector2 import Vector2
import re
import numpy as np

FILE_NAME = "Day 15/15_data.txt"

class ElfTec:
    def __init__(self, x, y) -> None:
        self.pos = Vector2(x, y)

class Sensor(ElfTec):
    def __init__(self,  x, y, beacon) -> None:
        super().__init__(x, y)
        self.closest_beacon = beacon
        self.scan_size = self.pos.manhattanDistanct(self.closest_beacon.pos)
    
    @property
    def scan_top_y(self):
        return self.pos.y - self.scan_size

    @property
    def scan_bottom_y(self):
        return self.pos.y + self.scan_size 

    def intersects(self, pos: Vector2):
        return self.pos.manhattanDistanct(pos) < self.scan_size

    def __repr__(self) -> str:
        return f"p:{self.pos.x}/{self.pos.y} ss:{self.scan_size} cb:{self.closest_beacon.pos.x}/{self.closest_beacon.pos.y}"

class Beacon(ElfTec):
    def __init__(self,  x, y) -> None:
        super().__init__(x, y)

sensors = np.array([])
beacons = np.array([])
data = [[data for data in line.split(': ')] for line in open(FILE_NAME, "r").read().split('\n')]
sensor_data, beacon_data = zip(*data)
for sensor_string, beacon_string in zip(sensor_data, beacon_data):
    bx, by = map(int, re.findall('-?[0-9]+', beacon_string))
    beacon = Beacon(bx, by)
    beacons = np.append(beacons, beacon)
    sx, sy = map(int, re.findall('-?[0-9]+', sensor_string))
    sensors = np.append(sensors, Sensor(sx, sy, beacon))

def checkPositionForIntersect(pos):
    for sensor in sensors:
        if sensor.intersects(pos):
            return True
    return False

def walkPerimeter(sensor: Sensor):
    start_pos = Vector2(sensor.pos.x + sensor.scan_size + 1, sensor.pos.y)
    current_pos = start_pos
    downMove = Vector2(-1, 1)
    leftMove = Vector2(-1, -1)
    upMove = Vector2(1, -1)
    rightMove = Vector2(1, 1)
    perimeter_vectors = []
    
    while current_pos.x != sensor.pos.x:
        perimeter_vectors.append(current_pos)
        current_pos += downMove
    while current_pos.y != sensor.pos.y:
        perimeter_vectors.append(current_pos)
        current_pos += leftMove
    while current_pos.x != sensor.pos.x:
        perimeter_vectors.append(current_pos)
        current_pos += upMove
    while current_pos.y != sensor.pos.y:
        perimeter_vectors.append(current_pos)
        current_pos += rightMove

    for pos in perimeter_vectors:
        if pos.y < 4_000_000 and pos.x < 4_000_000 and pos.y > 0 and pos.x > 0:
            if not checkPositionForIntersect(pos):
                print(pos.x * 4_000_000 + pos.y)
                return True
    else:
        return False

for i, sensor in enumerate(sensors):
    print(f"Checking Senson {i}")
    walkPerimeter(sensor)