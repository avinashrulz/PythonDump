T = int(input())

while T>=1:
    (N, B) = map(int, input().strip().split())
    area = 0
    maxArea = 0
    for i in range(N):
        (W, H, P) = map(int, input().strip().split())
        if P<=B:
            area = W*H
            if maxArea<area:
                maxArea = area
    if maxArea!=0:
        print(maxArea)
    else:
        print("no tablet")
    T -= 1