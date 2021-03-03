T = int(input())
while T> 0:
    N = int(input())
    count = 0
    while N > 0:
        (a, b) = map(int, input().strip().split())
        if b - a > 5:
            count += 1
        N -= 1
    print(count)
    T -= 1