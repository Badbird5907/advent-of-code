from aoc_lube import fetch
from math import sqrt
from collections import defaultdict
try:
    with open("input.txt", "r") as f:
        lines = map(str.strip, f.readlines())
except FileNotFoundError:
    lines = fetch(2024, 8, None).splitlines()

map = list(list(x) for x in lines)

def check_bounds(coord):
    x, y = coord
    return 0 <= y < len(map) and 0 <= x < len(map[0])

def dist(a,b):
    return (b[0] - a[0], b[1] - a[1])

antennas = defaultdict(set)

for y in range(len(map)):
    line = map[y]
    for x in range(len(map[0])):
        cell = line[x]
        if (not cell == "."):
            antennas[cell].add((x, y))

antinodes = set()
for key in antennas.keys():
    print(key, antennas[key])
    all_an = antennas[key]
    # I LOVE BRUTE FORCE
    # I LOVE MY O(n^2)
    for an1 in all_an:
        for an2 in all_an:
            if (an1 == an2):
                continue
            distance = dist(an1, an2)
            print(an1, "-", an2, ":", distance)
            for anti in [(an1[0] + distance[0], an1[1] + distance[1]), (an2[0] + distance[0], an2[1] + distance[1])]:
                if (check_bounds(anti) and anti != an1 and anti != an2):
                    antinodes.add(anti)
print(antinodes)


for y in range(len(map)):
    line = map[y]
    for x in range(len(map[0])):
        if (x, y) in antinodes and line[x] == ".":
            print("#", end="")
        else:
            print(line[x], end="")
    print()
print(len(antinodes))
