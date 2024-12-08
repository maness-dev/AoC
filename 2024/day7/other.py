import sys


data = []
with open("2024/day7/data.txt", "r") as file:
    for line in file:
        data.append(line.strip())


def evaluate(target: int, values: list[int]):
    end_bit = "".join(["1" for i in range(0, len(values) - 1)])
    outer_count = 0
    outer_ops = 0
    while outer_ops != end_bit:
        outer_ops = bin(outer_count)[2:].zfill(len(end_bit))
        outer_split_ops = list(outer_ops)

        count = 0
        ops = 0
        while ops != end_bit:
            ops = bin(count)[2:].zfill(len(end_bit))
            split_ops = list(ops)
            actual_ops = [int(x) + int(y) for x, y in zip(outer_split_ops, split_ops)]
            # print(actual_ops)
            score = 0
            range_count = 0
            ops_count = 0
            while range_count < len(values):
                if range_count == 0:
                    score = values[range_count]
                if range_count == len(values) - 1:
                    range_count += 1
                    continue
                char = (
                    "+"
                    if actual_ops[ops_count] == 0
                    else "*"
                    if actual_ops[ops_count] == 1
                    else "||"
                )
                # print(score, char, values[range_count + 1])
                if char == "||":
                    score = int(f"{score}{values[range_count+1]}")
                elif char == "+":
                    score += values[range_count + 1]
                else:
                    score = score * values[range_count + 1]
                range_count += 1
                ops_count += 1

            if score == target:
                return True
            count += 1

        outer_count += 1


total = 0
for line in data:
    target = int(line.split(":")[0])
    values = [int(x) for x in line.split(":")[1].strip().split(" ")]
    check = evaluate(target, values)
    if check:
        total += target
print(total)
