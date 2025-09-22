# Sudoku Solver using Backtracking

# Function to print the Sudoku grid
def print_grid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()

# Function to find an empty cell
def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:  # 0 means empty
                return i, j
    return None

# Function to check if placing a number is valid
def is_valid(grid, num, pos):
    row, col = pos

    # Check row
    for j in range(9):
        if grid[row][j] == num and j != col:
            return False

    # Check column
    for i in range(9):
        if grid[i][col] == num and i != row:
            return False

    # Check 3x3 subgrid
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False

    return True

# Backtracking solver
def solve(grid):
    find = find_empty(grid)
    if not find:
        return True  # Puzzle solved
    row, col = find

    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num

            if solve(grid):
                return True

            grid[row][col] = 0  # Reset and backtrack

    return False

# Example unsolved Sudoku puzzle (0 represents empty cells)
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Unsolved Sudoku:")
print_grid(sudoku_grid)

if solve(sudoku_grid):
    print("\nSolved Sudoku:")
    print_grid(sudoku_grid)
else:
    print("No solution exists.")
