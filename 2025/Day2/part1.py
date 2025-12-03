data = ""
with open("2025/Day2/data.txt") as f:
    data = f.read()

ranges = [tuple(map(int, r.split("-"))) for r in data.split(",")]

total = 0
for r in ranges:
    for num in range(r[0], r[1] + 1):
        str_num = str(num)
        first_half = str_num[: round(len(str_num) / 2)]
        second_half = str_num[round(len(str_num) / 2) :]

        if first_half == second_half:
            total += num

print(total)
