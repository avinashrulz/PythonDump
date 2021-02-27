def merge(A,B):
    (C, m, n) = ([], len(A), len(B))
    (i, j) = (0, 0)

    while i+j<m+n:
        #there is a no check on index j. in previous case, we first check j == n and then
        #proceed to other scenarios. but, after merging the 2 if /elif statements, 
        #we are not performing that action. Therefore, we will switch to the previous 
        #version of the program flow

        if i==m: # or A[i]>B[j]:
            C.append(B[j])
            j += 1
        elif j==n: # or A[i]<=B[j]:
            C.append(A[i])
            i += 1
        elif (A[i]<=B[j]):
            C.append(A[i])
            i += 1
        elif (A[i]>B[j]):
            C.append(B[j])
            j += 1
    return(C)

P = list(range(0,100,2))
Q = list(range(1,75,2))
print(merge(P,Q))