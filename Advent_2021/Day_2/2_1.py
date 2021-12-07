txt = open('input.txt', 'r')
directions = txt.read().split('\n')
txt.close()


def get_directions(file_input):
    count = 0
    f = 0
    d = 0
    # u = 0
    final = 0
    while count < len(file_input):
        for direction in file_input:
            count += 1

            if direction.rstrip(direction[-1]) == "forward ":
                f += int(direction[-1])
            elif direction.rstrip(direction[-1]) == "down ":
                d += int(direction[-1])
            elif direction.rstrip(direction[-1]) == "up ":
                d -= int(direction[-1])

    print(f)
    print(d)

    final = d * f
    print(final)

    print()

    print("Count")
    print(count)


get_directions(directions)
