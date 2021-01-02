#Using Reversal Algorithm

a = [1, 2, 3, 4, 5]
n = len(a)
rev = 2
def reverseArraay(arr, start, end):
    while (start<end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
b = [1, 2]
c = [3, 4, 5]
b.reverse()
print (b)
c.reverse()
print (c)
#a = b + c
for x in c:
    b.append(x)
b.reverse()
print (b)