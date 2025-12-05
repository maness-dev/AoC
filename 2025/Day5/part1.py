fresh = []
ingredients = []
with open("2025/Day5/data.txt") as f:
    for line in f.readlines():
        if "-" in line:
            fresh.append(list(map(int, line.split("-"))))
        elif line.strip().isdigit():
            ingredients.append(int(line.strip()))

good_count = 0
for i in ingredients:
    for range in fresh:
        if range[0] <= i <= range[1]:
            good_count += 1
            break


print(good_count)
