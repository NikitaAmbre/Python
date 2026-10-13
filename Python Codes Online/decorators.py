# Practice Questions on decorators:


# WAP to create a decorator which should always return positive number.
# **abs() to absorbe the negative value to give positive no's.

def positive(func):
    def inner (*a,**b):
        result=func(*a,*b)

        return abs(result)
    return inner

@positive 
def numbers(n):
    return n  
print(numbers(-50))
  

# Create a decorator to wish the employees of a company Happy Holiday.

# The message should be like this:

# Hi [Employee name],

# [Write a message]

# Thank you, HR of [Company name]

# Example: Hi Ishani, Happy Holiday,enjoy your weekend. Thank you, HR of Qspiders.


def wishes(func):
    def inner(*a,**b):
        print('hiii',a[0],',')
        print('Happy Holiday,enjoy your weekend. ')

        func(*a,*b)

        print('Thank you, HR of',a[1])
    return inner

@wishes
def A(employee_name,company_name):
    pass
A('nikita','infosys')
print()

@wishes
def A(employee_name,company_name):
    pass
A('Aanaya','QSpider')
print()


# Create a decorator that counts how many times a function has been called.

def function(func):
    count=0
    def inner(*a,**b):
        nonlocal count
        count=count+1
        print('function called', count,'times')
        func(*a,*b)
    return inner

@function
def A():
    print('hello world')
A()
A()
A()
A()


# Create a decorator that prints the function name before executing it.

def function_name(func):

    def inner(*a, **b):

        print("Function name:", func.__name__)

        func(*a, **b)

    return inner

@function_name
def A():
    print("Hello Nikita")

A()


# Create a decorator that prints "Access Granted" before executing a function.
def access(func):

    def inner(*a, **b):

        print("Access Granted")

        func(*a, **b)

    return inner

@access
def B():
    print("Welcome to the website")
B()

# Create a decorator that checks whether a number is even before executing a function.
def check_even(func):

    def inner(*a, **b):

        if a[0] % 2 == 0:
            print("Number is even")
            func(*a, **b)
        else:
            print("Number is odd")
            print("Function will not execute")

    return inner

@check_even
def C(n):
    print("Function executed")

C(10)
C(7)

# Create a decorator that measures and prints the execution time of a function.

import time
def execution_time(func):

    def inner(*a, **b):

        start_time = time.time()

        func(*a, **b)

        end_time = time.time()

        print("Execution time:", end_time - start_time, "seconds")

    return inner
@execution_time
def D():
    time.sleep(2)
    print("Function executed")
D()