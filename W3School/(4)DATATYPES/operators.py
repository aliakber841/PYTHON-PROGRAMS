print(1+2)	
# **	Exponentiation	x ** y	
# //	Floor division	x // y
# Arithmetic Operators includes +,-,*,/,%,**,//
# Assignment Operators includes =,+=,-=,*=,/=,%=,//=,**=,&=,|=,<<=,>>=,:=
# Comparison Operators includes <,>,<=,>=,==,!=
# Logical Operators includes and,or,not

# Identity Operators includes is and is not
#is 	Returns True if both variables are the same object	x is y	
#is not	Returns True if both variables are not the same object	x is not y

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference between "is" and "==": this comparison returns True because x is equal to y

# Membership Operators includes in and not in
#in 	Returns True if a sequence with the specified value is present in the object	x in y	
#not in	Returns True if a sequence with the specified value is not present in the object	x not in y
x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list


# Bitwise Operators includes &,|,<<,>>,^,~

#Operator Precedence includes (),**,+x  -x  ~x ,*  /  //  %, + - ,<<,>>,&,^,|,
# ==  !=  >  >=  <  <=  is  is not  in  not in , not and or
#If two operators have the same precedence, the expression is evaluated from left to right.
