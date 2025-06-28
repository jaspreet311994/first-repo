marks = [56,34,124,78]
print(marks[0:len(marks)])

marks.append(45)
print(marks[0:len(marks)])

marks.sort()
print(marks[0:len(marks)])

marks.sort(reverse=True)
print(marks[0:len(marks)])

marks.insert(1,65)   #here insert(location, value to be inserted)
print(marks[0:len(marks)])