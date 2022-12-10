data_file = open("Day 2/2_data.txt", "r")

possible_plays = "ABC"
possible_responses = "XYZ"

total_score = 0

for line in data_file:
    play, response = [word.strip() for word in line.split(" ", 1)]

    play_index = possible_plays.index(play);
    response_index = possible_responses.index(response)

    total_score += response_index * 3

    if response_index == play_index == 0:
        total_score += 3
    elif response_index == play_index == 2:
        total_score += 1
    else:
        total_score += play_index + response_index

print(total_score)