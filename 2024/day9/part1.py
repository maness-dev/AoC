from time import perf_counter_ns

data: list[str] = []
with open("2024/day9/test_data.txt", "r") as file:
    for line in file:
        data.append(line.strip())


def create(line):
    new_line = []
    num_ind = 0
    for ind, char in enumerate(line):
        if ind % 2:
            new_line.extend(["." for _ in range(0, int(char))])
        else:
            new_line.extend([f"{num_ind}" for _ in range(0, int(char))])
            num_ind += 1
    return new_line


def sort(line):
    num_inds = []
    space_inds = []
    first_num = True
    for ind, char in enumerate(line):
        if first_num and char == ".":
            first_num = False
        elif first_num:
            continue

        if char == ".":
            space_inds.append(ind)
        else:
            num_inds.append((ind, char))

    num_inds.reverse()
    for num_ind in num_inds:
        if set(list("".join(line).partition(".")[2])) == set("."):
            break
        line[space_inds.pop(0)] = num_ind[1]
        line[num_ind[0]] = "."

    return line


def sum(line):
    total = 0
    for ind, char in enumerate(line):
        if char != ".":
            total += int(char) * ind
        else:
            break
    return total


start = perf_counter_ns()
line = create(data[0])
print(line)
line = sort(line)
print(line)
total = sum(line)
print(total)
