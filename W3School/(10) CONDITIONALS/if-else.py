a = 33
b = 200
if b > a:
  print("b is greater than a")
elif a == b: #if the previous conditions were not true
  print("a and b are equal") 
else: # The else keyword catches anything which isn't caught by the preceding conditions.
  print("a is greater than b")
# You can also have an else without the elif:
if a > b: print("a is greater than b") # Shorthand if
#Ternary Operator
print("A") if a > b else print("B") 
print("A") if a > b else print("=") if a == b else print("B") # 3 conditional
c=500 
if a>b and c>a:
  print('Condition satisfied')
else:
  print('Condition not satisfied')
if a > b or c > a:
  print("At least one of the conditions is True")
if not a > b:
  print("a is NOT greater than b")
# Nested If statements
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
# Pass statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, 
# put in the pass statement to avoid getting an error.
if b > a:
  pass