data_file = open("Day 5/5_data.txt", "r")
stacks_lines, instructions_lines = [lines.split("\n") for lines in data_file.read().split('\n\n')]
stacks_count = int(stacks_lines[-1].strip()[-1])
stacks = [[] for _ in range(stacks_count)]
steps = []
is_cm_9001 = True

for line in instructions_lines:
    numbers = [int(i) for i in line.split() if i.isdigit()]
    steps.append(numbers)

for line in stacks_lines:
    for x in range(stacks_count):
        obj_str = line[x * 4: x * 4 + 4]
        if len(str(obj_str).strip()) == 3:
            obj = str(obj_str).strip()[1]
            stacks[x].append(obj)

for step in steps:
    move_count, source_stack, target_stack = step

    for x in range(move_count):
        stacks[target_stack - 1].insert(x if is_cm_9001 else 0, stacks[source_stack - 1].pop(0))

print(f"{''.join([stack[0] for stack in stacks])}")