import math
list1 = [2,4,5,7]
list2 = list1
list1 = list1[0:2]+[7]+list1[3:]
print(list1)
print(list2)

# list3 = [2,4,6,7,8]
# list4 = list3
# list3[3:] = [10,12]
# print(list3)
# print(list4)

# list3[3:]= [15]
# print(list3)
# print(list4)

# list3[3:]= [18,19,20]
# print(list3)
# print(list4)

# def findps(l,v):
#     for i in range(len(l)):
#         if  l[i] == v: #Exit, report position
#             pos = i
#             break
#     else:
#         pos = -1 # no break, v not in l
#     return(pos)

# print(findps([1,2,3,4,5,6,7,8,9], 10))

# def primepartition(m):
#     if m<0:
#         return False
#     for i in range(2, m//2):
#         if m%i == 0:
#             print("number i: " + str(i))
#             return False
#         else:
#             print("number i in else: " + str(i))
#             continue
#     else:
#         return True
#         i += 1

#print(primepartition(109))

"""
This is working as expected. A decent approach to find all prime numbers
"""
#Implemented the square root method
def primenumber(m):
    if m <= 1:
        return False
    if m == 2:
        return True
    if (m>2 and m%2 ==0):
        return False
    
    max_div = math.floor(math.sqrt(m))
    for i in range(3,max_div,2):
        print(str(i))
        if m%i == 0:
            print(str(m) + " is divided by " + str(i))
            return False
    return True
#print(primenumber(257))

def primepartition(n):
    listPrime = []
 
    # Create a boolean array 
    # "prime[0..n]" and initialize
    #  all entries it as true.
    # A value in prime[i] will
    # finally be false if i is 
    # Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
 
        # If prime[p] is not 
        # changed, then it is a prime
        if (prime[p] == True):
 
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
 
    # Print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            listPrime.append(p)
    for z in listPrime:
        for y in listPrime:
            if z+y == n:
                return True
    return False
#print(SieveOfEratosthenes(3432))

# def primenumber(m):
#     k = m
#     listPrime = []
#     while k>=2: 
#         if m <= 1:
#             return False
#         if m == 2:
#             return True
#         if (m>2 and m%2 ==0):
#             return False
#         max_div = math.floor(math.sqrt(m))
#         for i in range(3,max_div,2):
#             print(str(i))
#             if m%i == 0:
#                 print(str(m) + " is divided by " + str(i))
#                 return False
#         listPrime.append(i)
#         k -= 1
#     print(listPrime)
#print(primenumber(257))
 
# Driver code
# if __name__ == '__main__':
#     n = 30
#     print ("Following are the prime numbers smaller",)
#     print ("than or equal to", n)
#     SieveOfEratosthenes(n)

def matched(s):
    openBracket = 0
    for i in s:
        if i=="(":
            openBracket += 1
        if i == ")" and openBracket!=0:
            openBracket += -1
    if openBracket != 0:
        return False
    else:
        return True
print(matched('((jkl)78(A)&l(8(dd(FJI:),):)?)'))

# def rotatelist(l, k):
#     m = k%len(l)
#     if m == 0:
#         return l
#     else:
#         l = l[-m:]+l[:-m]
#         return l
# print(rotatelist([1,2,3,4,5], 4))

# def rotatelist(l,k):
#     temp = 0
#     if k%len(l)== 0:
#         return l
#     for i in range(k):
#         temp = l[-1]
#         l[-1] = l[0]
#         for k in range(len(l)):
#             l[k] = l[k+1]
#             l[-k+1]=temp
#     return l
# print(rotatelist([1,2,3,4,5], 2))

# def listrotate(l, k):
#     m = k%len(l)
#     n = k-m
#     if m == 5:
#         return l
#     while k>n:
#         l[k],l[n] = l[n], l[k]
#         k -= 1
#         n += 1
# print(listrotate([1,2,3,4,5],1))

def gcd(a, b):
    """ Greatest common divisor of a and b
        Using Euclid's algorithm
    """
    while b:
        a, b = b, a % b
    return a

def rotate_juggle(lst, dist):
    """ An iterative 'juggle' method
    """
    n = len(lst)

    for i in range(gcd(dist, n)):
        t = lst[i]
        j = i
        while 1:
            k = (j + dist) % n
            if k == i: break
            lst[j] = lst[k]
            j = k
        lst[j] = t

print(rotate_juggle([1,2,3,4,5], 2))

def rotatelist(l,k): 
    output_list = [] 
    k = k%len(l)
      
    # Will add values from n to the new list 
    for item in range(k, len(l)): 
        output_list.append(l[item]) 
      
    # Will add the values before 
    # n to the end of new list     
    for item in range(0, k):  
        output_list.append(l[item]) 
    return output_list