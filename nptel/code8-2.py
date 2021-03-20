def maxdifference(l):
    aggregate = {}
    innings = {}
    maxi = 0
    mini = 0
    for (name,score) in l:
        #maxi = max(score)
        #mini = min(score)
        try:
            aggregate[name] += score
        except KeyError:
            aggregate[name] = score
    maxdifference = []
    maxDiff = []
    for name in aggregate.keys(): 
        #maxDiff = max(aggregate.values())-min(aggregate.values())
        maxdifference.append(name)
        sorted(maxdifference)
    return(maxdifference[0])

print(maxdifference([('Kohli',73),('Ashwin',23),('Kohli',17),('Pujara',142),('Kohli',45),('Ashwin',60)]))