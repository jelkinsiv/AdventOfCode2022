lines = [line.strip() for line in open("Day 8/8_data.txt", "r").read().split('\n')]

MAP_WIDTH = len(lines[0])
MAP_HEIGHT = len(lines)

trees = [[None] * MAP_WIDTH for _ in range(MAP_HEIGHT)]

class Tree():
    def __init__(self, x, y, height) -> None:
        self.x = x
        self.y = y
        self.height = height
        self.isVisible = False
        self.scenicValue = 0
        pass

    def __repr__(self) -> str:
        return f"{self.height}({self.scenicValue})"

    @property
    def isEdge(self):
        if (self.x == 0 or self.x == MAP_HEIGHT - 1) or (self.y == 0 or self.y == MAP_HEIGHT - 1) :
            return True
        return False
        
def processToEdge(trees, edge_x = 0, edge_y = 0):
    if edge_y != 0:
        for x in range(MAP_WIDTH):
            is_negative = True if edge_y < 0 else False
            tallest_tree = trees[MAP_HEIGHT - 1][x] if is_negative else trees[0][x]
            y_start = MAP_HEIGHT - 1 if is_negative else 0
            y_end = 0 if is_negative else MAP_HEIGHT
            y_step = -1 if is_negative else 1

            for y in range(y_start, y_end, y_step):
                if trees[y][x].height > tallest_tree.height:
                    trees[y][x].isVisible = True
                    tallest_tree = trees[y][x]
    elif edge_x != 0:
        for y in range(MAP_HEIGHT):
            is_negative = True if edge_x < 0 else False
            tallest_tree = trees[y][MAP_WIDTH - 1] if is_negative else trees[y][0]
            x_start = MAP_WIDTH - 1 if is_negative else 0
            x_end = 0 if is_negative else MAP_WIDTH
            x_step = -1 if is_negative else 1

            for x in range(x_start, x_end, x_step):
                if trees[y][x].height > tallest_tree.height:
                    trees[y][x].isVisible = True
                    tallest_tree = trees[y][x]

def findDistanceToNextVisibleTree(search_x, search_y, current_tree):
    if search_x != 0:
        is_negative = True if search_x < 0 else False

        x_start = current_tree.x - 1 if is_negative else current_tree.x + 1
        x_end = 0 if is_negative else MAP_WIDTH
        x_step = -1 if is_negative else 1

        for x in range(x_start, x_end, x_step):
            tree = trees[current_tree.y][x]
            if tree.height >= current_tree.height:
                return abs(current_tree.x - tree.x)

        return current_tree.x if is_negative else abs(current_tree.x - MAP_WIDTH) - 1
    elif search_y != 0:
        is_negative = True if search_y < 0 else False

        y_start = current_tree.y - 1 if is_negative else current_tree.y + 1
        y_end = 0 if is_negative else MAP_HEIGHT
        y_step = -1 if is_negative else 1

        for y in range(y_start, y_end, y_step):
            tree = trees[y][current_tree.x]
            if tree.height >= current_tree.height:
                return abs(current_tree.y - tree.y)

        return current_tree.y if is_negative else abs(current_tree.y - MAP_HEIGHT) - 1

def calculateScenicValues():
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            current_tree = trees[y][x]
            if not (current_tree.isVisible or current_tree.isEdge):
                continue

            nScore = findDistanceToNextVisibleTree( 0, -1, current_tree)
            sScore = findDistanceToNextVisibleTree( 0,  1, current_tree)
            wScore = findDistanceToNextVisibleTree(-1,  0, current_tree)
            eScore = findDistanceToNextVisibleTree( 1,  0, current_tree)

            current_tree.scenicValue = nScore * sScore * wScore * eScore

for y in range(MAP_HEIGHT):
    for x in range(MAP_WIDTH):
        trees[y][x] = Tree(x, y, int(lines[y][x]))

processToEdge(trees, edge_y=-1)
processToEdge(trees, edge_y=1)
processToEdge(trees, edge_x=-1)
processToEdge(trees, edge_x=1)

calculateScenicValues()

# Part A
visible_trees = [tree for sub in trees for tree in sub if tree.isVisible or tree.isEdge]
print(len(visible_trees))

# Part B
scenic_tree = sorted([tree for sub in trees for tree in sub if tree.scenicValue > 0], key=lambda t: t.scenicValue, reverse=True)[0]
print(scenic_tree.scenicValue)