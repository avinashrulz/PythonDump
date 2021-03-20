inputlines = []
inputline = input()
while(inputline):
  inputlines.append(inputline)
  inputline = input()

for i in range(len(inputlines)//2,len(inputlines)):
  print(inputlines[i])
for i in range(0,len(inputlines)//2):
  print(inputlines[i])