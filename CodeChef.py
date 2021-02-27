# QUESTION 1
# def TotalExpenses():
#     N = int(input())
#     discount = 0.9
#     while N>0:
#         finalPrice = 0
#         (quantity,price)=list(map(int,input().split()))
#         if quantity>1000:
#             finalPrice = quantity*price*discount
#         else:
#             finalPrice = quantity*price
#         print(finalPrice)
#         #return(finalPrice)
#         N -= 1
# print(TotalExpenses())

# QUESTION 2
# def gradeSteel():
#     N = int(input())
#     while N>0:
#         finalDecision = 5
#         (hn,cc,ts)=list(map(float,input().split()))
#         if hn>50 and cc<0.7 and ts>5600:
#             finalDecision = 10
#         elif hn>50 and cc<0.7:
#             finalDecision = 9
#         elif cc<0.7 and ts>5600:
#             finalDecision = 8
#         elif hn>50 and ts>5600:
#             finalDecision = 7
#         elif hn>50 or cc<0.7 or ts>5600:
#             finalDecision = 6
#         else:
#             finalDecision = 5

#         print(finalDecision)
#         #return(finalPrice)
#         N -= 1
# print(gradeSteel())

# QUESTION 3 - Minimum Maximum

# a = [4,2,5]
# n = len(a)
# print("n: " + str(n))

# cost = 0
# j = 1
# i = 0
# print("i: " + str(i))
# print("j: " + str(j))

# while True:
#     if n<=1:
#         print("Final Cost: " + str(cost))
#         break
#     elif a[i]>a[j]:
#         cost = cost + a[j]
#         print("cost 1: " + str(cost))
#         del a[i]
#         n -= 1
#         #i = i+1
#         print("List1: " + str(a))
#     else:
#         cost = cost + a[i]
#         print("cost 2: " + str(cost))
#         del a[j]
#         n -= 1
#         #j = j+1
#         print("List2: " + str(a))
# print(cost)

#Question 3 - Code Chef - Minimum Maximum
# K = int(input())
# while K > 0:
#     size = int(input())  
#     # Below line read inputs from user using map() function  
#     l = list(map(int,input().strip().split()))[:size]

#     n = len(l)
#     cost = 0
#     i = 0
#     j = 1

#     while True:
#         if n<=1:
#             #print("Final Cost: " + str(cost))
#             break
#         elif l[i]>l[j]:
#             cost = cost + l[j]
#             #print("cost 1: " + str(cost))
#             del l[i]
#             n -= 1
#             #i = i+1
#             #print("List1: " + str(a))
#         else:
#             cost = cost + l[i]
#             #print("cost 2: " + str(cost))
#             del l[j]
#             n -= 1
#             #j = j+1
#             #print("List2: " + str(a))
#     K -= 1
#     print(cost)

# QUESTION 4
# k = 2
# li = list(map(int,input().strip().split()))[:k]
# n = li[1]


#N = li[1]
#l = list(map(str,input().strip().split()))[:N]
#print(l)



'''Working code for closing the tweet
complete it soon'''

# lst = []
# for i in range(0, n): 
#     ele = str(input()) 
#     lst.append(ele) # adding the element
# for j in range(0, len(lst)):
#     value = lst[j][-1]
#     if lst[j][-1] == '1':
#         print("Last is 1")
#     else:
#         print("Last is not 1")

#Question 4 - counting the snackdown

n = int(input())
lst = []
#while n>0:
for i in range(0,n):
    ele = int(input()) 
    lst.append(ele) # adding the element
for j in lst:
    if j in [2010, 2015, 2016, 2017, 2019]:
        print("HOSTED")
    else:
        print("NOT HOSTED")
