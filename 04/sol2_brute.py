# this is probably still the fastest way to do this lmao

with open("input.txt") as f:
    grid = [list(line) for line in f.read().splitlines()]
    count = 0
    for i in range(1, len(grid) - 1): # row
        for j in range(1, len(grid[0]) - 1): # col
            if grid[i][j] == "A":
                if (grid[i-1][j-1] == "M" and grid[i-1][j+1] == "S" and grid[i+1][j-1] == "M" and grid[i+1][j+1] == "S") or \
                (grid[i-1][j-1] == "S" and grid[i-1][j+1] == "M" and grid[i+1][j-1] == "S" and grid[i+1][j+1] == "M") or \
                (grid[i-1][j-1] == "S" and grid[i-1][j+1] == "S" and grid[i+1][j-1] == "M" and grid[i+1][j+1] == "M") or \
                (grid[i-1][j-1] == "M" and grid[i-1][j+1] == "M" and grid[i+1][j-1] == "S" and grid[i+1][j+1] == "S"):
                    count += 1
    print(count)
