with open("i", "r") as f:
  s = 0
  for l in f:
    li = list(map(int, l.split()))
    a1 = all(li[i]< li[i+1] <= li[i] + 3 for i in range(len(li)- 1) )
    a2 = all(li[i]> li[i+1] >= li[i]-3 for i in range(len(li)- 1) )
    if (a1 or a2):
      s += 1
  print(s)
