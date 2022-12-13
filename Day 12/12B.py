import string
from queue import Queue

FILE_NAME = "Day 12/12_data.txt"
lines = [lines.strip() for lines in open(FILE_NAME, "r").read().split('\n')]

MAP_HEIGHT = len(lines)
MAP_WIDTH = len(lines[0])
possible_starts = []

class PathFinder():
    def __init__(self, map) -> None:
        self.map = map

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def legal_neighbors(self, current):
        neighbors = []
        for new_position in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            node_position = (current[0] + new_position[0], current[1] + new_position[1])
            if (node_position[0] > MAP_WIDTH - 1) or (node_position[0] < 0) or (node_position[1] > MAP_HEIGHT - 1) or (node_position[1] < 0):
                continue
            
            current_tile = map.tiles[current[1]][current[0]]
            check_tile = map.tiles[node_position[1]][node_position[0]]
            valid_heights = [i for i in range(1, current_tile.height + 2)]
            if not (check_tile.height in valid_heights):
                continue

            neighbors.append(node_position)
        return neighbors

    def h_search(self, x, y, tx, ty):
        start = (x, y)
        goal = (tx, ty)

        frontier = Queue()
        frontier.put(start)

        came_from = dict() 
        came_from[start] = None

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                current = goal
                path = []
                while current != start: 
                    path.append(current)
                    current = came_from[current]
                return path

            for next in self.legal_neighbors(current):
                if next not in came_from:
                    priority = self.heuristic(goal, next)
                    frontier.put(next, priority)
                    came_from[next] = current

class Tile():
    def __init__(self, x, y, height) -> None:
        self.x = x
        self.y = y
        self.height = height

class Map:
    def __init__(self) -> None:
        self.tiles = [[None] * MAP_WIDTH for _ in range(MAP_HEIGHT)]
        self.start_tile: Tile = None
        self.end_tile: Tile = None 
        self.possible_starts = []

        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                point_height = lines[y][x]
                if point_height == 'S' or point_height == 'a':
                    tile = Tile(x, y, 1)
                    self.possible_starts.append(tile)
                    self.tiles[y][x] = tile
                elif point_height == 'E':
                    self.end_tile = Tile(x, y, 26)
                    self.tiles[y][x] = self.end_tile
                else:
                    self.tiles[y][x] = Tile(x, y, string.ascii_lowercase.index(point_height) + 1)

    def draw_map(self, path):
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                tile = self.tiles[y][x]
                if (x, y) in path:
                    print(f"#", end='')
                else:
                    print(f"{string.ascii_letters[tile.height - 1]}", end='')
            print()

map = Map()
pathfinder = PathFinder(map)
path_lens = []
for i, start in enumerate(map.possible_starts):
    print(f"Testing start {i}/{len(map.possible_starts)}")
    path = pathfinder.h_search(start.x, start.y, map.end_tile.x, map.end_tile.y)
    if path:
        path_lens.append(len(path))
path_lens.sort()
print(path_lens[0])