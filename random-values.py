import random
for i in range(3):
 print(random.random())
 print(random.randint(10,20))
 members=['John','Bob','Marry','Mosh']
 leader= random.choice(members)
 print(leader)

 dice=(random.randint(1,6),random.randint(1,6))
 print(dice)