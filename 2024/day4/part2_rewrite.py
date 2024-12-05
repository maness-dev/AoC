import time

now = time.time()
total = 0
data = []
with open("2024/day4/data.txt", "r") as file:
    data = file.readlines()


def rewrite(data):
    global total
    for line_ind, line in enumerate(data):
        for m_ind, char in enumerate(line):
            if char != "A":
                continue

            if (
                line_ind > 0
                and line_ind < len(data) - 1
                and m_ind > 0
                and m_ind < len(line) - 1
            ):
                if all(
                    [
                        set(
                            [
                                data[line_ind - 1][m_ind - 1],
                                data[line_ind + 1][m_ind + 1],
                            ]
                        )
                        == set(["S", "M"]),
                        set(
                            [
                                data[line_ind + 1][m_ind - 1],
                                data[line_ind - 1][m_ind + 1],
                            ]
                        )
                        == set(["S", "M"]),
                    ]
                ):
                    total += 1


for ind, line in enumerate(data):
    data[ind] = line.strip()

rewrite(data)
print(total)
print(f"runtime: {time.time()-now}")
