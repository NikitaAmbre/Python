# Practice Questions on lambda, map(), filter()

# 1. Lambda function that accepts a string and returns its
#    last character.

a = lambda n: n[-1]
print("1.", a('python'))


# 2. Lambda function that accepts an employee's salary and
#    calculates a 15% bonus.

a = lambda salary: salary * 15 / 100
print("2.", a(20000))


# 3. Lambda function that checks whether a given string is
#    a palindrome.

a = lambda n: n == n[::-1]
print("3.", a('madam'))


# 4. Lambda function that accepts length and width and
#    returns the area of the rectangle.

a = lambda length, width: length * width
print("4.", a(10, 5))



# 5. Lambda function that accepts an email address and
#    returns only the domain.

a = lambda email: email.split('@')[1]
print("5.", a('nikita@gmail.com'))



# 6. Given a list of words, use map() and lambda to create
#    a list containing the length of each word.


words = ['python', 'java', 'sql', 'numpy']

result = list(map(lambda word: len(word), words))

print("6.", result)


 
# 7. Given a list of distances in kilometers, use map() and
#    lambda to convert every value into miles.
 

km = [10, 20, 30, 40]

miles = list(map(lambda x: x * 0.621371, km))

print("7.", miles)



# 8. Given a list containing full names, use map() and
#    lambda to extract only the first name.


names = ['Nikita Ambre', 'Rahul Patil', 'Amit Sharma']

first_names = list(map(lambda name: name.split()[0], names))

print("8.", first_names)



# 9. Given a list of birth years, use map() and lambda to
#    calculate the age of each person.
 

birth_years = [2000, 2002, 2005, 1998]

ages = list(map(lambda year: 2026 - year, birth_years))

print("9.", ages)


# 10. A student has marks out of 500. Given a list of total
#     marks obtained, use map() and lambda to calculate
#     the percentage.
# 

marks = [400, 350, 450, 275]

percentage = list(map(lambda x: (x / 500) * 100, marks))

print("10.", percentage)


# 11. Given a list of words, use filter() and lambda to
#     extract words whose length is greater than 5.


words = ['python', 'java', 'computer', 'sql', 'database']

result = list(filter(lambda word: len(word) > 5, words))

print("11.", result)


# 12. Use filter() and lambda to extract numbers that are divisible by both 3 and 5.

numbers = [10, 15, 20, 30, 45, 50, 60, 75]

result = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))

print("12.", result)


# 13. Given a list of email addresses, use filter() and lambda to extract only Gmail addresses.


emails = [
    'nikita@gmail.com',
    'abc@yahoo.com',
    'rahul@gmail.com',
    'xyz@outlook.com'
]

result = list(filter(lambda email: email.endswith('@gmail.com'), emails))
print("13.", result)


# 14. Given employee performance scores, extract employees whose score is 80 or above.
scores = [75, 90, 65, 80, 85, 70]
result = list(filter(lambda x: x >= 80, scores))
print("14.", result)


# 15. Given a list of passwords, use filter() and lambda to select passwords having at least 8 characters.
passwords = ['abc123', 'python123', 'hello', 'admin@123', 'pass']
result = list(filter(lambda password: len(password) >= 8, passwords))
print("15.", result)