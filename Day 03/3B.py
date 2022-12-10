import string

total_score = 0

data_file = open("Day 3/3_data.txt", "r")
lines = data_file.readlines()
data_file.close

for x in range(0, len(lines), 3):
    bag1, bag2, bag3 = set(list(lines[x].strip())), set(list(lines[x + 1].strip())), set(list(lines[x + 2].strip())), 
    badge = [item for item in bag1 if item in bag2 and item in bag3]
    
    total_score += string.ascii_letters.index(str(badge[0])) + 1

print(total_score)