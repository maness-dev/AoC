def is_safe(row):
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    return set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}


data = [
    [int(y) for y in x.split(" ")]
    for x in open("Python/advent/2024/day2/02.txt").read().split("\n")
]

safe_count = sum([is_safe(row) for row in data])
print(safe_count)

safe_count = sum(
    [any([is_safe(row[:i] + row[i + 1 :]) for i in range(len(row))]) for row in data]
)
print(safe_count)
