no_of_digits = int(input("Number of digits: " ))
myList = []
for i in range(0, no_of_digits):
    myListValue = int(input("Input numbers in the list: "))
    myList.append(myListValue)
#no_of_possible_lists = math.factorial(no_of_digits)
no_of_possible_lists = 1
for j in range(1, (no_of_digits+1)):
    no_of_possible_lists = no_of_possible_lists*j

print(no_of_possible_lists)

print(myList)
#while (no_of_digits>0):


