def get_message_marker(datastream, window_size):
    for i in range(len(datastream) - window_size + 1):
        window = datastream[i : i + window_size]
        seq_start_index = i + window_size
        if len(set(window)) == window_size:
            return seq_start_index

if __name__ == "__main__":
    with open("inputs/input.txt") as file:
        datastream = file.read().strip()

    part_1_ans = get_message_marker(datastream, window_size=4)
    print(part_1_ans)

    part_2_ans = get_message_marker(datastream, window_size=14)
    print(part_2_ans)
