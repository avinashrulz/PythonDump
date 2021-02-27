# stack = []
# for i in range(5):
#     e = int(input())
#     stack.append(e)
# print("Stack is: " + str(stack))
# print(stack.pop())
# for i in range(N):          # A for loop for row entries 
#     a = [] 
#     for j in range(K):      # A for loop for column entries 
#         a.append(int(input())) 
#     matrix.append(a)

from collections import deque
T = int(input())
matrix = []
while T > 0:
    (N, K, P) = map(int, input().strip().split())
    li = [[int(input()) for x in range(K)] for y in range(N)] 
    #li = list(map(int,input().strip().split()))[:K+1]    
    print(li)
    

    T -= 1