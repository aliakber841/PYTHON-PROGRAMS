fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList=[]
for f in fruits:
    if "a" in f:
        newList.append(f)
print(newList)
newList=[ f for f in fruits if "b" in f]
print(newList)
newList=[f for f in fruits if 'apple' != f]
print(newList)
newList=[f for f in fruits]
print(newList)
newList = [x for x in range(10) if x < 5]
print(newList)
newList=[x.upper() for x in fruits]
print(newList)
newList=['hello' for x in fruits]
print(newList)
newList = [x if x != "banana" else "orange" for x in fruits]
print(newList)