def mod3pos(l):
  if len(l) == 0:
    return([])
  else:
    return([l[i] for i in range(len(l)) if i%3==0])
print(mod3pos([19,3,44,44,3,19,17,23]))