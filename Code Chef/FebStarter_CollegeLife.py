T = int(input())
while T>0:
    wathTime = 0
    Q = []
    L = []
    S = int(input())
    Q = list(map(int, input().strip().split()))[:S+1]
    while S > 0:
        L = list(map(int, input().strip().split()))
        for j in range(1, len(L)):
            wathTime = L[j] + wathTime
            #print(wathTime)
        S -= 1
    if len(L)>2:
        for k in range(len(Q)):
            wathTime = wathTime - Q[k]  
    # for k in range(len(Q)):
    #     wathTime = wathTime - Q[k]
    print(wathTime)
    #print(S, Q, L, E)
    T -= 1