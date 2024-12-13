from aoc_lube import fetch
from collections import defaultdict

try:
    with open("input.txt", "r") as f:
        input = f.read().strip().splitlines()
except FileNotFoundError:
    input = fetch(2024, 12, None).strip().splitlines()

matrix = []
for line in input:
    matrix.append(list(line))

print(matrix)

def inBounds(x,y):
    return 0 <= x < len(matrix[0]) and 0 <= y < len(matrix)
def get(x,y):
    if (inBounds(x,y)):
        return matrix[y][x]
    return None

def identify():
    queue = [(0,0)]
    visited = set()
    plants = defaultdict(list) # { A: [([perim], [area])] } - THIS IS NOT OPTIMIZED
    total = 0
    visited = set([(0,0)])
    while len(queue) > 0:
        pos = queue.pop(0)
        x,y = pos
        total += 1
        current = get(*pos)
        li = plants[current]
        
        connected_regions = []
        for i, (region_perim, region_area) in enumerate(li):  # unpack both perim and area
            for nPos in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                if nPos in region_area:  # check against area, not just perimeter
                    connected_regions.append(i)
                    break
        
        if len(connected_regions) == 0:  # new region
            li.append(([], set([pos])))  # ([perimeter], [area])
            perim, area = li[-1]
        elif len(connected_regions) == 1:  # add to existing region
            perim, area = li[connected_regions[0]]
            # perim.append(pos)
        else:  # merge regions
            base_region = connected_regions[0]
            perim, area = li[base_region]
            # perim.append(pos)
            
            for region_idx in reversed(connected_regions[1:]):  # merge other regions into base region
                other_perim, other_area = li[region_idx]
                perim.extend(other_perim)
                area.update(other_area)
                li.pop(region_idx)
        area.add(pos)
        next = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
        
        for nPos in next:
            if inBounds(nPos[0], nPos[1]):
                if get(*nPos) != current:
                    perim.append(pos)
                if nPos not in visited:
                    nVal = get(*nPos)
                    iPos = 0 if nVal == current else -1  # priority for same type
                    queue.insert(iPos, nPos)
                    visited.add(nPos)
            else:
                perim.append(nPos)
    print("Total Plants: ", len(plants))
    result = 0
    totalRegions = 0
    for key in plants.keys():
        li = plants[key]
        print(key)
        for region in li:
            perim, area = region
            perm_len = len(perim)
            print(f" -> A: {len(area)} | P: {perm_len}")
            totalRegions += 1
            result += perm_len * len(area)
    print("Total Regions: ", totalRegions)
    print("Result: ", result)

identify()