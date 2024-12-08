import sys


data = []
with open("2024/day7/test_data.txt", "r") as file:
    for line in file:
        data.append(line.strip())


def evaluate(target: int, values: list[int]):
    end_bit = "".join(["1" for i in range(0, len(values) - 1)])
    count = 0
    ops = 0
    while ops != end_bit:
        ops = bin(count)[2:].zfill(len(end_bit))
        line = ""
        split_ops = list(ops)
        score = ""
        line = ""
        for i, v in enumerate(values):
            if i == 0:
                score = v
                line = f"{v}"
                continue
            line = f"{line}{'+' if split_ops[i-1] == '0' else '*'}{v}"
            score = int(eval(f"{score}{'+' if split_ops[i-1] == '0' else '*'}{v}"))

        if score == target:
            return True
        count += 1
    return False


def merge_tests(target: int, values: list[int]):
    end_bit = "".join(["1" for i in range(0, len(values) - 1)])
    count = 0
    ops = 0
    while ops != end_bit:
        ops = bin(count)[2:].zfill(len(end_bit))
        split_ops = list(ops)
        line = ""
        for i, v in enumerate(values):
            if i == 0:
                line = f"{v}"
                continue
            if split_ops[i - 1] == "1":
                line = f"{line}{v}"
            else:
                line = f"{line},{v}"
        new = [int(x) for x in line.split(",")]
        if len(new) == 1:
            if target != int(new[0]):
                return False
            else:
                return True
        check = evaluate(target, new)
        if check:
            return True
        count += 1

    return False


total = 0

for line in data:
    target = int(line.split(":")[0])
    values = [int(x) for x in line.split(":")[1].strip().split(" ")]
    check = merge_tests(target, values)
    if check:
        total += target
print(total)
