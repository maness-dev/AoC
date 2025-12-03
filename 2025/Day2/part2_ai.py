with open("2025/Day2/data.txt") as f:
    ranges = [tuple(map(int, r.split("-"))) for r in f.read().split(",")]

total = sum(
    num
    for start, end in ranges
    for num in range(start, end + 1)
    if any(
        (s := str(num)[:i]) * (len(str(num)) // i) == str(num)
        for i in range(1, len(str(num)) // 2 + 1)
    )
)

print(total)
