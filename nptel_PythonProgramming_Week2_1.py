def mys(m):
    if m==1:
        return (1)
    else:
        return(m*mys(m-1))

#print(mys(0))


x = ["sun",[17],2,"king",[3,4]] # Statement 1
y = x[0:8]                      # Statement 2
z = x                           # Statement 3
w = y                           # Statement 4
z[0] = 0                        # Statement 5
y[0] = y[0][0:3] + 'k'          # Statement 6
y[4][0] = 5                 # Statement 7
#print(x)
#x[0] = x[0][1:3]                # Statement 8
w[4][0] = 1000                  # Statement 9
a = (x[4][0] == 5)              # Statement 10
#print(x[4][0])
#print (a)

x = [589,'big',397,'bash']
y = x[2:]
u = x
w = y
w = w[0:]
w[0] = 357
x[2:3] = [487]
#print(x[2])
#print(y[0])
#print(u[2])
#print(w[0])

first = "abcdefghi"
second = ""
for i in range(len(first)-1,-1,-2):
  second = first[i]+second
#print(second)


alph = [1,2,3,4,5,6,7,8,9,10]
b = []
for i in range(len(alph)-1, -1, -2):
    b=alph[i]
#print(b)

def mystery(l):
  l[0:2] = l[3:5]
  return()
list1 = [34,17,12,88,53,97,62]
mystery(list1)
print(list1)