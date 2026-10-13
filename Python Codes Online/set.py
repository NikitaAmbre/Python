
# Set: collection datatype where we store unique values.

# it is unordered.
s={10,20,30,40,50}
print(type(s))

print(id(s))
print(s)

# no duplicate values.
e={110,120,130,140,150,130}
print(e)

# set is mutable.we can add and remove values from set using built-in functions.
s.add(70)
print(s)

s.remove(50)
print(s)

# to see all fuctions or methods of set
print(dir(set))

# set can store homogeneous and heterogeneous values.
t={10,20.3,'python',2+6j,(7,8,9,2)}
print(t)

# default value of set is set().

# indexing is not possible in set.

# Syntax: var_name={val1,val2,.....,valn}

# Functions:

# i. add(): it is used to add values/elements in a set.

# Synatx: var_name.add(value)

# ii. pop():it is used to remove elements from the front of a set collection.

# Syntax:var_name.pop()
s.pop()
print(s)

# iii. remove(): it is used to remove given elements from the set.

# Syntax: var_name.remove(value)
s.remove(10)
print(s)
