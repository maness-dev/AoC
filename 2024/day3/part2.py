import re


def get_sum(line):
    return sum(
        [
            eval(match.replace(",", "*"))
            for match in re.findall("mul\((\d{1,3},\d{1,3})\)", line)
        ]
    )


total = 0
with open(
    "/Users/c0m02iw/Documents/Dev/random/Python/advent/2024/day3/data.txt", "r"
) as f:
    lines = f.read().split("don't()")
    for ind, line in enumerate(lines):
        if ind == 0:
            total += get_sum(line)
            continue
        if "do()" not in line:
            continue

        total += get_sum(line.partition("do()")[2])

print(total)
