data: list[str] = []
with open("2024/day8/data.txt", "r") as file:
    for line in file:
        data.append(line.strip())

coords: dict[str, list[tuple[int, int]]] = {}
for line_ind, line in enumerate(data):
    for col_ind, char in enumerate(line):
        if char.isalnum():
            if char in coords:
                coords[char].append((line_ind, col_ind))
            else:
                coords[char] = [(line_ind, col_ind)]

antinodes = set()
for symb in coords:
    points = coords[symb]
    for ind, point in enumerate(points):
        for inner_ind, inner_point in enumerate(points):
            antinodes.add(point)
            antinodes.add(inner_point)
            if ind == inner_ind:
                continue
            slope = (inner_point[0] - point[0], inner_point[1] - point[1])
            start = inner_point
            while True:
                antinode_point = (start[0] + slope[0], start[1] + slope[1])
                start = antinode_point
                if antinode_point[0] in range(0, len(data[0])) and antinode_point[
                    1
                ] in range(0, len(data)):
                    antinodes.add(antinode_point)
                else:
                    break

print(len(antinodes))
