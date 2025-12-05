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


def process_number(num):
    """Process a single number to get the highest 12-digit result"""
    original = num
    num = find_highest_index(num)
    if num == -1:
        return None, "Could not find valid starting point"

    steps = []
    steps.append(f"After find_highest_index: {num} (len={len(str(num))})")

    iteration = 0
    while len(str(num)) > 12:
        iteration += 1
        old_num = num
        num = remove_lowest_left_digit(num)
        min_digit = min(str(old_num))
        steps.append(
            f"Iteration {iteration}: Removed '{min_digit}' → {num} (len={len(str(num))})"
        )

    if len(str(num)) < 12:
        return None, f"Error: Result too short ({len(str(num))} digits)"

    return num, steps


# Test cases
test_cases = [
    987654321111111,
    811111111111119,
    234234234234278,
    818181911112111,
    821111111111119,  # My proposed counter-example
]

print("=" * 80)
print("TESTING LOGIC")
print("=" * 80)

for test in test_cases:
    print(f"\nInput: {test} ({len(str(test))} digits)")
    print("-" * 80)
    result, info = process_number(test)

    if isinstance(info, list):
        for step in info:
            print(f"  {step}")
        print(f"\n  FINAL RESULT: {result}")
    else:
        print(f"  ERROR: {info}")

# Now test with actual data
print("\n" + "=" * 80)
print("TESTING WITH ACTUAL DATA")
print("=" * 80)

data = []
with open("2025/Day3/data.txt") as f:
    data = [int(x) for x in f.read().splitlines()]

sum_total = 0
errors = []

for i, num in enumerate(data):
    result, info = process_number(num)
    if result is None:
        errors.append((i, num, info))
    else:
        sum_total += result

print(f"\nProcessed {len(data)} numbers")
print(f"Errors: {len(errors)}")
if errors:
    for idx, num, err in errors[:5]:  # Show first 5 errors
        print(f"  Line {idx + 1}: {num} - {err}")
print(f"\nSum: {sum_total}")
