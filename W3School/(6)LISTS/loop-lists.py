thisList = ["apple", "banana", "cherry"]
for x in thisList:
    print(x)

for i in range(len(thisList)): #Print all items by referring to their index number. 
    print(i) # 0,1,2

j=0
while j<len(thisList):
    print(thisList[j])
    j=j+1

#Using list comprehension
[print(x) for x in thisList]