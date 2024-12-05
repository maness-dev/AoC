import re

with open(
    "/Users/c0m02iw/Documents/Dev/random/Python/advent/2024/day3/data.txt", "r"
) as f:
    print(
        sum(
            [
                eval(match.replace(",", "*"))
                for match in re.findall("mul\((\d{1,3},\d{1,3})\)", f.read())
            ]
        )
    )
