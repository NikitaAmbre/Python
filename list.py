l=[1,2,3,4,5,6,7,8,9,10]
print(l)

print(type(l))

print(len(l))

print(id(l))

print(l[3])

print(l[5]==12)

l[5]=90
print(l)

l.append(1234)
print(l)

l.extend([23,45,67,890])
print(l)

l.insert(8,100)
print(l)

l.pop()
print(l)

l.remove(45)
print(l)



# List: it is used to store multiple elements in a single variable using square brackets [].

# Syntax: var_name=[val1,val2,.....valn]

# list is mutable datatype, which means we can add,delete or replace values.

# list is ordered.

# list stores duplicate values.

# list elements can be accessed directly using indexing.

# list stores both homogeneous and heterogeneous values.

# homogeneous : same datatypes

# hetrogenous: diff. datatypes

# add to elements:

#     append(): used to add one value at a time at the end the list.

# Syntax: var_name.append(value)

#     extend(): used to add multiple values at the end of the list at a go.

# Syntax: var_name.extend([values])

#     insert(): add value in a given index position.

# Syntax: var_name.insert(index_position,value)
# remove elements:

#     pop(): remove values from a list collection either from the given index or from the end the list.

# Syntax: var_name.pop(): remove the last element

# var.pop(index_position): remove the given index positioned value.

#     remove(): used to delete one element at a time from a list,the given element is removed.

# Syntax: var_name.remove(value)