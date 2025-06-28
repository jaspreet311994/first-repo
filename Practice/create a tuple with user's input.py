#asking user to add items to tuple

my_tuple = []
j=1
n=int(input("How many numbers do you want to add in tuple: "))

while j <= n:
    i = int(input("Enter the numbers to be added: "))
    my_tuple.append(i)
    j+=1

print(my_tuple)