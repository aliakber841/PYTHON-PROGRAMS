thisDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisDict)
print(thisDict['year'])
print(len(thisDict))
print(type(thisDict))
newDict= dict(name = "John", age = 36, country = "Norway")
print(newDict)
x=thisDict.get('model')
print(x)
y=thisDict.keys()
print(y)
thisDict['color']='white'
print(thisDict)
print(thisDict.values())
thisDict['year']=1970
print(thisDict)
z=thisDict.items() # The items() method will return each item in a dictionary, as tuples in a list.
print(z)
if "model" in thisDict:
  print("Yes, 'model' is one of the keys in the thisDict dictionary")
thisDict.update({'year':1964})
print(thisDict)
#The update() method will update the dictionary with the items from a given argument.
#  If the item does not exist, the item will be added.
