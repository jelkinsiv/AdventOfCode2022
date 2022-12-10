data_file = open("Day 6/6_data.txt", "r").readlines()[0]
packet_length = 14

for i in range(len(data_file)):
    packet = data_file[i:i + packet_length]
    if (len(set(packet)) == len(packet)):
        print(i + packet_length)
        break