from copy import deepcopy
from pprint import pprint
from time import perf_counter_ns


data = []
with open("2024/day6/test_data.txt", "r") as file:
    for line in file:
        data.append(line.strip())

direction = "up"
points = {}
beginning_point = (0, 0)
total = 0
previous_points = {"up": set(), "down": set(), "left": set(), "right": set()}
obstacle_points = set()
start = 0, 0
direc = ""


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
    global direction, total, previous_points, obstacle_points, direc
    all_points = []
    new_start = (0, 0)
    data.reverse()
    for line_ind, line in enumerate(data):
        line = list(line)
        if len(line) - 1 - line_ind <= start[0]:
            if line[start[1]] == "#":
                if direc:
                    direc = change_direction(direc)
                else:
                    direction = change_direction(direction)
                new_start = (len(line) - line_ind, start[1])
                break
            else:
                all_points.append((len(line) - line_ind - 1, start[1]))
                previous_points["up"].add(start[1])
                if len(line) - line_ind - 1 in previous_points["right"]:
                    obstacle_points.add((len(line) - line_ind, start[1]))
    data.reverse()
    return new_start, data, all_points


def search_down(start: tuple[int, int], data):
    global direction, total, previous_points, obstacle_points, direc
    all_points = []
    new_start = (0, 0)
    for line_ind, line in enumerate(data):
        line = list(line)
        if line_ind > start[0]:
            all_points.append((line_ind - 1, start[1]))
            previous_points["down"].add(start[1])
            if line_ind - 1 in previous_points["left"]:
                obstacle_points.add((line_ind, start[1]))
            if line[start[1]] == "#":
                if direc:
                    direc = change_direction(direc)
                else:
                    direction = change_direction(direction)
                new_start = (line_ind - 1, start[1])
                break
    return new_start, data, all_points


def search_right(start: tuple[int, int], data: list[str]):
    global direction, total, previous_points, obstacle_points, direc
    new_start = (0, 0)
    all_points = []
    line = list(data[start[0]])
    for ind, v in enumerate(line):
        if ind >= start[1]:
            if v == "#":
                if direc:
                    direc = change_direction(direc)
                else:
                    direction = change_direction(direction)
                new_start = (start[0], ind - 1)
                break
            else:
                all_points.append((start[0], ind))
                previous_points["right"].add(start[0])
                if ind in previous_points["down"]:
                    obstacle_points.add((start[0], ind + 1))

    data[start[0]] = "".join(line)
    return new_start, data, all_points


def search_left(start: tuple[int, int], data: list[str]):
    global direction, total, previous_points, obstacle_points, direc
    new_start = (0, 0)
    all_points = []
    line = list(data[start[0]])
    line.reverse()
    for ind, v in enumerate(line):
        if ind > len(line) - 1 - start[1]:
            all_points.append((start[0], len(line) - ind - 1))
            previous_points["left"].add(start[0])
            if len(line) - ind - 1 in previous_points["up"]:
                line.reverse()
                obstacle_points.add((start[0], len(line) - 2 - ind))
                line.reverse()
            if v == "#":
                if direc:
                    direc = change_direction(direc)
                else:
                    direction = change_direction(direction)
                new_start = (start[0], len(line) - ind)
                break
    line.reverse()
    data[start[0]] = "".join(line)
    return new_start, data, all_points


def sub_loop(start, temp):
    global direc
    this_path_points = []
    while True:
        match direc:
            case "up":
                start, temp, _ = search_up(start, temp)
            case "down":
                start, temp, _ = search_down(start, temp)
            case "left":
                start, temp, _ = search_left(start, temp)
            case "right":
                start, temp, _ = search_right(start, temp)
        if start == (0, 0):
            direc = ""
            return False
        else:
            if start in this_path_points:
                direc = ""
                return True
            else:
                this_path_points.append(points)


loop_obs = []
tested = {}
for line_ind, line in enumerate(data):
    if "^" in line:
        start = (line_ind, line.index("^"))
        beginning_point = start
while True:
    match direction:
        case "up":
            start, data, all_points = search_up(start, data)
            direc = "right"
            for point in all_points:
                if point == beginning_point:
                    continue
                loopy = sub_loop(point, deepcopy(data))
                if loopy:
                    point[0] = point[0] - 1
                    loop_obs.append(point)
        case "down":
            start, data, all_points = search_down(start, data)
            direc = "left"
            for point in all_points:
                if point == beginning_point:
                    continue
                loopy = sub_loop(point, deepcopy(data))
                if loopy:
                    point[0] = point[0] + 1
                    loop_obs.append(point)
        case "left":
            start, data, all_points = search_left(start, data)
            direc = "up"
            for point in all_points:
                if point == beginning_point:
                    continue
                loopy = sub_loop(point, deepcopy(data))
                if loopy:
                    point[1] = point[1] - 1
                    loop_obs.append(point)
        case "right":
            start, data, all_points = search_right(start, data)
            direc = "down"
            for point in all_points:
                if point == beginning_point:
                    continue
                loopy = sub_loop(point, deepcopy(data))
                if loopy:
                    point[1] = point[1] + 1
                    loop_obs.append(point)
    if start == (0, 0):
        break
print()
print(len(obstacle_points))
