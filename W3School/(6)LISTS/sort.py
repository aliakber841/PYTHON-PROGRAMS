thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
thisList.sort()
print(thisList)
thisList.sort(reverse=True)
print(thisList)
def myFun(n):
    return abs(n-50)
newList=[100,50,65,82,30]
newList.sort(key=myFun)
print(newList) #[50, 65, 30, 82, 100]
#Sort the list based on how close the number is to 50:
thisList.sort(key=str.lower)
print(thisList)
thisList.reverse()
print(thisList)
newList=thisList.copy() # or list(thisList) or thisList[:]
print(newList)