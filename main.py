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

def get_data():
    global grid
    for i in range(9):
        row = input(f"Enter data for Row{i+1}").split()
        for j in range(9):
            grid[i][j].value = int(row[j])
            if grid[i][j].value != 0:
                grid[i][j].candidates = {1, 2, 3, 4, 5, 6, 7, 8, 9}

def print_grid():
    for row in range(9):
        printable_row = []
        for i in range(9):
            printable_row.append(grid[row][i].value)
            if i in {2, 5}:
                printable_row.append("|")
        print(*printable_row, sep=" ")
        if row in {2, 5}:
            print("-"*23)

def trim_candidates():
    global grid

    cols = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)]
    blocks = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)]
    for i in range(9):
        row = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        for j in range(9):
            if grid[i][j].value != 0:
                row.remove(grid[i][j].value)
                cols[j].remove(grid[i][j].value)
                blocks[(((i+1)//3)+1)*(((j+1)//3)+1)-1].remove(grid[i][j].value)

print_grid()
