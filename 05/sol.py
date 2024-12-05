def checkValid(beforeDict, update):
    for i in range(len(update)): # for each number
        num = update[i]
        for j in range(i + 1, len(update)): # for each number after current number
          if not num in beforeDict:
              return False
          val = update[j]
          # print(f" -> checking: {beforeDict[num]} <- {val}")
          if val not in beforeDict[num]: # if the number is supposed to be before
              # print("  -> False")
              return False
    # print(" |-> True")
    return True
with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    updates = []
    beforeDict = {}
    one = True
    for line in lines:
        if (line == ""):
            one = False
            continue
        if (one):
            k,val = line.split("|")
            value = int(val)
            key = int(k)
            if not key in beforeDict:
                beforeDict[key] = [value]
            else:
                beforeDict[key].append(value)
        else:
            updates.append([int(x) for x in line.split(",")])
    for key in beforeDict:
        beforeDict[key].sort()
    # print(beforeDict)
    # print(updates)
    # verify
    total = 0
    for update in updates:
      # print(f"Update: {update}")
      if checkValid(beforeDict, update):
        total += update[len(update) // 2]
    print(total)