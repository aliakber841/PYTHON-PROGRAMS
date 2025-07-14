mySet = {"apple", "banana", "cherry"}
print(mySet)
#The values True and 1 are considered the same value in sets, and are treated as duplicates
print(len(mySet))
print(type(mySet))
newSet=set((1,2,3))
print(mySet)
#You cannot access items in a set by referring to an index or a key.
for x in mySet:
    print (x)
print("banana" in mySet)
#add.
mySet.add('orange')
print(mySet)
x = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
x.update(tropical)
print(x)
myList=[1,2,3,4]
x.update(myList)
print(x)
x.remove('apple') #If the item to remove does not exist, remove() will raise an error.
print(x)
x.discard('banana') #If the item to remove does not exist, discard() will NOT raise an error.
print(x)
x.pop() #Removes a random item
print(x)
tropical.clear() #empties the set
print(tropical)
del tropical # del the set completely
for x in mySet:
    print(x)