name = ''
while True:
    print("Who are you?")
    name = input()
    if name != "Joe":
        print("I'm fine. Thanks! Who are you?")
        continue
    else:
        print("Hello Joe. What is the password? (it is a fish.)")
        pasd = input()
        if pasd == "Swordfish":
            break
print("Access Granted!")