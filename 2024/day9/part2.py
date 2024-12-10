from copy import deepcopy


data: list[str] = []
with open("2024/day9/test_data.txt", "r") as file:
    for line in file:
        data.append(line.strip())


def create(line):
    file_spaces = []
    num_ind = 0
    for ind, char in enumerate(line):
        if ind % 2:
            spaces = ["." for _ in range(0, int(char))]
            if len(spaces) > 0:
                file_spaces.append(spaces)
        else:
            file_spaces.append([f"{num_ind}" for _ in range(0, int(char))])
            num_ind += 1
    return file_spaces


def sort(file_spaces: list[list[str]]):
    reverse = deepcopy(file_spaces)
    reverse.reverse()
    for ind, file in enumerate(reverse):
        if ind == len(reverse) - 1:
            continue
        if file[0] == ".":
            continue

        for sub_ind, sub in enumerate(file_spaces):
            if (
                sub[0] == "."
                and len(sub) >= len(file)
                and sub_ind < file_spaces.index(file)
            ):
                replace = ["." for _ in range(0, len(file))]
                old_index = file_spaces.index(file)
                if file_spaces[old_index - 1][0] == ".":
                    file_spaces[old_index - 1].extend(replace)
                    if old_index + 1 < len(file_spaces):
                        if file_spaces[old_index + 1][0] == ".":
                            file_spaces[old_index - 1].extend(
                                file_spaces[old_index + 1]
                            )
                        file_spaces.pop(old_index + 1)
                    file_spaces.pop(old_index)
                elif (
                    old_index + 1 < len(file_spaces)
                    and file_spaces[old_index + 1][0] == "."
                ):
                    file_spaces[old_index + 1].extend(replace)
                    file_spaces.pop(old_index)
                else:
                    file_spaces[old_index] = replace

                filler = ["." for _ in range(len(file), len(sub))]
                new = file_spaces[:sub_ind]
                new.append(file)
                if len(filler) > 0:
                    new.append(filler)
                new.extend(file_spaces[sub_ind + 1 :])
                file_spaces = new
                break

    new = [x for y in file_spaces for x in y]

    return new


def sum(line):
    total = 0
    for ind, char in enumerate(line):
        if char != ".":
            total += int(char) * ind

    return total


file_spaces = create(data[0])
print(file_spaces)
sorted = sort(file_spaces)
print(sorted)
total = sum(sorted)
print(total)
