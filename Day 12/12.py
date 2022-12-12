import string

FILE_NAME = "Day 12/12_data_test.txt"
lines = [lines.strip() for lines in open(FILE_NAME, "r").read().split('\n')]

MAP_HEIGHT = len(lines)
MAP_WIDTH = len(lines[0])

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
                tile = map[y][x]
                print_string = ''
                if tile == self.start_tile:
                    print_string = f"({tile.height:2})"
                elif tile == self.end_tile:
                    print_string = f"[{tile.height:2}]"
                else:
                    print_string = f" {tile.height:2} "
                print(f"{print_string}", end='')
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

        return valid_heights


map = Map()
walker = Walker(map.start_tile.x, map.start_tile.y)



while walker.x != map.end_tile.x and walker.y != map.end_tile.y:
    valid_tiles = map.getValidTiles(walker.x, walker.y)
    target_tile = map.tileTowards

    print()
        # find adjecent tiles
        # check valid
# find one that is closer to end tile
# move