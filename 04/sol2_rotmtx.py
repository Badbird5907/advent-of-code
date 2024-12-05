from math import cos, sin, radians
word = "XMAS"
theta = radians(45) # 45 deg -> rad
# R(t) = [ cos t -sin t \ sin t cos t]
def rotate(x,y):
  return round(x * cos(theta) - y * sin(theta)), round(x * sin(theta) + y * cos(theta))

def print_pretty_matrix(matrix):
    for row in matrix:
        formatted_row = [str(elem) if isinstance(elem, tuple) else elem for elem in row]
        print(' '.join(formatted_row))
with open("input.txt", "r") as f:
  matrix = [list(line) for line in f.read().splitlines()]
  rows, cols = len(matrix), len(matrix[0])
  # TODO: rotate matrix
