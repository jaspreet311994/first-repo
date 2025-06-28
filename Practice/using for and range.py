
#for num in range(1,100):
#    print(num)

#for num in range(100,0, -1):
#    print(num)

my_tuple=[]
i = int(input("Enter the number you want to have mulitplication table:"))
temp = int(i)
num = 1
for num in range (1,11):
    mult = num * i
    my_tuple.append(mult)

print("Multiplication table for", temp, "is: ", my_tuple)
