def median3(x,y,z):
    if x <= y:
        if x >= z:
            mymedian = x
        elif y > z:
            median = y
        else:
            median = z
    else:
        if x > z:
            median = x
        elif y < z:
            median = y
        else:
            median = z

  # Your code below this line
  # Your code above this line
    return(mymedian)

l = median3(1,3,2)
print(l)