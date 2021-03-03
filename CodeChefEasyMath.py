T = int(input())
while T > 0:
    multiply = 0
    sum = 0
    sumLi = []
    N = int(input())
    li = list(map(int, input().strip().split()))[:N+1]
    (i, j, k) = (0, 0, 0)
    for k in range(len(li)):
        for j in range(len(li)):
            if k!=j:
                multiply = li[k]*li[j]
                print(li[k], li[j], multiply)
    T -= 1
#print (N, T, li)