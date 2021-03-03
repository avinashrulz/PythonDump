#Standard approach
# T = int(input())
# while T>0:
#     (a, b) = map(int, input().strip().split())
#     temp = 0
#     check = 1
#     while check == 1:
#         temp = a
#         a = a-b
#         if a<0:
#             check = 0
#         else:
#             check = 1
#     print(temp)
#     T -= 1

#Optimized Approach
T = int(input())
while T>0:
    (a, b) = map(int, input().strip().split())
    print(a%b)
    T-=1
