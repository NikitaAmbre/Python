#copy operations
#  It is a process of copying the content from one varible to another keeping the original content intact.
n=[12,23,34,56]
m=n
print(n)
print(m)
print(id(n))
print(id(m))
m[3]=67
print(m)
print(n)

#  There are 2 types:
    #  General/Normal copy
        #Shallow copy
p=[9,8,7,6,5]
q=p.copy()
print(p)
print(q)
print(id(p))
print(id(q))
q[2]=89
print(q)
print(p)

         #Deep copy

k=[4,3,6,7,2,[2,7,88,90]]
import copy
l=copy.deepcopy(k)
print(k)

print(type(k))
print(id(k))
print(l)
print(id(l))

l[4]=567
print(l)
print(k)

print(l[5])

#  General/Normal Copy
 # The content of the variable will be copied in the same memory location.
 # Shallow Copy

 # The content of the variable is copied in different memory location.

 # Syntax:

 # import copy copy.copy(source_var)

 # or

# dest_var=source_var.copy()

# In nested collection when shallow copy is done the nested values gets copied in the same memory location which when modified can effect the original collection
# Deep Copy

# It copies the content of the original variable into another variable but in different memory location, even if it is a nested collection.

# Syntax:

# import copy dest_var=copy.deepcopy(source_var)