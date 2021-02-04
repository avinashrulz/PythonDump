print(format("Hello", "10s"), end = '#')
print(format(111, "4d"), end = '#')
print(format(924.656, "3.2f"))
#print("This is spart" + repr(123))
#x= ['abc', 'def']
#y = ['def', 'abc']
#print(id(x)==id(y))
#print(id(y))
#help(id)

def f(x):
    d=0
    y=1
    while y<=x:
        d=d+1
        y=y*3
    return (d)

value = f(846)
print(value)


def h(n):
    s = 0
    for i in range(1, n+1):
        if n%i > 0:
            s = s+1
    return (s)

k = h(41)
print (k)

def g(m,n):
    res = 0
    while m>=n:
        res = res+1
        m = m-n
    return(res)

l = g(57, 8)
print(l)

def mys(m):
    if m == 1:
        return(1)
    else:
        return(m*mys(m-1))

p = mys(-1)
print(p)
