import string
from math import sqrt
from dataclasses import dataclass
import heapq

FILE_NAME = "Day 12/12_data_test.txt"
lines = [lines.strip() for lines in open(FILE_NAME, "r").read().split('\n')]

MAP_HEIGHT = len(lines)
MAP_WIDTH = len(lines[0])


@dataclass(order=True, eq=True)
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        return (self.x == other.x and self.y == other.y)

class Node():
    def __init__(self, x, y, parent) -> None:
        self.parent = parent
        self.position: tuple = (x , y)

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

class PathFinder():
    def __init__(self, map) -> None:
        self.map = map

    def pathToClosestTarget(self, pos, target):

        end_node = Node(target.x, target.y, None)

        start_node = Node(pos.x, pos.y, None)
        start_node.g = 0
        start_node.h = ((start_node.position[0] - end_node.position[0]) ** 2) + ((start_node.position[1] - end_node.position[1]) ** 2)
        start_node.f = start_node.g + start_node.h 

        open_list = [start_node]
        closed_list = []

        while open_list:
            open_list.sort(key=lambda node: node.f)
            current_node = heapq.heappop(open_list)
            

            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1]
            else:
                print(current_node.g)


            children = []
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                
                if (node_position[0] > MAP_WIDTH - 1) or node_position[0] < 0 or node_position[1] > (MAP_HEIGHT - 1) or node_position[1] < 0:
                    continue

                current_tile = map.tiles[current_node.position[1]][current_node.position[0]]
                check_tile = map.tiles[node_position[1]][node_position[0]]
                valid_heights = [ current_tile.height, current_tile.height + 1]
                if not (check_tile.height in valid_heights):
                    continue

                
                if len([node for node in closed_list if node.position[0] == node_position[0] and node.position[1] == node_position[1]]) <= 0:
                    new_node = Node(node_position[0], node_position[1], current_node)
                    children.append(new_node)

            child:Node
            for child in children:
                child.g = current_node.g + 1
                child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
                child.f = child.g + child.h

                for open_node in open_list:
                    if child.position[0] == open_node.position[0] and child.position[1] == open_node.position[1] and child.g > open_node.g:
                        continue

                open_list.append(child)

            closed_list.append(current_node)

class Tile():
    def __init__(self, x, y, height) -> None:
        self.x = x
        self.y = y
        self.height = height

class Walker():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Map:
    def __init__(self) -> None:
        self.tiles = [[None] * MAP_WIDTH for _ in range(MAP_HEIGHT)]
        self.start_tile: Tile = None
        self.end_tile: Tile = None 

        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                point_height = lines[y][x]
                if point_height == 'S':
                    self.start_tile = Tile(x, y, 0)
                    self.tiles[y][x] = self.start_tile
                elif point_height == 'E':
                    self.end_tile = Tile(x, y, 27)
                    self.tiles[y][x] = self.end_tile
                else:
                    self.tiles[y][x] = Tile(x, y, string.ascii_lowercase.index(point_height) + 1)

    def draw_map(self):
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                tile = self.tiles[y][x]
                print_string = ''
                if tile == self.start_tile:
                    print_string = f"{'SS'}"
                elif tile == self.end_tile:
                    print_string = "EE"
                else:
                    print_string = f"{tile.height:2}"
                print(f"{print_string}", end='.')
            print()
    
    def getValidTiles(self, x, y):
        valid_tiles = []
        valid_heights = [self.tiles[y][x].height, self.tiles[y][x].height + 1]
        if x > 1:
            if self.tiles[x - 1][y].height in valid_heights:
                valid_tiles.append(self.tiles[x - 1][y])
        if x < MAP_WIDTH - 2:
            if self.tiles[x + 1][y].height in valid_heights:
                valid_tiles.append(self.tiles[x + 1][y])
        if y > 1:
            if self.tiles[x][y - 1].height in valid_heights:
                valid_tiles.append(self.tiles[x][y - 1])
        if y < MAP_HEIGHT - 2:
            if self.tiles[x][y + 1].height in valid_heights:
                valid_tiles.append(self.tiles[x][y + 1])

        return valid_tiles


map = Map()
walker = Walker(map.start_tile.x, map.start_tile.y)
pathfinder = PathFinder(map)
path = pathfinder.pathToClosestTarget(walker, map.end_tile)
print(len(path) - 1)
print(path)