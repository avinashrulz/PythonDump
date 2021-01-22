def exampleFunction():
    """ This is for the help function to identify what this code does
    """
    print("This is good")
    numbers = [0,1,2,3,4,5]
    print(numbers)
    print(numbers[0:2])
    print(numbers[2:])
    print(numbers[:4])
    print("Printing Elements From Last - The Last Element Is " + str(numbers[-1]))
    print(max(numbers))
    print(min(numbers))
    numbers.append('Avinash')
    print(numbers)
    print(numbers.pop())
    print(numbers.index(4))
    print(2**3) 
    print(4/3)
    print(4//3)
    listoflists = [[1,2,3], ['a','b','c'], ['X','Y','Z']]
    print ("Length of listoflists is " + str(len(listoflists)))
    print(listoflists[2][1])

def exampleFunctionLoops():
    s = 'steganograpHOy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
    msg = 'Avinash is awesome'
    # print all the uppercase letters in s, one at a time
    for char in s:
        if char.isupper():
            print(char, end = '')
    for i in range(3):
        print (msg, i)

#The argument of the while loop is evaluated as a boolean statement, 
# and the loop is executed until the statement evaluates to False.
def exampleWhileLoop():
    """The argument of the while loop is evaluated as a boolean statement, 
    and the loop is executed until the statement evaluates to False."""
    i = 0
    while i < 10:
        print(i, end=' ')
        i += 1


exampleFunction()
exampleFunctionLoops()
exampleWhileLoop()

def StringManipulation():
    print("Welcome to String Manipulation Task")
    print("All operations on a list can also happen on thrings, but strings are immutable")
    test="This is a typical string."
    timeInput = "12/23/2020"
    month, date, year = timeInput.split('/')
    print('-'.join([month, date, year]))
    print(test.split())
    print(test.split('s'))
    print(timeInput.split('/'))
    decimal_no = 23.3456
    print("Hello {}, this is awesome experience on the {}th day of the year!!!".format(test, date))
    print("Hello {0}, this is awesome experience on the {1}th day of the year!!! {1} is a good number, {0} is even better!!!".format(test, decimal_no))

def WorkingWithDictionaries():
    numbers = {"one": 1, "two": 213221, "three": 3}
    print (numbers["two"])
    numbers["eleven"] = 123
    print (numbers["eleven"])
    numbers["two"] = 1234
    print (numbers["eleven"])
    print(numbers)
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    planets_initial = {planet: planet[0:3] for planet in planets}
    print(planets_initial)
    join_all = ' '.join(planets_initial.values())
    print(join_all)
    for k in numbers:
        print("{} = {}".format(k, numbers[k]))
    for planet, initial in planets_initial.items():
        print("{} begins with \"{}\"".format(planet.rjust(10), initial))

StringManipulation()
WorkingWithDictionaries()