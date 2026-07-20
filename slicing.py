# Q1) Given s = 'PythonProgramming', extract Python.
s = 'PythonProgramming'
print(s[0:6])

# Q2) Extract Programming from the same string.
print(s[6:])

# Q3) Extract the first 6 characters of s.
print(s[:7])

#Q4)Extract the last 5 characters of s.
print(s[12:])

#Q5) Extract characters from index 3 to 9.
print(s[3:10])

#Q6) Reverse the string s using slicing.

print(s[:-18:-1])
#Q7) Extract every second character from s.
print(s[0::2])

# Extract every third character from s.
print(s[::3])

# Extract the string in reverse order, skipping one character each time.
print(s[:-18:-2])

# From s = 'DataScience', extract Science using negative indexing.
s = 'DataScience'
print(s[-7:])

# Given nums = [10, 20, 30, 40, 50, 60, 70, 80], extract the first 4 elements.
nums = [10, 20, 30, 40, 50, 60, 70, 80]
print(nums[:4])

# Extract the last 3 elements.
print(nums[5:])

# Extract elements from index 2 to 5.
print(nums[2:6])

# Extract all elements except the first and last.
print(nums[1:7])

# Extract the middle 4 elements.
print(nums[2:6])

# Reverse the list using slicing.
print(nums[:-9:-1])

# Extract every alternate element.
print(nums[::2])

# Extract elements at odd indices only.
print(nums[1::2])

# Extract elements at even indices only.
print(nums[::2])

# From nums, create a new list containing elements in reverse order, skipping every second element.
print(nums[::-2])

# Given t = ('apple', 'banana', 'cherry', 'date', 'fig', 'grape'), extract the first 3 items.
t = ('apple', 'banana', 'cherry', 'date', 'fig', 'grape')
print(t[:3])

# Extract the last 2 items.
print(t[4:])

# Extract items from index 1 to 4.
print(t[1:5])

# Extract all items except banana and date using slicing and concatenation.
print(t[:1]+t[2:3]+t[4:])

# Extract ('cherry', 'date', 'fig').
print(t[2:5])

# Reverse the tuple using slicing.
print(t[:-7:-1])

# Extract every second item.
print(t[::2])

# Extract every third item starting from index 1.
print(t[1::3])

# Extract the tuple in reverse order, skipping one item each time.
print(t[::-2])

# Extract the first 4 items in reverse order.
print(t[:-5:-1])

# Given m = 'MachineLearning', extract Learning and reverse it.
m = 'MachineLearning'
print(m[7:])
print(m[:-9:-1])

# Given lst = [1,2,3,4,5,6,7,8,9,10], extract all odd numbers using slicing.
lst = [1,2,3,4,5,6,7,8,9,10]
print(lst[::2])

# Given l = (10,20,30,40,50,60,70,80), extract (80, 60, 40, 20) using slicing.
l = (10,20,30,40,50,60,70,80)
print(l[::-2])

# Given a = 'ArtificialIntelligence', extract every second character in reverse order.
a = 'ArtificialIntelligence'
print(a[:-22:-2])




