from time import perf_counter_ns


data = []
with open("2024/day5/data.txt", "r") as file:
    data = file.readlines()

rules = []
updates = []
for line in data:
    if "|" in line:
        rules.append([int(x) for x in line.strip().split("|")])
    if "," in line:
        updates.append([int(x) for x in line.strip().split(",")])


def sort(update, last_check=False):
    updated: list = update
    for i, num in enumerate(update):
        if i == len(update) - 1:
            break

        nex = update[i + 1]
        for rule in rules:
            if num in rule and nex in rule:
                if num == rule[0]:
                    continue
                else:
                    updated[i] = nex
                    updated[i + 1] = num
                    return True, updated, last_check

    return False, updated, True


sorted = []
part_1_total = 0
part_2_total = 0
start = perf_counter_ns()
for up in updates:
    updated = True
    last = False
    new = up
    good = True
    while updated:
        updated = False
        updated, new, last = sort(new, last)
        if updated and good:
            good = False

    if good:
        part_1_total += new[int(len(new) / 2)]

    if not good:
        part_2_total += new[int(len(new) / 2)]


print(part_1_total, part_2_total)
print(f"{perf_counter_ns() - start}ns > {(perf_counter_ns() - start)/1000000000}s")
