def greet_typhon():
    print("Hello Students")

greet_typhon()
greet_typhon()
       
       # SINGLE ARGUMENT

def username(name):
    print(f"Hello my student {name.upper()} !")
username("Ali")

   # MULTIPLE ARGUMENTS

def display_course(course_topic="Online Course",course_name="Unknown",course_hours=0):
    """ Display Information about course """
    print(f"\n Course Topic : {course_topic} ")
    print(f" Course Name : {course_name} ")
    print(f" Course Hours : {course_hours} Hours")
display_course("Python" ,"Learn Python Fast and Hard way by Nikhat",3)
display_course("R Programming" ,"R Programming Masterclass by Nikhat",3)

  # DEFAULT VALUES
display_course(course_hours=3,course_topic="Python", course_name="Learn Python Fast and Hard way by Nikhat",)
display_course(course_name="Java Course")

   #RETURNING VARIABLES FROM FUNCTIONS

def get_car_info(car_maker,car_model,car_year):
    """  Return a full car info """
    car_info= f"{car_maker.upper()} {car_model.title()} {car_year}"
    return car_info

bmw=get_car_info("BMW","528i",2016)
myvolvo= get_car_info("Volvo","S40",2008)
vw_car=get_car_info("VW","Golf 7",2014)
print(bmw)
print(f"My Volvo is best {myvolvo}")
print(f"VW is best {vw_car}")