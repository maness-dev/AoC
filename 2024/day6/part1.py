import os
from time import perf_counter_ns
import time


data = []
with open("2024/day6/data.txt", "r") as file:
    for line in file:
        data.append(line.strip())

start = 0, 0
for line_ind, line in enumerate(data):
    if "^" in line:
        start = (line_ind, line.index("^"))

direction = "up"


def change_direction(direction):
    match direction:
        case "up":
            direction = "right"
        case "right":
            direction = "down"
        case "down":
            direction = "left"
        case "left":
            direction = "up"
    return direction


def search_up(start: tuple[int, int], data):
    global direction
    new_start = (0, 0)
    data.reverse()
    for line_ind, line in enumerate(data):
        line = list(line)
        if len(line) - 1 - line_ind <= start[0]:
            if line[start[1]] != "#":
                line[start[1]] = "X"
                data[line_ind] = "".join(line)
                data.reverse()
                os.system("cls" if os.name == "nt" else "clear")
                print("\n".join(data))
                # time.sleep(0.1)
                data.reverse()
            else:
                direction = change_direction(direction)
                new_start = (len(line) - line_ind, start[1])
                break
    data.reverse()
    return new_start, data


def search_down(start: tuple[int, int], data):
    global direction
    new_start = (0, 0)
    for line_ind, line in enumerate(data):
        line = list(line)
        if line_ind > start[0] and line[start[1]] != "#":
            line[start[1]] = "X"
            data[line_ind] = "".join(line)
            os.system("cls" if os.name == "nt" else "clear")
            print("\n".join(data))
            # time.sleep(0.1)
        elif line_ind > start[0] and line[start[1]] == "#":
            direction = change_direction(direction)
            new_start = (line_ind - 1, start[1])
            break

    return new_start, data


def search_right(start: tuple[int, int], data: list[str]):
    global direction
    new_start = (0, 0)
    line = list(data[start[0]])
    for ind, v in enumerate(line):
        if ind >= start[1]:
            if v != "#":
                line[ind] = "X"
                data[start[0]] = "".join(line)
                os.system("cls" if os.name == "nt" else "clear")
                print("\n".join(data))
                # time.sleep(0.1)
            else:
                direction = change_direction(direction)
                new_start = (start[0], ind - 1)
                break

    data[start[0]] = "".join(line)
    return new_start, data


def search_left(start: tuple[int, int], data: list[str]):
    global direction
    new_start = (0, 0)
    line = list(data[start[0]])
    line.reverse()
    for ind, v in enumerate(line):
        if ind > len(line) - 1 - start[1]:
            if v != "#":
                line[ind] = "X"
                line.reverse()
                data[start[0]] = "".join(line)
                os.system("cls" if os.name == "nt" else "clear")
                print("\n".join(data))
                # time.sleep(0.1)
                line.reverse()
            else:
                direction = change_direction(direction)
                new_start = (start[0], len(line) - ind)
                break
    line.reverse()
    data[start[0]] = "".join(line)
    return new_start, data


start_time = perf_counter_ns()
while True:
    match direction:
        case "up":
            start, data = search_up(start, data)
        case "down":
            start, data = search_down(start, data)
        case "left":
            start, data = search_left(start, data)
        case "right":
            start, data = search_right(start, data)

    if start == (0, 0):
        break
# print(sum([x.count("X") for x in data]))
print(
    f"{perf_counter_ns() - start_time}ns > {(perf_counter_ns() - start_time)/1000000000}s"
)
