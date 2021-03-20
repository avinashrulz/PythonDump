#import math

def myLog(x, b):
    if x < b:
        return 0  
    return 1 + myLog(x/b, b)

T = int(input())
while T>0:
    C = int(input())
    b = 2
    rangePower = myLog(C, b)+1
    rangeLimit = 2**rangePower
    #print(rangePower, rangeLimit)
    maxMultiply = 0
    multiply = 0
    # multiply = [i*j for i in range(rangeLimit-1, 0 , -1) for j in range(rangeLimit-1, i, -1) if i^j == C and multiply == 0]
    for i in range(rangeLimit-1, 0 , -1):
        for j in range(rangeLimit, i, -1):            
            if i^j == C and maxMultiply == 0:
                #print(i, j)
                maxMultiply = i*j
                break
        else:
            continue
        break
    print(maxMultiply)
    T -= 1