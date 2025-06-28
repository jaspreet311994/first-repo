# WAP to check if a list contains a palindrome of elements.

list = [1,2,1,3]

list1 = list.copy()
list1.reverse()

if (list1 == list):
    print("List is Palindrome")
else:
    print("List is not a Palindrome")