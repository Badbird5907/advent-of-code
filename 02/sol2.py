with open("i", "r") as f:
  s = 0
  for l in f:
    li2 = list(map(int, l.split()))
    for i in range(len(li2)):
      li = li2[:i] + li2[i+1:]
      a1 = all(li[i]< li[i+1] <= li[i] + 3 for i in range(len(li)- 1) )
      a2 = all(li[i]> li[i+1] >= li[i]-3 for i in range(len(li)- 1) )
      if a1 or a2:
        s += 1
        break
  print(s)