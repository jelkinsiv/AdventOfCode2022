from ast import literal_eval
from functools import cmp_to_key

FILE_NAME = "Day 13/13_data.txt"

def compare_data(start_left_data, start_right_data) -> int:
    for left, right in zip(start_left_data, start_right_data):
        match(isinstance(left, int), isinstance(right, int)):
            case True, True:
                if left == right:
                    continue
                elif left < right:
                    return -1
                else:
                    return 1
            case True, False:
                left = [left]
            case False, True:
                right = [right]

        result = compare_data(left, right)
        if result == 0: continue
        return result

    if len(start_left_data) < len(start_right_data): 
        return -1
    elif len(start_left_data) > len(start_right_data): 
        return 1
    else:                 
        return 0

# Part A
packet_pairs = [[literal_eval(pair) for pair in packet.splitlines()] for packet in open(FILE_NAME, "r").read().split('\n\n')]
correct_comparisons = 0

for index, pair in enumerate(packet_pairs, start=1):
    result = compare_data(pair[0], pair[1])
    if result < 0:
        correct_comparisons += index

print(correct_comparisons)

# Part B
key1 = [[2]]
key2 = [[6]]
lines = [literal_eval(packet) for packet in open(FILE_NAME, "r").read().splitlines() if packet != '']
lines.extend([key1, key2])

ordered_data = sorted(lines, key=cmp_to_key(lambda l, r: compare_data(l,r)))
key_score = (ordered_data.index([[2]]) + 1) * (ordered_data.index([[6]]) + 1)

print(key_score)