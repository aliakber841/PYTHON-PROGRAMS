def my_function():
    print('Hello World')
my_function()

def name(n): #parameter is the variable listed inside the parentheses in the function definition.
    print(f'My name is {n}')
name('Ali') #argument is the value that is sent to the function when it is called.

def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Ali", "Akber")

def unknown(*kids): #If the number of arguments is unknown, add a * before the parameter name:
   print('The youngest child is ' + kids[2])
unknown("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):
  print("The youngest child is " + child1)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary keyword arguments
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")
#If the number of keyword arguments is unknown, add a double ** before the parameter name:
#Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.

def my_function(country = "Norway"): # default value
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
# If we call the function without argument, it uses the default value

#Passing a List as an Argument
def foodItems(food):
   for x in food:
      print(x)
fruits=['apple','banana']
foodItems(fruits)

# Return values
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

def my_function(): #if you for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.
  pass

# Positional Only Arguments
def my_function(x, /): #To specify that a function can have only positional arguments, add , / after the arguments:
  print(x)
my_function(3)

def my_function(x): #Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
  print(x)
my_function(x = 3)

#Keywords only arguments
def my_function(*, x): #To specify that a function can have only keyword arguments, add *, before the arguments:
  print(x)
my_function(x = 3)
#Without the *, you are allowed to use positional arguments even if the function expects keyword arguments:
#But with the *, you will get an error if you try to send a positional argument

#Combine Positional-Only and Keyword-Only
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)

# Recursion Functions
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("Recursion Example Results:")
tri_recursion(6)

