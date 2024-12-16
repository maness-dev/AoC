from time import perf_counter_ns
import concurrent.futures

data: list[str] = []
with open("2024/day11/data.txt", "r") as file:
    for line in file:
        data.append(line.strip())


def process(nums: list[int], ind: int):
    new_nums: list[int] = []
    for num in nums:
        if len(str(num)) % 2 == 0:
            new_nums.append(int(str(str(num)[: int(len(str(num)) / 2)])))
            new_nums.append(int(str(str(num)[int(len(str(num)) / 2) :])))
            continue
        if num == 0:
            new_nums.append(1)
            continue
        new_nums.append(num * 2024)

    return new_nums, ind


start = perf_counter_ns()
new_nums = [int(x) for x in data[0].split(" ")]
iter = 0
while iter != 75:
    if iter % 10 == 0:
        print(iter)
    split_work = [new_nums[i : i + 25] for i in range(0, len(new_nums), 25)]
    new_nums = []
    list_positions = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(process, values, ind)
            for ind, values in enumerate(split_work)
        ]
        for future in concurrent.futures.as_completed(futures):
            list_positions[future.result()[1]] = future.result()[0]
    for i in range(0, len(list_positions)):
        new_nums.extend(list_positions[i])

    iter += 1

print(len(new_nums))
end = perf_counter_ns()
print(
    f"Time: {end-start}ns / {(end-start)/1000000000}s / {(end-start)/1000000000/60}Min / {(end-start)/1000000000/60/60}Hours"
)
