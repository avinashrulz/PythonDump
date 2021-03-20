T = int(input())
while T>0:
    (N,U,D) = map(int, input().strip().split())
    li = []
    count = 0
    parchute = 0
    li = list(map(int, input().strip().split()))[:N+1]
    print(li)
    for x in range(1, len(li)):
        print(li[x-1])
        if li[x-1] <= li[x]:
            if li[x-1] - li[x]<=U:
                count += 1
        if li[x-1] > li[x]:
            if li[x-1] - li[x]<=D:
                count += 1
            elif parchute == 0:
                count += 1
    print(count)
    T -= 1