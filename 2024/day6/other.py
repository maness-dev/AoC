from copy import deepcopy


data = []
with open("2024/day6/data.txt", "r") as file:
    data = [x.strip() for x in file.readlines()]
dup = deepcopy(data)

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


total = 0
paths = []
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
    else:
        if loc not in paths:
            paths.append(loc)
            total += 1
        line = list(dup[line_ind])
        line[col_ind] = "X"
        dup[line_ind] = "".join(line)

        line_ind += movement[0]
        col_ind += movement[1]

    # print("\n".join(dup))

print(total)
