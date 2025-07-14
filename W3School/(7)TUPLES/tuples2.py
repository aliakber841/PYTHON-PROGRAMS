x=('apple','banana','mango')
y=list(x)
y[1]='kiwi'
x=tuple(y)
print(x)
y.append('orange')
x=tuple(y)
print(x)
z=('guava',)
x+=z
print(x)
y.remove('mango')
x=tuple(y)
print(x)
del x
