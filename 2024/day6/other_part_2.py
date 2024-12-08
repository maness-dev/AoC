data = []
with open("2024/day6/test_data.txt", "r") as file:
    data = [x.strip() for x in file.readlines()]

line_ind = 0
col_ind = 0
movement = (-1, 0)

for line_ind, line in enumerate(data):
    if "^" in line:
        col_ind = list(line).index("^")
        break


def change_move():
    global movement
    match movement:
        case (-1, 0):
            movement = (0, 1)
        case (0, 1):
            movement = (1, 0)
        case (1, 0):
            movement = (0, -1)
        case (0, -1):
            movement = (-1, 0)


def get_all_chars(move, search_char):
    global col_ind, line_ind
    loc = (col_ind, line_ind)
    while True:
        loc = (loc[0] + move[0], loc[1] + move[1])
        if loc[0] in range(0, len(data[line_ind])) and loc[1] in range(0, len(data)):
            char = list(data[col_ind + move[0]])[line_ind + move[1]]
            if char == "#":
                break
            elif char == search_char:
                return True
        else:
            break
    return False


def check_around():
    global movement, line_ind, col_ind
    match movement:
        case (-1, 0):
            return get_all_chars((0, 1), "-")
        case (0, 1):
            return get_all_chars((1, 0), "-")
        case (1, 0):
            return get_all_chars((0, -1), "-")
        case (0, -1):
            return get_all_chars((-1, 0), "-")


total = 0
while True:
    loc = (line_ind, col_ind)

    if line_ind in [-1, len(data)] or col_ind in [-1, len(data[0])]:
        break
    pos_char = list(data[line_ind])[col_ind]
    if pos_char == "#":
        line_ind -= movement[0]
        col_ind -= movement[1]
        change_move()
        line_ind += movement[0]
        col_ind += movement[1]
    elif pos_char in ["-", "|"] or check_around():
        line = list(data[line_ind])
        line[col_ind] = "+"
        data[line_ind] = "".join(line)
        line_ind += movement[0]
        col_ind += movement[1]
    else:
        line = list(data[line_ind])
        if movement[0] == 0:
            line[col_ind] = "-"
        else:
            line[col_ind] = "|"
        data[line_ind] = "".join(line)

        line_ind += movement[0]
        col_ind += movement[1]

    print("\n".join(data))
    input()

print(total)
