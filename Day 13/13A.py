from ast import literal_eval

FILE_NAME = "Day 13/13_data.txt"
packet_pairs = [[literal_eval(pair) for pair in packet.splitlines()] for packet in open(FILE_NAME, "r").read().split('\n\n')]

correct_comparisons = 0
correct_pairs = []

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

for index, pair in enumerate(packet_pairs, start=1):
    result = compare_data(pair[0], pair[1])
    if result < 0:
        correct_comparisons += index
        correct_pairs.append(pair)

print(', '.join([str(i) for i in correct_pairs]))
print(correct_comparisons)
print()