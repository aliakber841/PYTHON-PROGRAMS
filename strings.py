a=5
b=10
a=b
print ("a= ",a)
print ("b= ",b)


name="This is the world best python course"
print(name.title())
# title() method converts every word to capital => This Is The World Best Python Course
print(name.upper())  #all letters capital
print(name.lower())   #all letters small


car_make="BMW"
car_model="5er 2014"
car= f"{car_make} {car_model}"
my_message=f"Typhon drives a {car.upper()}"
my_bigger_message=f"{my_message} and he crashed it"
print(my_bigger_message)

# This is the f strings. f means format 

print("This is a \t Python Tab")
print("This is a \n Python Tab")
print("\t Programming Languages: \nPython\nJava\nC++\nSwift")
# \t => spacing (Tab)    
# \n=> new line

my_best_coding_languagae= " PYTHON "
print(my_best_coding_languagae)
my_best_coding_languagae=my_best_coding_languagae.lstrip()
my_best_coding_languagae=my_best_coding_languagae.rstrip()
print(my_best_coding_languagae)

#rstrip and lstrip is used to remove whitespace from right and left side of string respectively

udemy_url="https://udemy.com"
udemy_url_without_prefix=udemy_url.removeprefix('https://')
udemy_url_without_suffix=udemy_url.removesuffix(".com")
print(udemy_url_without_prefix)
print(udemy_url_without_suffix)