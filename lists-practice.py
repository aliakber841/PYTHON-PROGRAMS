names=['Ali','Uzair','Akber','Usama','Rajab']
print(names)
print(names[4])
print(names[2:])
print(names[2:4])
names[2]='Huzaifa'
print(names)

numbers=[45,23,81,97,63]
largest=numbers[0]
for output in numbers:
    if(largest<output):
      largest=output
print(largest)


numbers=[1,2,3,4,5,6]
numbers.append(20)
print(numbers)
numbers.insert(3,45)
print(numbers)
numbers.sort()
numbers.reverse()
numbers2=numbers.copy()
numbers.append(10)
print(numbers)
print(numbers2)
numbers.remove(2)
numbers.pop()
numbers.clear()
print(50 in numbers)
print(numbers.count(5))

numblist = [2, 3, 4, 2, 5, 7, 3]
result = []
for item in numblist:
   if item not in result:
        result.append(item)
print(result)
