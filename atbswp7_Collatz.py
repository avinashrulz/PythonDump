import sys

try:
    print("Enter any number:")
    inputValue = int(input())    
    while True:
        if inputValue != 1:
            if inputValue%2==0:
                result = inputValue//2
                print(result)
                inputValue = result
            else:
                result = 3*inputValue+1
                print(result)
                inputValue = result
        else:
            break
except KeyboardInterrupt:
    sys.exit