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

def in_bounds(pos, matrix):
    return pos[0] >= 0 and pos[0] < len(matrix) and pos[1] >= 0 and pos[1] < len(matrix[0])

def sim(matrix, oPos, obs):
    visited = set()
    direction = Direction.UP
    pos = (oPos[0], oPos[1])
    
    while True:
        y, x = pos
        if not in_bounds(pos, matrix):
            return 0
            
        if matrix[y][x] or (y, x) == obs:
            pos = (y - direction.value[1][0], x - direction.value[1][1])
            direction = direction.next() 
        elif (y, x, direction) in visited:
            return 1
        else:
            visited.add((y, x, direction))
            pos = direction.next_pos((y, x))

with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    matrix = []
    for i in range(len(lines)):
        line = lines[i]
        matrix.append([c == "#" for c in line])
        for j in range(len(line)):
            if line[j] == "^":
                pos = (i,j)
                break
    
    possibilities = sum(
        1 for y in range(len(matrix)) 
        for x in range(len(matrix[0])) 
        if not matrix[y][x]
        and sim(matrix, pos, (y,x))
    )
    print(possibilities)
