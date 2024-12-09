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
    if (idx == len(nums)): # reached all
        return val == expected
    return check(expected, nums, idx + 1, val + nums[idx]) or check(expected, nums, idx + 1, val * nums[idx]) or (two and check(expected, nums, idx + 1, int(str(val) + str(nums[idx]))))

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
run(False)
print("Two:")
run(True)