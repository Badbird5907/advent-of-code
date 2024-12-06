def checkValid(beforeDict, update):
    for i in range(len(update)): # for each number
        num = update[i]
        for j in range(i + 1, len(update)): # for each number after current number
          if not num in beforeDict:
              return False
          val = update[j]
          if val not in beforeDict[num]: # if the number is supposed to be before
              return False
    return True
def fix(beforeDict, update):
    # print(f"Fixing {update}")
    for i in range(len(update)): # for each number
        num = update[i]
        if not num in beforeDict:  # Add this check
            # move to end
            update.append(num)
            update.pop(i)
            continue
        for j in range(i + 1, len(update)): # for each number after current number
          val = update[j]
          if val not in beforeDict[num]: # if the number is supposed to be before
              # swap
              update[i], update[j] = update[j], update[i]
    # print(update)
    return update
with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    updates = []
    rules = {}
    one = True
    for line in lines:
        if (line == ""):
            one = False
            continue
        if (one):
            k,val = line.split("|")
            value = int(val)
            key = int(k)
            if not key in rules:
                rules[key] = [value]
            else:
                rules[key].append(value)
        else:
            updates.append([int(x) for x in line.split(",")])
    for key in rules:
        rules[key].sort()
    # print(beforeDict)
    # print(updates)
    # verify
    total = 0
    for update in updates:
      # print(f"Update: {update}")
      if not checkValid(rules, update):
        while not checkValid(rules, update): # thanks, https://www.reddit.com/r/adventofcode/comments/1h75sp4/2024_day_5_it_works_though/
            update = fix(rules, update)
        total += update[len(update) // 2]
    print(total)