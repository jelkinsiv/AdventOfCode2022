import string

data_file = open("Day 3/3_data_test.txt", "r")
total_score = 0

for line in data_file:
    pouch1, pouch2 = set(list(line[:len(line)//2])), set(list(line[len(line)//2:].strip()))
    mistake = [item for item in pouch1 if item in pouch2]
    total_score += string.ascii_letters.index(str(mistake[0])) + 1

print(total_score)