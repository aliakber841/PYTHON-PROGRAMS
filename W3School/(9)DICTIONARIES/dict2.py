x = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x.pop("model") # delete the inserted key
print(x)
x.popitem() # delete the last inserted item
print(x)
del x['brand'] # delete the item with specific key name
print(x)
del x # will delete the dictionary completely
y = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
y.clear() # will clear the dictionary
z = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for a in z:
    print(a) #return value are the keys
    print(z[a]) # return values
for a in z.values(): # return values
    print(a)
for a in z.keys(): # return keys
    print(a)
for b,c in z.items(): # returns both keys and values
    print(b,c)
