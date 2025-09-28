import os
import time

class Cell:

    def __init__(self, value=0):
        self.value = value
        self.candidates = set()

#region
grid = [
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()],
    [Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell(), Cell()]
]
#endregion

#initial functions, run only 1 time
#region
def get_data():
    global grid
    global empty_squares

    with open("sample.txt", "r") as puzzle_file:
        for i in range(9):
            # row = input(f"Enter data for Row{i+1}: ")
            row = puzzle_file.readline()
            for j in range(9):
                grid[i][j].value = int(row[j])
                if grid[i][j].value == 0:
                    grid[i][j].candidates = {1, 2, 3, 4, 5, 6, 7, 8, 9}
                else:
                    empty_squares += 1


def trim_candidates():
    global grid

    cols = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)]
    blocks = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)]
    rows = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if grid[i][j].value != 0:
                if grid[i][j].value in rows[i]:
                    rows[i].remove(grid[i][j].value)
                if grid[i][j].value in cols[j]:
                    cols[j].remove(grid[i][j].value)
                if grid[i][j].value in blocks[(((i//3))*3)+(j//3)]:
                    blocks[(((i//3))*3)+(j//3)].remove(grid[i][j].value)
    
    for i in range(9):
        for j in range(9):
            if grid[i][j].value == 0:
                    grid[i][j].candidates = rows[i].intersection(cols[j]).intersection(blocks[(((i//3))*3)+(j//3)])

#endregion

#print functions
#region
def print_board():
    for _ in range(6):
        print()
    for row in range(9):
        printable_row = []
        for i in range(9):
            if grid[row][i].value == 0:
                printable_row.append('_')
            else:
                printable_row.append(grid[row][i].value)
            if i in {2, 5}:
                printable_row.append("|")
        print(*printable_row, sep=" ")
        if row in {2, 5}:
            print("-"*23)

#this is for testing
def print_candidates():
    for _ in range(6):
        print()
    for row in range(9):
        printable_cell_row = [[" "]*35, [" "]*35, [" "]*35]
        for i in range(3):
            printable_cell_row[i][3] = "|"
            printable_cell_row[i][7] = "|"
            printable_cell_row[i][11] = "█"
            printable_cell_row[i][15] = "|"
            printable_cell_row[i][19] = "|"
            printable_cell_row[i][23] = "█"
            printable_cell_row[i][27] = "|"
            printable_cell_row[i][31] = "|"
        for i in range(9):#each cell
            for candidate in range(1, 10):
                if candidate in grid[row][i].candidates:
                    printable_cell_row[(candidate-1)//3][(candidate-1)%3+(i*4)] = candidate
        
        for printable_row in printable_cell_row:
            print(*printable_row, sep=" ")
        if row in {2, 5}:
            print("█"*70)
        elif row != 8:
            print("-"*22+"█"+"-"*23+"█"+"-"*22)
    print()
#endregion

#Logic functions
#region
def fill_square(i, j, val):
    global empty_squares

    grid[i][j].value = val
    grid[i][j].candidates = set()
    empty_squares -= 1

def one_candidate():
    changed = False

    for i in range(9):
        for j in range(9):
            if len(grid[i][j].candidates) == 1:
                fill_square(i, j, grid[i][j].candidates.pop())
                trim_candidates()
                changed = True
    return changed

def one_place_in_group():
    cols = [[(-1, -1)]*9 for _ in range(9)]
    blocks = [[(-1, -1)]*9 for _ in range(9)]
    rows = [[(-1, -1)]*9 for _ in range(9)]

    changed = False
    for i in range(9):
        for j in range(9):
            for candidate in grid[i][j].candidates:
                if rows[i][candidate-1] == (-1, -1):
                    rows[i][candidate-1] = (i, j)
                else:
                    rows[i][candidate-1] = (-2, -2)

                if cols[j][candidate-1] == (-1, -1):
                    cols[j][candidate-1] = (i, j)
                else:
                    cols[j][candidate-1] = (-2, -2)

                if blocks[(((i//3))*3)+(j//3)][candidate-1] == (-1, -1):
                    blocks[(((i//3))*3)+(j//3)][candidate-1] = (i, j)
                else:
                    blocks[(((i//3))*3)+(j//3)][candidate-1] = (-2, -2)

    for row in range(9):
        for num in range(9):
            if rows[row][num][0] > -1:
                fill_square(rows[row][num][0], rows[row][num][1], num+1)
                changed = True

    trim_candidates()

    return changed


#endregion    

empty_squares = 0

get_data()
trim_candidates()
print_board()
# print_candidates()

try:
    while empty_squares > 0:
        while one_place_in_group():#one place in a group
            while one_candidate():
                # time.sleep(1)
                os.system('clear')
                print_board()
            # time.sleep(1)
            os.system('clear')
            print_board()
        #overlap block and row/col
        # print("HI")
        break

except KeyboardInterrupt:
    # os.system('clear')
    pass
finally:
    # print_board()
    pass