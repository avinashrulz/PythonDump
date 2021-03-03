T = int(input())
while T>0:
    s = str(input())
    count = 0 
    for i in range(len(s)-1):
        if s[i] == '<':
            if s[i+1] == '>':
                count += 1
    print(count)               
    T -= 1