from enum import Enum
class Direction(Enum):
    UP = ("^", (-1, 0))
    DOWN = ("v", (1, 0)) 
    LEFT = ("<", (0, -1))
    RIGHT = (">", (0, 1))
    
    def next(self):
        if self == Direction.UP:
            return Direction.RIGHT
        if self == Direction.RIGHT:
            return Direction.DOWN
        if self == Direction.DOWN:
            return Direction.LEFT
        if self == Direction.LEFT:
            return Direction.UP
    
    def next_pos(self, pos):
        return (pos[0] + self.value[1][0], pos[1] + self.value[1][1])

def pretty_print(matrix, visited, pos, direction):
    for i in range(len(matrix)):
        row = matrix[i]
        for j in range(len(row)):
            if (i,j) == pos:
                print(direction.value[0], end="")
            elif (i,j) in visited:
                print("X", end="")
            elif row[j]:
                print("#", end="")
            else:
                print(".", end="")
        print()

def in_bounds(pos, matrix):
    return pos[0] >= 0 and pos[0] < len(matrix) and pos[1] >= 0 and pos[1] < len(matrix[0])

with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    matrix = []
    visited = set()
    pos = (0,0)
    direction = Direction.UP
    for i in range(len(lines)):
        line = lines[i]
        matrix.append([c == "#" for c in line])
        for j in range(len(line)):
            if line[j] == "^":
                pos = (i,j)
                break
    pretty_print(matrix, visited, pos, direction)

    while (in_bounds(pos, matrix)):
        visited.add(pos)
        next = direction.next_pos(pos)
        if (not in_bounds(next, matrix)): # if out of bounds, exit
            break
        if (matrix[next[0]][next[1]]): # wall
            direction = direction.next()
            next = direction.next_pos(pos)
        pos = next
    
    print(len(visited))
