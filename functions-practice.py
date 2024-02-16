def greet_user(first_name,last_name):
    print(f'Hi {first_name} {last_name}')
    print("Welcome abroad")


print("Start")
greet_user("Ali","Akber")
# greet_user(first_name= "Ali",last_name="Akber") 
 #keyword arguments. Helps to improve the  readability of the code
print("Finish")

def square(number):
    return number*number
result= square(3)
print(result)


def emojiconverter(message):
    words=message.split(' ')
    emojis={
        ":)" : "😊",
        ":(" :"😢",
    }
    output=""
    for word in words:
         output+= emojis.get(word,word)+" "
    return output


message= input(">")
result= emojiconverter(message)
print(result)