txt = open('input.txt', 'r')
directions = txt.read().split('\n')
txt.close()


def get_directions(file_input):
    count = 0
    f = 0
    aim = 0
    depth = 0
    final = 0
    while count < len(file_input):
        for direction in file_input:
            count += 1

            if direction.rstrip(direction[-1]) == "forward ":
                f += int(direction[-1])
                depth = depth + (aim * int(direction[-1]))
            elif direction.rstrip(direction[-1]) == "down ":
                aim += int(direction[-1])
            elif direction.rstrip(direction[-1]) == "up ":
                aim -= int(direction[-1])

    final = depth * f
    print(final)


get_directions(directions)
