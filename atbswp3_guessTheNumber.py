import random
num = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")
counter = 0
while True:
    print("Take a Guess!")
    guess = int(input())
    counter = counter + 1
    if guess == num:
        print("Good Job! you guessed my number in " + str(counter) + " guesses.")
        break
    elif guess < num:
        print("Your guess is too low.")
    elif guess > num:
        print("Your guess is too high.")