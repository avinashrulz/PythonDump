new_myList = []

def toAdd(List):
    return (''.join(List))

def permute(myList, l, r): 
    if l==r: 
        print (toAdd(myList))
    else: 
        for i in range(l,r+1): 
            myList[l], myList[i] = myList[i], myList[l] 
            permute(myList, l+1, r) 
            myList[l], myList[i] = myList[i], myList[l] # backtrack

no_of_digits = int(input("Number of digits: " ))
myList = ''
for k in range(0, no_of_digits):
    myListValue = int(input("Input numbers in the list: "))
    myList.join(myListValue)

permute(myList, 0, (no_of_digits-1)) 

 
    