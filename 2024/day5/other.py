rules, updates = open("2024/day5/data.txt").read().split("\n\n")


def order(nums):
    return sorted(nums, key=lambda x: -sum(f"{x}|{y}" in rules for y in nums))


print(
    sum(
        int(order(nums)[len(nums) // 2])
        for nums in [x.split(",") for x in updates.split("\n")]
        if order(nums) == nums
    )
)
print(
    sum(
        int(order(nums)[len(nums) // 2])
        for nums in [x.split(",") for x in updates.split("\n")]
        if order(nums) != nums
    )
)
