a = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
b = a.copy()
print(b)
c= dict(a)
print(c)
#Nested
myFamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myFamily['child2']['name'])
for d,obj in myFamily.items():
    print(d)

    for e in obj:
        print(e)