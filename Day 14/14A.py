import numpy as np
from ast import literal_eval

FILE_NAME = "Day 14/14_data.txt"

class Tile:
    def __init__(self, x, y, collidable, char) -> None:
        self.x = x
        self.y = y
        self.isCollidable = collidable
        self.char = char

    def setWall(self):
        self.isCollidable = True
        self.char = "█"
    
    def setSand(self):
        self.isCollidable = True
        self.char = "░"
        
class Map:
    def __init__(self, width, height, x_offset, y_offset) -> None:
        
        self.tiles = [[None] * width for _ in range(height)]
        self.width = width
        self.height = height
        self.x_offset = x_offset
        self.y_offset = y_offset

        for y in range(self.height):
            for x in range(self.width):
                self.tiles[y][x] = Tile(x + self.x_offset, y + self.y_offset, False, '·')

    def loadObstacles(self, paths):
        for path in paths:
            for i in range(len(path) - 1):
                self.addLine(path[i], path[i + 1])
                print()
            print()

    def addLine(self, start_point, end_point):
        line_x  = end_point[0] - start_point[0] 
        line_y =  end_point[1] - start_point[1]

        if line_x == 0:
            length = line_y + 1 if line_y > 0 else line_y - 1
            step = 1 if line_y > 0 else -1
            for y in range(0,length, step):
                nx, ny  = start_point[0] - self.x_offset, start_point[1] + y - self.y_offset
                self.tiles[ny][nx].setWall()

        if line_y == 0:
            length = line_x + 1 if line_x > 0 else line_x - 1
            step = 1 if line_x > 0 else -1
            for x in range(0,length, step):
                nx, ny = start_point[0] + x - self.x_offset, start_point[1] - self.y_offset
                self.tiles[ny][nx].setWall()

    def drawMap(self):
        for y in range(self.height):
            for x in range(self.width):
                print(f'{self.tiles[y][x].char}', end='')
            print()

class Sand:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.isFalling = True
    
    def moveTo(self, x, y):
        self.x = x
        self.y = y

max_x = 0
max_y = 0
min_x = 1000
min_y = 0

lines = [[literal_eval(segment) for segment in line.split("->")] for line in open(FILE_NAME, "r").read().split('\n')]
line_paths = np.array(lines)

for line in line_paths:
    for segment_point in line:
        max_x = segment_point[0] if segment_point[0] > max_x else max_x
        min_x = segment_point[0] if segment_point[0] < min_x else min_x
        max_y = segment_point[1] if segment_point[1] > max_y else max_y
        min_y = segment_point[1] if segment_point[1] < min_y else min_y

MAP_WIDTH = max_x - min_x + 1
MAP_HEIGHT = max_y - min_y + 1

map = Map(MAP_WIDTH, MAP_HEIGHT, min_x, min_y)
map.loadObstacles(line_paths)
sand_emitter = (500, 0)

run_simulation = True
sand_count = 0
sand = Sand(500, 0)
while run_simulation:
    sand.moveTo(sand_emitter[0], sand_emitter[1])
    sand.isFalling = True
    while sand.isFalling:
        if (sand.y - map.y_offset + 1) > map.height - 1:
            run_simulation = False
            sand.isFalling = False
            break
        down_tile: Tile = map.tiles[sand.y - map.y_offset + 1][sand.x - map.x_offset]
        left_down_tile: Tile = map.tiles[sand.y - map.y_offset + 1][sand.x - map.x_offset - 1]
        right_down_tile: Tile = map.tiles[sand.y - map.y_offset + 1][sand.x - map.x_offset + 1]
        if not down_tile.isCollidable:
            sand.moveTo(down_tile.x, down_tile.y)
        elif not left_down_tile.isCollidable:
            sand.moveTo(left_down_tile.x, left_down_tile.y)
        elif not right_down_tile.isCollidable:
            sand.moveTo(right_down_tile.x, right_down_tile.y)
        else:
            map.tiles[sand.y - map.y_offset][sand.x - map.x_offset].setSand()
            sand.isFalling = False
    sand_count += 1

map.drawMap()
print(f"INTO THE ABYSS: {sand_count - 1}")
print()