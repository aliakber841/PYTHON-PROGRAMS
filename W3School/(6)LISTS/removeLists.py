thisList = ["apple", "banana", "cherry"]
thisList.remove("apple") #removes that value
print(thisList)
thisList.append('banana') # adds at the end
thisList.remove('banana')
print(thisList)
thisList.pop(0) # pops the given index if specified
print(thisList)
thisList.append('apple')
print(thisList)
thisList.pop() # pops last value if index is not specified
print(thisList)
thisList.append('apple')
print(thisList)
del thisList[0] # del the value at the given index
print(thisList)
del thisList # del the list
newList=["apple", "banana", "cherry"]
newList.clear() # empties the list
print(newList)