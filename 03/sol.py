import re

reg = "mul\(([0-9]{1,3},[0-9]{1,3})\)"
with open('input.txt') as f:
    lines = f.read().splitlines()
    numbers = [str for line in lines for str in re.findall(reg, line)]
    sum = 0
    for num in numbers:
        a, b = num.split(',')
        sum += int(a) * int(b)
    print(sum)
    
