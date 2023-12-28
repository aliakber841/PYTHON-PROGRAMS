myspecial=[5,22,36,27,90,12]
car_makers=["Mercedes","BMW","VW","HONDA","KIA","Hyundai"]
print(car_makers)
print(myspecial[3])
print(car_makers[0].upper())  # -1 always returns last item in the list
print(f"My first car was {car_makers[1].title()}")
car_makers[2]="SAAB"
print(car_makers)
car_makers.append("Jeep")
print(car_makers)
car_makers.insert(0,"Lexus")
print(car_makers)
del car_makers[2]
print(car_makers)

popped_car=car_makers.pop() #Pop from the top of stack
print(f" The deleted car was {popped_car}")
print(car_makers)

popped_car=car_makers.pop(0)
print(car_makers)

too_expensive="KIA"
car_makers.remove(too_expensive)
print(car_makers)
print(f"{too_expensive.title()} was expensive for me")

car_makers.sort()
print(car_makers)

car_makers.sort(reverse=True)
print(car_makers)

print(sorted(car_makers))
print(car_makers)

car_makers.reverse()
print(car_makers)

print(len(car_makers))