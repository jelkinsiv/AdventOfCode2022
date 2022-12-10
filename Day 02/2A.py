data_file = open("Day 2/2_data.txt", "r")

possible_plays = "ABC"
possible_responses = "XYZ"

total_score = 0

for line in data_file:
    play, response = [word.strip() for word in line.split(" ", 1)]

    play_index = possible_plays.index(play);
    response_index = possible_responses.index(response)

    total_score += response_index + 1

    #check for draw
    if  play_index == response_index :
        total_score += 3
    
    #check win
    elif (play_index == 0 and response_index == 1) or \
        (play_index == 1 and response_index == 2) or \
        (play_index == 2 and response_index == 0):
        total_score += 6

print(total_score)