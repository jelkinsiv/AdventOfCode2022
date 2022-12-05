data_file = open("Day 5/5_data.txt", "r")

stacks_count = 9
stacks = [[] for i in range(stacks_count)]
steps = []

for line in data_file:
    if line[0].startswith("m"):
        numbers = [int(i) for i in line.split() if i.isdigit()]
        steps.append(numbers)
        continue

    for x in range(0, stacks_count):
        obj_str = line[x * 4: x * 4 + 4]
        if len(str(obj_str).strip()) == 3:
            obj = str(obj_str).strip()[1]
            stacks[x].append(obj)

for step in steps:
    move_count = step[0]
    source_stack = step[1]
    target_stack = step[2]

    for x in range(move_count):
        # Part 1 
        # stacks[target_stack - 1].insert(0, stacks[source_stack - 1].pop(0))

        # Part 2
        stacks[target_stack - 1].insert(x, stacks[source_stack - 1].pop(0))

for stack in stacks:
    print(stack[0], end="")

print()