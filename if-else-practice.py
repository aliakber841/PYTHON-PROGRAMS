is_hot=False
is_cold=True
if is_hot:
    print("It's a hot day.Drink Plenty of water")
elif is_cold:
     print("It's a cold day")
     print("Wear warm clothes")
else:
     print("It's a lovely day")
   
print("Enjoy your day")

price=1000000
buyer_credit= False
if buyer_credit:
    down_payment=(10/100)*price
    print(down_payment)
else:
     down_payment=(20/100)*price
print(f"Down Payment: ${down_payment}")

has_high_income=True
has_good_credit=True
if has_high_income and has_good_credit:
# if has_high_income or has_good_credit:
     print("Eligible for loan")

has_high_income=True
has_criminal_record=False
if has_high_income and not has_criminal_record:
     print("Eligible for loan")

temperature=30
if temperature>=30:
     print("It's a hot day")
else:
      print("It's not a hot day")

name="Ali Akber"
if len(name)<3:
     print("Name must have at Least 3 characters")
elif len(name)>50:
      print("Name can be a maximum of 50 characters")
else:
     print('name looks good')