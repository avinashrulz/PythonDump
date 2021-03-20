import math
def squarefree(n):
    sqrt = int(math.sqrt(n))
    for i in range(2,sqrt+1):
        if n%i == 0:
            return(False)
        else:
            return(True)
print(squarefree(48))