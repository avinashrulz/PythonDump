def thirdmax(l):
    (mymax,mysecondmax,mythirdmax) = (0,0,0)
    for i in range(len(l)):
        print(l)
        if len(l)<3:
            break
    # Your code below this line
        if l[0]<l[1]:
            if l[0]<l[2]:
                mythirdmax = l[0]
                print(mythirdmax)
            elif l[2]<l[1]:
                mythirdmax = l[2]
                print(mythirdmax)
        # elif l[0]>l[1]:
        #     if l[2]>l[1]:
        #         mythirdmax = l[1]
        l = l[1:]
    else:
        mythirdmax = l[0]
    return(mythirdmax)
print(thirdmax([9,2,4,1]))