#Question 1
# N = int(input())

# for i in range(0, N):
#     BMI = 0
#     result = 0
#     (a, b) = map(int, input().strip().split())
#     BMI = a//(b**2)
#     if BMI <= 18:
#         result = 1
#     elif BMI <=24:
#         result = 2
#     elif BMI <=29:
#         result = 3
#     else:
#         result = 4
#     print(result)
#     N -= 1

#question 2
#Enter number of Tests
T = int(input())

# For each test, Accept the inputs
while T > 0:
    #An empty list to store problem scores
    li = []

    #Enter the number of students(N) and number of problems(K)
    (N, K) = map(int, input().strip().split())

    #for K problems, accept the score for each problem and store in the list li
    li = list(map(int, input().strip().split()))[:K]

    #For each student, check the success or failure of solving problems
    for i in range(0,N):
        #Enter the success-failure string for each user
        st = str(input())

        #Initialize s as the toral score to 0
        s = 0

        #for each index of the string, check success(1) or Failure(0)
        for j in range(len(st)):

            #If success, add the corresponding score to total sum
            if st[j] == '1':
                s = s + li[j]

            #Else will be the failure scenario where there is no change in total score
            else:
                s = s
        
        #Print total score for each test
        print(s)

    #Increment the value of test
    T -= 1
