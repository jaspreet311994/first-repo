
dict = {}

marks1 = int(input("Enter your maths marks: "))
marks2 = int(input("Enter your science marks: "))
marks3 = int(input("Enter your english marks: "))

dict.update({"maths" : marks1})
dict.update({"science" : marks2})
dict.update({"english" : marks3})

print(dict)