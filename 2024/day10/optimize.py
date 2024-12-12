from time import perf_counter_ns
import concurrent.futures


data: list[str] = []
with open("2024/day10/data.txt", "r") as file:
    for line in file:
        data.append(line.strip())


def search(start_point, start_number):
    results: list[tuple[int, int]] = []
    point_9 = []
    if start_point[0] > 0:
        num = int(data[start_point[0] - 1][start_point[1]])
        if num == start_number + 1:
            if num == 9:
                point_9.append((start_point[0] - 1, start_point[1]))
            results.append((start_point[0] - 1, start_point[1]))
    if start_point[0] < len(data) - 1:
        num = int(data[start_point[0] + 1][start_point[1]])
        if num == start_number + 1:
            if num == 9:
                point_9.append((start_point[0] + 1, start_point[1]))
            results.append((start_point[0] + 1, start_point[1]))
    if start_point[1] > 0:
        num = int(data[start_point[0]][start_point[1] - 1])
        if num == start_number + 1:
            if num == 9:
                point_9.append((start_point[0], start_point[1] - 1))
            results.append((start_point[0], start_point[1] - 1))
    if start_point[1] < len(data[0]) - 1:
        num = int(data[start_point[0]][start_point[1] + 1])
        if num == start_number + 1:
            if num == 9:
                point_9.append((start_point[0], start_point[1] + 1))
            results.append((start_point[0], start_point[1] + 1))

    if start_number != 8:
        with concurrent.futures.ProcessPoolExecutor(
            max_workers=1, max_tasks_per_child=100
        ) as executor:
            futures = [
                executor.submit(search, new_start, start_number + 1)
                for new_start in results
            ]
            for future in concurrent.futures.as_completed(futures):
                point_9.extend(future.result())

    return point_9


zeroes: list[tuple[int, int]] = []
for line_ind, line in enumerate(data):
    for col_ind, char in enumerate(line):
        if char == "0":
            zeroes.append((line_ind, col_ind))

part1 = 0
part2 = 0
start = perf_counter_ns()
with concurrent.futures.ProcessPoolExecutor(
    max_workers=1, max_tasks_per_child=100
) as executor:
    futures = [executor.submit(search, zero_point, 0) for zero_point in zeroes]
    for future in concurrent.futures.as_completed(futures):
        part1 += len(set(future.result()))
        part2 += len(future.result())
print(part1)
print(part2)
end = perf_counter_ns()
print(f"Time: {end-start}ns / {(end-start)/1000000000}s")
