aList = [15,16,17,18,18,16, 17, 19,1,2,3,4,5,5,6,7,7,8,8,9,9,9,9,10]
aSet = set(aList)
#print(len(aList))
#print(aSet)


def MergeSort(A,left,right):
    if right-left <= 1:
        return(A[left:right])
    elif (right-left>1):
        mid = (right+left)//2
        L = MergeSort(A,left,mid)
        R = MergeSort(A,mid,right)
        return(Merge(L,R))

#Merging 2 Sorted Arrays - Part of Merge Sort
def Merge (A, B):
    (C, m, n) = ([], len(A), len(B))
    (i, j) = (0, 0)

    while i+j<m+n:
        #end of list A
        if (i==m):
            C.append(B[j])
            j = j + 1
        #end of list B
        elif j==n:
            C.append(A[i])
            i = i + 1
        #Comparison of values in both the list, copying the least value in a selarate list
        #incrementing the list index of the list from which the value was copied
        elif A[i]<=B[j]:
            C.append(A[i])
            i = i + 1
        elif A[i]>B[j]:
            C.append(B[j])
            j = j + 1
    return(C)

#Test Case
#print(Merge([2,5,7,9], [1,3,5,6,8]))
a = [88,60,26,47,55,77,29,91]
print(MergeSort(a, 0, len(a)))































# def rainaverage(l):
#   (t1,t2,t3)=({},{},{})
#   for i,j in l:
#     if i not in t1:
#       (t1[i],t2[i])=(j,1)
#     else:
#       (t1[i], t2[i]) = (t1[i]+j,t2[i]+1)
#   for i,j in t2.items():
#     t3[i]=float(t1[i]/j)
#   l2=[(i,j) for i,j in t3.items()]
#   l2.sort(key=lambda  a:a[0])
#   return l2

# def listtype(l):
#   return type(1) == type([]) 
# l3=[]
# def flatten(l4):
#   for i in l4:
#     if listtype(i):
#       flatten(i)
#     else:
#       l3.append(i)
#   return l3