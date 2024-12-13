# TODO: Complete this
from aoc_lube import fetch

try:
    with open("input.txt", "r") as f:
        disk = f.read().strip()
except FileNotFoundError:
    disk = fetch(2024, 9, None).strip()

print(disk)

def pretty_print(disk):
    state = False
    for j in range(len(disk)):
        times = int(disk[j])
        char = "." if state else str(j // 2)
        print(char * times, end="")
        state = not state
    print()
pretty_print(disk)

left_ptr = 1
right_ptr = len(disk) - 1
left_free = False

def is_free(ptr):
    return ptr % 2 != 0

while left_ptr <= right_ptr:    
    while (is_free(right_ptr) and left_ptr <= right_ptr):
        print("-1")
        right_ptr -= 1
        break
    
    while (not is_free(left_ptr) and left_ptr <= right_ptr):
        print("+1")
        left_ptr += 1
        break
    left = disk[left_ptr]
    right = disk[right_ptr]

    pretty_print(disk)
    # here, left is at a free space, while right is at a block
    
