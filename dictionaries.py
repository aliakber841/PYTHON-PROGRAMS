customer={
    'name':'Ali',
    'age':21,
    'Email': 'aliansari9199@gmail.com',
    'is_verified': True
}
print(customer['name'])
print(customer.get("birthdate","Jan 25"))
customer['age']=20
print(customer['age'])
customer['skills']='Web Developer'
print(customer)

digits_mapping={
    '1': "One",
    '2': 'Two',
    '3':'Three',
    '4': 'Four'
}
phone= input("Phone :")
output=''
for ch in phone:
    output+= digits_mapping.get(ch,"!")+" "
print(output)