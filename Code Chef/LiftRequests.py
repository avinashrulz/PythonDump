import math
T = int(input())
while T > 0:
    (a,b) = map(int, input().strip().split())
    count = 0
    lastFloor = 0
    while b > 0:
        (c,d) = map(int, input().strip().split())
        count = count + abs(lastFloor - c)+abs(c-d)
        lastFloor = d
        b -= 1
    print(count)
    T -= 1