
#import time, sys
#print(chr(ord('b')+1))

#a = [ x for x in range(5)]
#b = [x for x in range(7) if x in a and x%2==0]
#print(b)
#print(10//6)
#print(time.time())
#print(sys.argv)


T = int(input())
while T>0:
    N = int(input())
    s = []
    print(type(s))
    e = []
    for x in range(N-1):
        s.append(x)
    for y in range(N-1):
        e.append(y)
    i = 0
    z = 0
    for x in s:
        if e[i]>x:
            s[i], x = x, s[i]
            i += 1
            z = 1
        else:
            z = 0
    if z:
        print('WIN')
    else:
        print('LOSE')            
    T-=1

