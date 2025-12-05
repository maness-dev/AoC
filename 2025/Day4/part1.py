data = []
with open("2025/Day4/data.txt") as f:
    data = [line.strip() for line in f.readlines()]

accessible = 0

for i, line in enumerate(data):
    above_line = data[i - 1] if i > 0 else None
    current_line = line
    next_line = data[i + 1] if i < len(data) - 1 else None
    for c_i, c in enumerate(current_line):
        count = 0
        if c == "@":
            if above_line:
                count += sum(
                    [
                        above_line[c_i - 1] == "@" if c_i > 0 else False,
                        above_line[c_i] == "@",
                        above_line[c_i + 1] == "@"
                        if c_i < len(above_line) - 1
                        else False,
                    ]
                )
            if next_line:
                count += sum(
                    [
                        next_line[c_i - 1] == "@" if c_i > 0 else False,
                        next_line[c_i] == "@",
                        next_line[c_i + 1] == "@"
                        if c_i < len(next_line) - 1
                        else False,
                    ]
                )
            count += sum(
                [
                    current_line[c_i - 1] == "@" if c_i > 0 else False,
                    current_line[c_i + 1] == "@"
                    if c_i < len(current_line) - 1
                    else False,
                ]
            )
            if count < 4:
                accessible += 1

print(accessible)
