def disjointlist(l,k):
    for i in range(len(l)):
        for j in range(len(k)):
            if l[i] == k[j]:
                #print(l[i], k[j])
                return (False)
            else:
                continue
    else:
        #print(l[i], k[j])
        return(True)

print(disjointlist([1,2,7,2,5], [6,7,8,9,0]))