#Multiline Strings
a="""
My name is ali
my age is 22
"""
print(a)
#strings in Python are arrays of bytes representing unicode characters.
print(a[2])
for x in a:
    print(x)
print(len(a))
print('age' in a) # to check whether a part of string is present or not
if "age" in a:
    print('age is present in a')
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")