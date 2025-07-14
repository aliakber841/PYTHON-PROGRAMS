myList=['fruits','vegetables']
print(myList)
print(len(myList))
print(type(myList))
list2=list(("apple","banana","orange"))
print(list2)
print(list2[2])
print(myList[-2])
print(list2[0:2])
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList[:4])
print(thisList[2:])
print(thisList[-4:-1])
if "apple" in thisList:
    print("There is an apple")

#Changing the lists
thisList[0]='Pomegranate'
print(thisList)
thisList[1:3]=['guava','pineapple']
print(thisList)
thisList[1:2]=["blackcurrant", "watermelon"]
print(thisList)
newList=["apple", "banana", "cherry"]
newList[1:3]=['watermelon']
print(newList)
newList.insert(2,'Guava')
print(newList)
