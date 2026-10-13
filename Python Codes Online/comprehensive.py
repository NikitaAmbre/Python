#Practise Questions on Comphrension

#List Comprehension

# 1. Given a list of integers, create a new list containing the square of
# only odd numbers, but skip numbers divisible by 5.
l=[1,2,3,4,5,6,7,8,9,10]
a=[i**2 for i in l if i%2!=0 if i%5!=0]
print(a)

# 2. From two lists a = [1,2,3] and b = [4,5], create a list of tuples (x, y)
# such that their sum is even.
a = [1,2,3]
b = [4,5]
p=[(x,y) for x in a for y in b if (x+y)%2==0]
print(p)

# 3. Given a sentence, create a list of words that start with a vowel and
# are longer than 3 characters.

s='is your folder name is abstraction'
a=[p for p in s.split() if p[0] in 'AEIOUaeiou' and len(p)>3]
print(a)

# 4. Given a list of numbers, replace even numbers → 'even', odd
# numbers → 'odd', but if divisible by 7 → 'lucky'.

l=[1,5,6,14,34,78,21,99]
a=['lucky' if i%7==0 else 'even' if i%2==0 else'odd' for i in l]
print(a)

# 5. Flatten a nested list [[1,2,3],[4,5],[6,7,8]] and keep only numbers
# greater than 4.
n=[[1,2,3],[4,5],[6,7,8]]
a=[i for x in n for i in x if i>4]
print(a)


#Set Comprehension

# 1. From a list with duplicates, create a set of squares of numbers divisible by 3.

a={i**2 for i in range(1,11) if i%3==0 }
print(a)

# 2. Given a string, create a set of unique consonants only (ignore vowels and spaces).

s='Encapsultion And Abstraction'
a={i for i in s if i not in 'AEIOUaeiou '}
print(a)

# 3. From numbers 1 to 50, create a set of prime numbers.
a = {i for i in range(1, 51) if i > 1 and all(i % j != 0 for j in range(2, i))}
print(a)


# 4. From nested list [[2,4],[4,6],[6,8]], create a set of all even numbers greater than 4.
n = [[2, 4], [4, 6], [6, 8]]
a = {i for x in n for i in x if i % 2 == 0 and i > 4}
print(a)

# 5. From a list of words, create a set of lengths of words that contain
# the letter 'a'.

words = ['apple', 'banana', 'cat', 'dog', 'mango', 'grape']
a = {len(i) for i in words if 'a' in i}
print(a)

# #Dictionary Comprehension

# 1. Create a dictionary where key = number and value = square, only
# for numbers divisible by 4 from 1 to 20.
a = {k: k**2 for k in range(1, 21) if k % 4 == 0}
print(a)



# 2. Given a sentence, create a dictionary where key = word and value =
# length, excluding words shorter than 4 characters.

s = 'Python is a very powerful programming language'
a = {i: len(i) for i in s.split() if len(i) >= 4}
print(a)

# 3. Given a list of numbers, create a dictionary where key = number
# and value = 'even' or 'odd', skipping numbers divisible by 5.
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = {i: 'even' if i % 2 == 0 else 'odd' for i in n if i % 5 != 0}
print(a)

# 4. Given a string, create a dictionary of character frequencies (ignore spaces).
s = 'hello world'
a = {i: s.count(i) for i in set(s.replace(' ', ''))}
print(a)

# 5. Given keys = ['a','b','c','d'] and values = [10,15,20,25], create a
# dictionary including only pairs where value > 15.
keys = ['a', 'b', 'c', 'd']
values = [10, 15, 20, 25]
a = {k: v for k, v in zip(keys, values) if v > 15}
print(a)