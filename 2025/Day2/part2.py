import re


data = ""
with open("2025/Day2/data.txt") as f:
    data = f.read()

ranges = [tuple(map(int, r.split("-"))) for r in data.split(",")]

total = 0
for r in ranges:
    for num in range(r[0], r[1] + 1):
        str_num = str(num)
        for i in range(1, round(len(str_num) / 2) + 1):
            matches = re.findall(f"{str_num[:i]}", str_num)
            if len(matches) * len(str_num[:i]) == len(str_num):
                total += num
                break

print(total)
