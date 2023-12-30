car_makers=["Mercedes","BMW","VW","HONDA","KIA","Hyundai"]
for car in car_makers:
    print(car)
    print(f"{car.title()} great car ! ")

print("Thank you every car makers, these cars are special and great")


   #Loop With Range
for myvalue in range(1,10):
    print(myvalue)

for myvalue in range(6):
    print(myvalue)

mySpecialNumbers= list(range(1,11))
print(mySpecialNumbers)

mySpecialNumbers= list(range(2,11,2))  #Add 2 to number (3rd Argument)
print(mySpecialNumbers)

mySquares=[]
for myValue in range(1,11) :
 mySquare=myValue **2
 mySquares.append(mySquare)
print(mySquares)

    #Slices in with Lists and Loops
car_makers=["Mercedes","BMW","VW","HONDA","KIA","Hyundai","Nissan"]
print(car_makers[0:3])
print(car_makers[:4])
print(car_makers[3:])
print(car_makers[-3:])
print("Here are the first four car makers in my list:")
for car_maker in car_makers[:4]:
   print(car_maker.title())

   #Slices VS Var for Copying List
my_favorite_cars =["Mercedes","BMW","VW","HONDA","KIA","Hyundai","Nissan"]
friend_favorite_cars= my_favorite_cars[:]

my_favorite_cars.append("Toyota")
friend_favorite_cars.append("Fiat")

print("My favorite cars are:")
print(my_favorite_cars)

print("\nMy Friends favorite cars are:")
print(friend_favorite_cars)