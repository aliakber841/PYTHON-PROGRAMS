print(10 > 9)
print(10 == 9)
print(10 < 9)

a=4
b=90
if b>a:
    print("b is greater than a")
else:
    print('a is greater than b')

print(bool("Hello"))
print(bool(15))
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.
#The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

print(myFunction())

def test():
   return True

if test():
   print("YES")
else:
   print("NO")

#Python also has many built-in functions that return a boolean value, like the isinstance() function,
#  which can be used to determine if an object is of a certain data type:
a=900
print(isinstance(a,int))