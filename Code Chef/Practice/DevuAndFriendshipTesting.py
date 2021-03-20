T = int(input())

while T>=1:
    l = []
    N = int(input())
    l = list(map(int, input().strip().split()))
    l1 = set(l)
    l2 = list(l1)
    print(len(l2))
    T -= 1