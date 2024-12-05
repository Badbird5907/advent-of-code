dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
word = "XMAS"

def checkDir(grid, i, j, dir, idx):
    i1, j1 = i + dir[0], j + dir[1]
    if not (0 <= i1 < len(grid) and 0 <= j1 < len(grid[0])): # bounds
        return False
    if grid[i1][j1] != word[idx + 1]:
        return False
    if idx + 1 == len(word) - 1:
        return True
    return checkDir(grid, i1, j1, dir, idx + 1)

def countMatches(grid, i, j):
    return sum(checkDir(grid, i, j, dir, 0) for dir in dirs)

with open('input.txt') as f:
    grid = [list(line) for line in f.read().splitlines()]
    count = sum(countMatches(grid, i, j) 
               for i in range(len(grid)) # row
               for j in range(len(grid[0])) # col
               if grid[i][j] == word[0]) # only check first
    print(count)