from AOCHelpers.vector2 import Vector2
import re
import numpy as np

FILE_NAME = "Day 15/15_data.txt"
CHECK_ROW = 2_000_000

class ElfTec:
    def __init__(self, x, y) -> None:
        self.pos = Vector2(x, y)

class Sensor(ElfTec):
    def __init__(self,  x, y, beacon) -> None:
        super().__init__(x, y)
        self.closest_beacon = beacon
        diff = self.pos - self.closest_beacon.pos
        self.scan_size = abs(diff.x) + abs(diff.y)
    
    @property
    def scan_top_y(self):
        return self.pos.y - self.scan_size

    @property
    def scan_bottom_y(self):
        return self.pos.y + self.scan_size 

    def scanStartXAtLine(self, y):
        return self.pos.x - (self.sizeAtLine(y) // 2) 

    def intersectLine(self, y):
        return (y >= self.scan_top_y) and (y <= self.scan_bottom_y)

    def sizeAtLine(self,y):
        if not self.intersectLine(y): return 0
        intesect_y = abs(self.pos.y - y)
        return 2 * (self.scan_size - intesect_y) + 1

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

sensor_slices = []
for sensor in sensors:
    start_x = sensor.scanStartXAtLine(CHECK_ROW)
    slice_width = sensor.sizeAtLine(CHECK_ROW)
    sensor_slices.append((start_x, slice_width))

max_x = 0
min_x = 1000000000
for x, width in sensor_slices:
    min_x = x if x < min_x else min_x
    max_x = x + width if x + width > max_x else max_x

scan_slice = ["."] * (max_x - min_x)
for slice in sensor_slices:
    for i in range(slice[1] - 1):
        x = slice[0] - min_x + i 
        scan_slice[x - 1 ] = '#'

total = [x for x in scan_slice if x == '#' ]
print(len(total))