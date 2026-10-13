# we can store duplicate values.

e=(1,2,3,4,5,2,4,5)
print(e)
# we store the values in tuple in single brackets.

# Syntax: var_name=(val1,val2,...,valn)

# or

# var_name=val1,val2,...valn

# the elements in tuple are ordered.

# default value of tuple (); which is internally False.

t=(1,2,3,4,5)
print(type(t))

print(len(t))

u=100,200,300
print(type(u))

p=160,
print(type(p))

print(t[0])

# tuple is immutable 
# t[2]=13
# print(t)
# Traceback (most recent call last):
#   File "c:\Users\Admin\Documents\python series\tuple.py", line 32, in <module>
#     t[2]=13
#     ~^^^
# TypeError: 'tuple' object does not support item assignment

t=(12,4.5,'nikita',2+9j,[3,4,5])
print(t)     #tuple: collection datatype, which is used to store homogeneous and heterogeneous values.