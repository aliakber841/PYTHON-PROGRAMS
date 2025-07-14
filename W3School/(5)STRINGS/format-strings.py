age=22
print(f"My name is Ali. My age is {age}")
price = 59
txt = f"The price is {price} dollars"
print(txt)
txt = f"The price is {price:.2f} dollars" #Display the price with 2 decimals
print(txt)
#A placeholder can include a modifier to format the value.
#A modifier is included by adding a colon : followed by a legal formatting type, 
# like .2f which means fixed point number with 2 decimals:
txt = f"The price is {20*10} dollars"
print(txt)
txt = "We are the so-called \"Vikings\" from the north."

fruit = "apples"
txt=f"I love {fruit.upper()}"
print(txt)

def myConverter(x):
  return x * 0.3048
txt = f"The plane is flying at a {myConverter(30000)} meter altitude"
print(txt)

price = 59000
txt = f"The price is {price:,} dollars"
print(txt)

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

quantity = 3
itemNo = 567
price = 49
#myOrder = "I want {} pieces of item number {} for {:.2f} dollars."
myOrder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myOrder.format(quantity, itemNo, price))

myOrder = "I have a {carName}, it is a {model}."
print(myOrder.format(carName = "Ford", model = "Mustang"))