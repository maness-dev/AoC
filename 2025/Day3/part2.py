data = []
with open("2025/Day3/data.txt") as f:
    data = [int(x) for x in f.read().splitlines()]


def get_best_12_digits(number):
    """
    Greedy algorithm to select the best 12 digits from the number
    while maintaining their original order.

    Remove (len - 12) digits by always removing a digit when there's
    a larger digit after it, otherwise remove from the end.
    """
    str_num = str(number)
    if len(str_num) < 12:
        return -1

    if len(str_num) == 12:
        return int(str_num)

    digits = list(str_num)
    to_remove = len(digits) - 12

    # Remove digits greedily
    for _ in range(to_remove):
        # Find first position where current digit < next digit
        for i in range(len(digits) - 1):
            if digits[i] < digits[i + 1]:
                digits.pop(i)
                break
        else:
            # All remaining digits are in descending order, remove from end
            digits.pop()

    return int("".join(digits))


sum_total = 0
for num in data:
    result = get_best_12_digits(num)
    if result == -1:
        print("error:", num)
    else:
        print(result)
        sum_total += result

print("sum:", sum_total)
