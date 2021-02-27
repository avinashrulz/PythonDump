#ATM Machine - ATM2

# T = int(input())
# while T > 0:
#     li=[]
#     result = []
#     (n,k) = list(map(int, input().strip().split()))
#     li = list(map(int, input().strip().split()))[:n]    
#     for i in li:
#         if i<=k:
#             k = k - i
#             #result.append(1)
#             print(1, end='')
#         else:
#             #result.append(0)
#             print(0, end = '')
#     #print(result)
#     print()
#     T -= 1


# # print("n: " + str(n))
# # print("k: " + str(k))
# # print("List li: " + str(li))

# #Question - That is my score! WHATSCORE
# T = int(input())

# while T > 0:
#     N = int(input())
#     li = []
#     sum = 0
#     thisDict = {}
#     while N > 0:
#         #For every test, Take 2 inputs
#         (a,b) = map(int, input().strip().split())

#         #If the key is more than 9, don't insert a value in the dictionary, 
#         # but increment the count
#         if a>8:
#             sum = sum
#             N -= 1
#             continue
#         if a not in thisDict.keys():
#             thisDict[a] = b  
#             sum = sum + thisDict[a]     
#         elif thisDict[a]<b:
#             sum = sum - thisDict[a]
#             thisDict[a] = b
#             sum = sum + b
#         N -= 1
#     print(sum)
#     T -= 1          


#Question - That is my score! WHATSCORE. Prettier way of reaching to solution
T = int(input())

while T > 0:
    N = int(input())
    li = []
    sum = 0
    thisDict = {}
    while N > 0:
        #For every test, Take 2 inputs
        (a,b) = map(int, input().strip().split())
        if a>8:
            N -= 1
            continue
        if a not in thisDict.keys():
            thisDict[a] = b  
        elif thisDict[a]<b:
            sum = sum - thisDict[a]
            thisDict[a] = b
        N -= 1
    for k in thisDict:
        sum = sum + thisDict[k]
    print(sum)
    T -= 1          
