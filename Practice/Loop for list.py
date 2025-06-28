#WAP to print the elements of the following list using a loop
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

i = []
n=1
while n<=10:
    i.append(n*n)
    n+=1
print("List of numbers are: ", i)