#region

grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0]]

#each type of group that needs to have 9 in each. Box goes left to right top to bottom, collumns left to right, rows top to bottom.
boxes = [{1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9}]


columns = [{1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9}]


rows = [{1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9},
       {1, 2, 3, 4, 5, 6, 7, 8, 9},]

#endregion

def get_data():
    global grid
    global empty_squares

    print("Enter the data for each row from top to bottom")
    print("Make them space seperated with a '0' for an empty space")

    for i in range(9):
        temporary = input(f"Row {i}: ").split()
        for j in range(9):
            grid[j] = int(temporary[j])
            if grid[j] == 0:
                empty_squares += 1

def print_grid():
   for row in grid:
       print(*row, sep = " ")


empty_squares = 0

while empty_squares > 0:
    pass
    #will add actual logic here
