isLate=True
if isLate:
    print("I need to call my BOSS")

car_model="BMW"
car_year=2015
if (2023-car_year) <10 :
    print(f"Your car is {2023-car_year} years old and its almost new we can buy it")
else:
    print(f"Sorry our company doesn't buy {car_model} cars that age is more than 10")
    print(f"Your car age is {2023-car_year}")

car_makers=["Mercedes","Bmw","VW","HONDA","KIA","Hyundai"]
for car in car_makers:
 if car == "Bmw" :
    print(car.upper())
 else:
    print(car.title())
