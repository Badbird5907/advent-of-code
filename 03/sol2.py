import re
reg = "(mul\(([0-9]{1,3},[0-9]{1,3})\))|(do\(\))|(don't\(\))"
with open('input.txt') as f:
    lines = f.read().splitlines()
    numbers = [str for line in lines for str in re.findall(reg, line)]
    sum = 0
    e = True
    for num in numbers:
        _, ac, do, dont = num
        if do != "":
            e = True
        elif dont != "":
            e = False
        elif ac != "" and e:
            a,b = ac.split(",")
            sum += int(a) * int(b)
    print(sum)
    
