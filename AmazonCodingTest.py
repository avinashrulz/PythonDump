# # s = input("Enter a string: " )

# # #print(s)
# # freqCount = []
# # for i in s:
# #     if s.count(i)>1:
# #         if i not in freqCount:
# #             freqCount.append(i)
# # print(freqCount)

# def Dictionary(s):
#     seq = {1: "avinash", 2:"Will work for", 3:"Google one day"}
#     #seq.values() = s
#     print(seq)

# Dictionary("Achyut")

# def SelectionSort(l):
#     for start in range(len(l)):
#         #assuming that the minimum value is at 0 position
#         minpos = start
#         for i in range (start, len(l)):
#             if l[i]<l[minpos]:
#                 minpos = i
#         (l[start], l[minpos]) = (l[minpos], l[start])
#     print(l)

# SelectionSort([2,5,7,3,5,9])

# # def remdup(l):
# #     k = []
# #     for i in l:
# #         for j in l:
# #             if i == j:
                

def remdeup(l):
    seen = set()
    for i in range(len(l)-1, -1, -1):
        if l[i] in seen:
            del l[i]
        else:
            seen.add(l[i])
    return(l)
    #print(l)

print(remdeup([3,5,7,5,3,7,10]))


def remdup(k):
    seen = set()
    for i in reversed(k):
        if i in seen:
            k.remove(i)
        else:
            seen.add(i)
    return(k)
    
print(remdup([3,5,7,5,3,7,10]))

def splitsum(l):
    pos = 0
    neg = 0
    for i in l:
        if i>0:
            i = i*i
            pos += i
        if i<0:
            i = i*i*i
            neg += i
    return([pos, neg])
print(splitsum([1,3,-5]))

def matrixflip(m, d):
  if d == 'v':
    return m[::-1]
  elif d == 'h':
    return [row[::-1] for row in m]
  else:
    return m[:]


 