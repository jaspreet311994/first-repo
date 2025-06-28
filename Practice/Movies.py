# list =[]

# list.append(input("enter the first movie: "))
# list.append(input("enter the second movie: "))
# list.append(input("enter the third movie: "))

# print ("Three movies are: ", list)

list = [1,2,3,2,1]

list1 = list.copy()
list.reverse()

if(list1 == list):
    print("List is palindrome.")
else:
    print("List is not palindrome.")

