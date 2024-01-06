course1="Python's for Beginners"
course2='Python for "Beginners" '
course3='''
Hi Ali,

Here is our first email to you.

Thank you,
The support team


'''
another=course1[:]

print(course1)
print(course2)
print(course3)
print(course1[0])
print(course2[0:3])
print(course1[1:])
print(course2[:5])
print(another)

print(len(course1))
course1.upper()
course1.lower()
print(course1.find('P'))
print(course1.replace('Beginners','Absolute Beginners'))
'Python' in course1  #gives boolean value