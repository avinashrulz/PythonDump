(N, H, X) = map(int, input().strip().split())
l = []
count = 0
l = list(map(int, input().strip().split()))
#for i in range(N):
    #ele = int(input())
    #l.append(ele)
for k in l:
    if X+k < H:
        count += 1
        if count == len(l):
            print("NO")
    else:
        print("YES")
        break