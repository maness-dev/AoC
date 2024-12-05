data = []
with open("2024/day4/data.txt", 'r') as file:
    data = file.readlines()

def search(line_index):
    def search_diag(x_index, direction):
        if direction == 'upleft':
            if all(
                [
                    data[line_index-1][x_index-1]=='M',
                    data[line_index-2][x_index-2]=='A',
                    data[line_index-3][x_index-3]=='S',
                ]
            ) :
                return True
            return False
        if direction == 'upright':
            if all(
                [
                    data[line_index-1][x_index+1]=='M',
                    data[line_index-2][x_index+2]=='A',
                    data[line_index-3][x_index+3]=='S',
                ]
            ):
                return True
            return False
        if direction == 'downleft':
            if all(
                [
                    data[line_index+1][x_index-1]=='M',
                    data[line_index+2][x_index-2]=='A',
                    data[line_index+3][x_index-3]=='S',
                ]
            ) :
                return True
            return False
        if direction == 'downright':
            if all(
                [
                    data[line_index+1][x_index+1]=='M',
                    data[line_index+2][x_index+2]=='A',
                    data[line_index+3][x_index+3]=='S',
                ]
            ):
                return True
            return False


    def search_up(x_index):
        if all(
            [
                data[line_index-1][x_index]=='M',
                data[line_index-2][x_index]=='A',
                data[line_index-3][x_index]=='S',

            ]
        ):
            return True
        return False
    
    def search_down(x_index):
        if all(
            [
                data[line_index+1][x_index]=='M',
                data[line_index+2][x_index]=='A',
                data[line_index+3][x_index]=='S',

            ]
        ):
            return True
        return False
    
    def search_sides(x_ind, direc):
        if direc == 'left':
            if all(
            [
                    data[line_index][x_ind-1]=='M',
                    data[line_index][x_ind-2]=='A',
                    data[line_index][x_ind-3]=='S',

                ]
            ):
                return True
            return False
        if direc == 'right':
            if all(
            [
                    data[line_index][x_ind+1]=='M',
                    data[line_index][x_ind+2]=='A',
                    data[line_index][x_ind+3]=='S',

                ]
            ):
                return True
            return False

    searches = []

    for x_ind,char in enumerate(data[line_index]):
        if char != 'X':
            continue

        if line_index >2:
            searches.append(search_up(x_ind))
            if x_ind > 2:
                searches.append(search_diag(x_ind,"upleft"))
            if x_ind < len(data[line_index].strip())-3:
                searches.append(search_diag(x_ind,"upright"))


        if line_index < len(data)-3:
            searches.append(search_down(x_ind))
            if x_ind > 2:
                searches.append(search_diag(x_ind,"downleft"))
            if x_ind < len(data[line_index].strip())-3:
                searches.append(search_diag(x_ind,"downright"))

        if x_ind > 2:
            searches.append(search_sides(x_ind,"left"))
        if x_ind < len(data[line_index].strip())-3:
            searches.append(search_sides(x_ind,"right"))

    return searches

total=0
for line_ind, v in enumerate(data):
    total+=sum(search(line_ind))
    
print(total)
