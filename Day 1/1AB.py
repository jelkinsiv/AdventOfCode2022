elves_totals = []
current_elf = 0
data_file = open("1_data.txt", "r")

for line in data_file:
    if line == "\n":
        elves_totals.append(current_elf)
        current_elf = 0
    else: 
        current_elf += int(line)

elves_totals.sort(reverse=True)

# Part 1
print(sum(elves_totals[0:1]))

# Part 2
print(sum(elves_totals[0:3]))