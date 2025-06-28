my_tuple = (1,2,3,4,5,6,7,8,9)
x = 5
for num in my_tuple:
    if (num == x):
        print ("Number found at: ", my_tuple.index(num) )
        num+=1
        break
    else:
        print("searching...")
    
