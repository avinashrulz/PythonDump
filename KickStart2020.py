T = int(input())
case = 0
while T>0:
    (A, B) = map(int, input().strip().split())
    count = 0
    li = list(map(int, input().strip().split()))[:A+1] 
    li.sort()
    #print(li)
    for j in range(len(li)):
        if li[j]<=B:
            B = B-li[j]
            count += 1
    case += 1
    print("Case #" + str(case) + ":" + str(count))
    T -= 1  
    