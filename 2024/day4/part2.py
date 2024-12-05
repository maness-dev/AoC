from copy import deepcopy
import time

now = time.time()
total = 0
data = []
with open("2024/day4/data.txt", "r") as file:
    data = file.readlines()


def search(data):
    found = False
    cp = deepcopy(data)
    for line_ind, line in enumerate(data):
        line = line.strip()
        for m_ind, char in enumerate(line):
            if char != "M":
                continue
            if line_ind > 1:
                # search upleft and upright
                if m_ind > 1:
                    top_of_x = list(data[line_ind - 2])
                    middle_of_x = list(data[line_ind - 1])
                    bottom_of_x = list(data[line_ind])

                    if middle_of_x[m_ind - 1] == "A":  # see if center of X is 'A'
                        if (
                            top_of_x[m_ind - 2] == "S"
                        ):  # see if opposite of current 'M' is 'S'
                            if set([bottom_of_x[m_ind - 2], top_of_x[m_ind]]) == set(
                                ["S", "M"]
                            ):  # validate other 2 points are 'S' and 'M'
                                middle_of_x[m_ind - 1] = "."
                                cp[line_ind - 1] = "".join(middle_of_x)
                                return cp, True

                if m_ind < len(line) - 2:
                    top_of_x = list(data[line_ind - 2])
                    middle_of_x = list(data[line_ind - 1])
                    bottom_of_x = list(data[line_ind])

                    if middle_of_x[m_ind + 1] == "A":  # see if center of X is 'A'
                        if (
                            top_of_x[m_ind + 2] == "S"
                        ):  # see if opposite of current 'M' is 'S'
                            if set([bottom_of_x[m_ind + 2], top_of_x[m_ind]]) == set(
                                ["S", "M"]
                            ):  # validate other 2 points are 'S' and 'M'
                                middle_of_x[m_ind + 1] = "."
                                cp[line_ind - 1] = "".join(middle_of_x)
                                return cp, True

            if line_ind < len(data) - 2:
                if m_ind > 1:
                    top_of_x = list(data[line_ind])
                    middle_of_x = list(data[line_ind + 1])
                    bottom_of_x = list(data[line_ind + 2])

                    if middle_of_x[m_ind - 1] == "A":  # see if center of X is 'A'
                        if (
                            bottom_of_x[m_ind - 2] == "S"
                        ):  # see if opposite of current 'M' is 'S'
                            if set([bottom_of_x[m_ind], top_of_x[m_ind - 2]]) == set(
                                ["S", "M"]
                            ):  # validate other 2 points are 'S' and 'M'
                                middle_of_x[m_ind - 1] = "."
                                cp[line_ind + 1] = "".join(middle_of_x)
                                return cp, True

                if m_ind < len(line) - 2:
                    top_of_x = list(data[line_ind])
                    middle_of_x = list(data[line_ind + 1])
                    bottom_of_x = list(data[line_ind + 2])

                    if middle_of_x[m_ind + 1] == "A":  # see if center of X is 'A'
                        if (
                            bottom_of_x[m_ind + 2] == "S"
                        ):  # see if opposite of current 'M' is 'S'
                            if set([bottom_of_x[m_ind], top_of_x[m_ind + 2]]) == set(
                                ["S", "M"]
                            ):  # validate other 2 points are 'S' and 'M'
                                middle_of_x[m_ind + 1] = "."
                                cp[line_ind + 1] = "".join(middle_of_x)
                                return cp, True

    return cp, found


for ind, line in enumerate(data):
    data[ind] = line.strip()

while True:
    data, found = search(data)
    if found:
        total += 1
    else:
        break
print(total)
print(f"runtime: {time.time()-now}")
