from aoc_lube import fetch
from math import prod

try:
    with open("input.txt", "r") as f:
        lines = map(str.strip, f.readlines())
except FileNotFoundError:
    lines = fetch(2024, 7, None).splitlines()
equations = []
for l in lines:
  one, two = l.split(": ")
  nums = list(map(int, two.split(" ")))
  equations.append((int(one), nums))


def check(expected, nums, idx, val, two = False):
    # print(" " * i + "Checking", idx, val, nums)
    if (idx == len(nums)): # reached all
        # print(" " * i + " -> ", res)
        return val == expected
    return check(expected, nums, idx + 1, val + nums[idx]) or check(expected, nums, idx + 1, val * nums[idx]) or (two and check(expected, nums, idx + 1, int(str(val) + str(nums[idx]))))

# print(check(100, [1, 10, 10], 1, 1))

def run(two):
    total =0
    for eqtn in equations:
      if (len(eqtn[1]) == 2):
          total += eqtn[0] if (sum(eqtn[1]) == eqtn[0] or prod(eqtn[1]) == eqtn[0]) else 0
      else:
          if (check(
              expected=eqtn[0],
              nums=eqtn[1],
              idx=1,
              val = eqtn[1][0],
              two=two
          )):
              total += eqtn[0]
    print(total)

print("One:")
run(True)
print("Two:")
run(False)