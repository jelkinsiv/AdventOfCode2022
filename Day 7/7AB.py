data_file = open("Day 7/7_data.txt", "r")
top_dir = None

# Part A
max_file_size = 100000

# Part B
min_system_size_needed = 30000000
file_system_size = 70000000

class Dir:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.children = []

    @property
    def size(self):
        size = 0
        for child in self.children:
            if type(child) == ElfFile:
                size += child.size
            elif type(child) == Dir:
                size += child.size
        return size

class ElfFile:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = int(size)

def parseDataFile(top_dir):
    top_dir = Dir("~", None)
    current_dir = top_dir
    current_dir.children.append(Dir("/", current_dir))

    for line in [line.strip() for line in data_file]:
        if line.startswith('$'):
            command = line.strip().split(' ')
            if command[1] == 'cd':
                if command[2] == "..":
                    current_dir = current_dir.parent
                else:
                    current_dir = next(d for d in current_dir.children if d.name == command[2])
        elif line.startswith('dir'):
            new_dir = Dir(line.strip().split(' ')[1], current_dir)
            current_dir.children.append(new_dir)
        else:
            file_parts = line.split(" ")
            current_dir.children.append(ElfFile(file_parts[1], file_parts[0]))
    
    return top_dir

def walkDirScore(current_dir, score):
    score += current_dir.size if current_dir.size < max_file_size else 0

    for cd in [cd for cd in current_dir.children if type(cd) == Dir]:
        score = walkDirScore(cd, score)
    
    return score

def walkDirDeletable(current_dir, min_file_size_delete, current_deletable_file_size):
    current_deletable_file_size = min(current_dir.size, current_deletable_file_size) if current_dir.size > min_file_size_delete else current_deletable_file_size

    for cd in [cd for cd in current_dir.children if type(cd) == Dir]:
        current_deletable_file_size = min(walkDirDeletable(cd, min_file_size_delete, current_deletable_file_size), current_deletable_file_size)

    return current_deletable_file_size

top_dir = parseDataFile(top_dir)

# Part A
root_dir = top_dir.children[0]
print(f'PART A: {walkDirScore(root_dir, 0)}')

# Part B
root_dir = top_dir.children[0]
min_file_size_delete = (root_dir.size - file_system_size) + min_system_size_needed
print(f'PART B: {walkDirDeletable(root_dir, min_file_size_delete, root_dir.size)}')