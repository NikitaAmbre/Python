# # 1. Function WITHOUT arguments & WITHOUT return value
# Write a function to print "Hello, World!".
def print_hello():
    print("hello world")
print_hello()

# Write a function to print numbers from 1 to 10.
def print_num():
    for i in range(1,11):
        print(i)
print_num()

# Write a function to print the multiplication table of 5.
def print_table():
    for i in range(1,11):
        print(f"5 * {i} = {5*i}")
print_table()

# Write a function to print all even numbers from 1 to 20.
def print_even():
    for i in range(1,21):
        if i%2==0:
            print(f"{i} is even")
print_even()

# write a function to print your name 5 times.
def print_name():
    for i in range(5):
        print("Nikita")
print_name()

# # 2. Function WITH arguments & WITHOUT return value
# Write a function that takes a number and prints its square.
def check_square(num):
    print(f"square of {num} is {num*num}")
check_square(5)

# Write a function that takes a number and prints whether it is even or odd.
def check_number(num):
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
check_number(int(input("Enter number: ")))

# Write a function that takes two numbers and prints their sum.
def print_sum(num1,num2):
    print(f"sum of {num1} and {num2} is {num1+num2}")
print_sum(int(input("Enter first number: ")),int(input("Enter second number: ")))

# Write a function that takes a number and prints its multiplication table.
def print_multiplication(num):
    for i in range(1,11):
        print(f"{num}*{i}={num*i}")
print_multiplication(int(input("Enter number: ")))

# Write a function that takes a string and prints it in uppercase.
def print_uppercase(string):
    print(string.upper())
print_uppercase(input("Enter string: "))

# # 3. Function WITHOUT arguments & WITH return value
# Write a function that returns the number 100.
def print_num():
    return 100
print(print_num())

# Write a function that returns the sum of numbers from 1 to 10.
def print_sum():
    sum = 0
    for i in range(1,11):
        sum += i
    return sum
print(print_sum())

# Write a function that returns a list of first 5 even numbers.
def list_even():
    even=[]
    for i in range(1,11):
        if i%2==0:
            even.append(i)
    return even
print(list_even())

# Write a function that returns the square of 7.
def f_square():
    return 7*7
print(f_square())

# Write a function that returns the length of a fixed string ("Python").
def f_length():
    return len("Python")
print(f_length())

# # 4. Function WITH arguments & WITH return value
# Write a function that takes a number and returns its square.
def f_square(num):
    return num*num
print(f_square(int(input("Enter number: "))))

# Write a function that takes two numbers and returns their sum.
def f_sum(x,y):
    return x+y
print(f_sum(int(input("Enter first number: ")),int(input("Enter second number: "))))

# Write a function that takes a number and returns True if even, False if odd.
def f_check(num):
    if int(num)%2==0:
        return True
    else:
        return False
print(f_check(int(input("Enter number: "))))

# Write a function that takes a string and returns it reversed.
def f_string(s):
    return s[::-1]
print(f_string(input("Enter string: ")))

# Write a function that takes a number and returns its factorial.
def f_fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(f_fact(int(input("Enter number: "))))