def remove_lowest_left_digit(number):
    str_num = str(number)
    min_digit = min(str_num)
    min_index = str_num.index(min_digit)
    return int(str_num[:min_index] + str_num[min_index + 1 :])


def find_best_12_digits(number):
    """
    Find the best 12-digit number by trying all possible starting positions
    and selecting the one that yields the maximum result after trimming.
    """
    str_num = str(number)
    if len(str_num) < 12:
        return -1

    best_result = 0

    # Try every possible starting position that leaves at least 12 digits
    for start_pos in range(len(str_num) - 11):
        substring = str_num[start_pos:]
        num = int(substring)

        # Trim down to 12 digits
        while len(str(num)) > 12:
            num = remove_lowest_left_digit(num)

        if len(str(num)) == 12:
            best_result = max(best_result, num)

    return best_result if best_result > 0 else -1


# Load and process data
data = []
with open("2025/Day3/data.txt") as f:
    data = [int(x) for x in f.read().splitlines()]

sum_total = 0
for i, num in enumerate(data):
    result = find_best_12_digits(num)
    if result == -1:
        print(f"ERROR on line {i + 1}: {num}")
    else:
        sum_total += result
        if i < 5:  # Print first 5 for verification
            print(f"Line {i + 1}: {result}")

print(f"\nSum: {sum_total}")
