secret_number = 777
a = int(input("Enter the random number="))
while a:
    if a == secret_number:
        print("Well done, muggle! You are free now.")
        break
    else:
        print("Ha ha! You're stuck in my loop!")
        break
