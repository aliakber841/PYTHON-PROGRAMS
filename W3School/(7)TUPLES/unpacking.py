fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits2 # red will be a list
print(green)
print(yellow)
print(red)

(green, *yellow, red) = fruits2
print(green)
print(yellow)
print(red)

