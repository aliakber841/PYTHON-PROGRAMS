set1={1,2,3}
set2={'a','b','c'}
set3=set1.union(set2) # set3 = set1 | set2  ..same result
print(set3)
set4 = {"apple", "bananas", "cherry"}
mySet = set1.union(set2, set3, set4) # set1 | set2 | set3 |set4
print(mySet)
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y) # join a set with tuple 
print(z) #The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.
set1.update(set2)
print(set1)
#Both union() and update() will exclude any duplicate items.
set5=set1.intersection(set2) # set1 & set2 ..same result
print(set5)
#The & operator only allows you to join sets with sets, and not with other data types
set1.intersection_update(set2)
print(set1)
#The intersection_update() method will also keep ONLY the duplicates, 
# but it will change the original set instead of returning a new set.
set6=set1.difference(set4) # set1- set4
print(set6)
#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1.difference_update(set2)
print(set1)
set10 = {"apple", "banana", "cherry"}
set20 = {"google", "microsoft", "apple"} #set1 ^ set2 .. same resukt
set30 = set10.symmetric_difference(set20) #Keep the items that are not present in both sets:
print(set30)
set10.symmetric_difference_update(set20) #will change original set
print(set10)
# my_set = {1, 2, 3, 4, 5}
# total = 0

# for num in my_set:
#     total += num

# print(total)  # Output: 15