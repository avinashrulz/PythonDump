def sum3cube(n):
#n = int(input())
    cube = int(n**(1/3))
    print(cube)
    #value = 0
    li = []
    for i in range(cube):
        #print(i)
        li.append(i**3)
        #print(li)
    for k in range(len(li)):
        n = n - li[k]
    for j in range(len(li)):
        if n == li[j]:
            return (True)
        else:
            return(False)
print(sum3cube(10))