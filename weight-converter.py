weight=input("Enter your weight ")
option=input("L(bs) K(kilos) ")
if option=="l" or option=="L":
    your_weight= int(weight)*0.45
    print(f"Your weight is: {your_weight} kilos")
elif option=="k" or option=="K":
    your_weight= int(weight)//0.45
    print(f"Your weight is: {your_weight} pounds")
