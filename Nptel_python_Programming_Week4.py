def mystery(l):
  if (l == []):
    return(l)
  else:
    mid = len(l)//2
    if (len(l)%2 == 0):
      return l[mid-1:mid+1] + mystery(l[:mid-1]+l[mid+1:])
    else:
      return l[mid:mid+1] + mystery(l[:mid]+l[mid+1:])

print(mystery([22,14,19,65,82,55]))

triples = [ (x,y,z) for x in range(1,4) for y in range(2,5) for z in range(5,8) if x+y > z ]
print(triples)
marks = {"Quizzes":{"Mahesh":[3,5,7,8],"Suresh":[9,4,8,8],"Uma":[9,9,7,6]},"Exams":{"Mahesh":[37],"Uma":[36]}}
#marks["Exams"]["Suresh"].extend([44])
marks["Exams"]["Suresh"] = [44]
#marks["Exams"]["Suresh"][0:] = [44]
print(marks)

inventory = {}
#inventory["Amul"] = ["Mystic Mocha",55]
#print(inventory)
inventory["Amul, Mystic Mocha"] = 55
print(inventory)