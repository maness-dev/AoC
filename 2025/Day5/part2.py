ranges = []
with open("2025/Day5/data.txt") as f:
    ranges.extend(
        list(map(int, line.split("-"))) for line in f.readlines() if "-" in line
    )

ranges.sort()

merged = []
for start, end in ranges:
    if merged and start <= merged[-1][1] + 1:
        merged[-1][1] = max(merged[-1][1], end)
    else:
        merged.append([start, end])

total = sum(end - start + 1 for start, end in merged)
print(total)
