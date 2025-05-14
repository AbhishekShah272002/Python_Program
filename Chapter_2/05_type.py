# This is a simple program to demonstrate the use of type() function in Python
# The type() function is used to get the type of an object.
a = 31
t = type(a)
print(t)

b = 31.0
t = type(b)
print(t)

c = "31"
t = type(c)
print(t)

d = "Abhi"
t = type(d)
print(t)

e = "31.5"
f = float(e)# convert string to float
t = type(f)# convert string to float
print(t)