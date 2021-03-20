T = int(input())
while T > 0:
    count = 0
    group = 0
    s = str(input())
    for i in s:
        if i == '1':
            count += 1
            if count == 1:
                group += 1
        else:
            count = 0
    print(group)
    T -= 1