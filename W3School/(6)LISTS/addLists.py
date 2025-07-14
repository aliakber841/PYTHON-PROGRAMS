thisList = ["apple", "banana", "cherry"]
thisList.append("Mango") # adds the value at the end of the list
print(thisList)
thisList.insert(0,'Orange')
print(thisList)
tropical = ["mango", "pineapple", "papaya"]
thisList.extend(tropical) # adds the values of another list
print(thisList)
thisTuple = ("kiwi", "orange")
thisList.extend(thisTuple) # adds the value of tuples too
print(thisList)