x="ali"
def myfun():
    x="rajab"
    print('my name is ',x)
myfun()
print('my name is ',x)
#when you create a variable inside a function, that variable is local, and can only be used inside that function.
#To create a global variable inside a function, you can use the global keyword.
def myfun():
 global y
 y="rajab"
 print('my name is ',y)
myfun()
print('my name is ',y)
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)