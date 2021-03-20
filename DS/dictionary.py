score = {}
score["test1"] = {}
score["test2"] = {}
score["test1"]["Kohli"]= 123
score["test1"]["Dhawan"] = 32
score["test2"]["Dhawan"] = 145
print(score)

# randdom = {}
# for l in "abcdefghi":
#     randdom[l] = l
#     print(randdom[l])
# print (randdom.keys())
# print(randdom.values())
# a = "111"
# print(int(a, 2))

#Print 4x3 matrix initialized with zero values
l = [ [0 for i in range(3)] for j in range(4)] 
print(l)

rowlist = [0 for i in range(3)]
k = [rowlist for j in range(4)]
print(k)
k[1][1] = 9
print(k)