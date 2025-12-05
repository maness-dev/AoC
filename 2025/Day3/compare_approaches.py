def remove_lowest_left_digit(number):
    str_num = str(number)
    min_digit = min(str_num)
    min_index = str_num.index(min_digit)
    return int(str_num[:min_index] + str_num[min_index + 1 :])


def find_highest_index(number):
    str_num = str(number)
    for i in range(9, -1, -1):
        if str(i) in str_num:
            if len(str_num[str_num.index(str(i)) :]) >= 12:
                return int(str(str_num[str_num.index(str(i)) :]))
    return -1


def approach1_original(num):
    """Original approach with find_highest_index"""
    num = find_highest_index(num)
    if num == -1:
        return None
    while len(str(num)) > 12:
        num = remove_lowest_left_digit(num)
    return num if len(str(num)) == 12 else None


def approach2_from_start(num):
    """Alternative: always start from position 0"""
    if len(str(num)) < 12:
        return None
    while len(str(num)) > 12:
        num = remove_lowest_left_digit(num)
    return num if len(str(num)) == 12 else None


# Load data
data = []
with open("2025/Day3/data.txt") as f:
    data = [int(x) for x in f.read().splitlines()]

sum1 = 0
sum2 = 0
differences = []

for i, num in enumerate(data):
    result1 = approach1_original(num)
    result2 = approach2_from_start(num)

    if result1 is None or result2 is None:
        print(f"ERROR on line {i + 1}: {num}")
        continue

    sum1 += result1
    sum2 += result2

    if result1 != result2:
        differences.append(
            {
                "line": i + 1,
                "input": num,
                "approach1": result1,
                "approach2": result2,
                "diff": result2 - result1,
            }
        )

print(f"Approach 1 (with find_highest_index): {sum1}")
print(f"Approach 2 (from start):               {sum2}")
print(f"Difference:                             {sum2 - sum1}")
print(f"\nNumber of differences: {len(differences)}")

if differences:
    print("\nFirst 10 differences:")
    for d in differences[:10]:
        print(f"Line {d['line']}: {d['input']}")
        print(f"  Approach 1: {d['approach1']}")
        print(f"  Approach 2: {d['approach2']} (diff: +{d['diff']})")
