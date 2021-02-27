def BinarySearch(l, a):
    start = 0
    end = len(l)
    midPos = (start+end)//2
    if l[midPos] == a:
        return(midPos)
    if l[midPos] > a:
        for i in range(start, midPos):
            if l[i] == a:
                return(i)
    if l[midPos] < a:
        for i in range(midPos+1, end - 1):
            if l[i] == a:
                return(i)

print(BinarySearch([2,5,7,9,12,13,15,17,19], 18))


#Time - O(n^2), space - O(n)
def SelectionSort(l):
    for start in range(len(l)):
        #assuming that the minimum value is at 0 position
        minpos = start
        for i in range (start, len(l)):
            if l[i]<l[minpos]:
                minpos = i
        (l[start], l[minpos]) = (l[minpos], l[start])
    print(l)

SelectionSort([2,5,7,3,5,9])

def InsertionSort(l):
    for sliceEnd in range(len(l)):
        pos = sliceEnd
        while pos>0 and l[pos] < l[pos-1]:
            (l[pos], l[pos-1])=(l[pos-1], l[pos])
            pos = pos - 1

def Palliandorme(n):
    # OK
    
