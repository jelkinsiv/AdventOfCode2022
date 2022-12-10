data_file = open("Day 4/4_data.txt", "r")
contained_pairs = 0

def doesContain(array1, array2):
    if (array1[0] <= array2[0]) and (array1[1] >= array2[1]):
        return True
    return False

for line in data_file:
    first_elf, second_elf = [list(map(int,word.strip().split("-"))) for word in line.split(",", 1)]

    if doesContain(first_elf, second_elf) or doesContain(second_elf, first_elf):
        contained_pairs += 1

print(contained_pairs)