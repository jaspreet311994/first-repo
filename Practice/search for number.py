#Search for a number x in this tuple using loop
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

i = int(input("Select a number to search in this tuple: "))
n = 0
tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

while n < 10:
    if (tuple[n] == i):
        print("Number you wanted is as pos",n)
        break
    else:
        print("finding...")
    n+=1

