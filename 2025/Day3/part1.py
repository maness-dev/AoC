import re


data = []
with open("2025/Day3/data.txt") as f:
    data = f.read().splitlines()
sum = 0
for num in data:
    largest_number = 0
    for i in range(9, -1, -1):
        i_str = str(i)
        if i_str not in str(num):
            continue

        if len(re.findall(i_str, str(num))) > 1:
            largest_number = int(i_str * 2)

        i_ind = re.search(i_str, str(num)).start()
        for j in range(9, -1, -1):
            j_str = str(j)
            if j_str in str(num[i_ind + 1 :]):
                if int(i_str + j_str) > largest_number:
                    largest_number = int(i_str + j_str)
                break

        if largest_number != 0:
            sum += largest_number
            break
print(sum)
