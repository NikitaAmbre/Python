#WAP to check if a given integer is greater than 200.
s=int(input("enter a number: "))
if s>200:
    print("given integer is greater than 200")
else:
    print("given integer is not greater than 200")

# WAP to check if a given integer is multiple of 5 and divisible by 3.
a=int(input("enter a number: "))
if a%5==0 and a%3==0:
    print("number is multiple of 5 and divisible by 3")
else:
    print("number is not multiple of 5 and divisible by 3")

# WAP to check if a given integer is 2-digit number or not.
p=int(input("enter a number: "))
if 10<=p<=99:
    print("number is 2-digit number")
else:
    print("number is not 2-digit number")
 
# WAP to print the cube of the number only if the number is divisible by 7.
p=int(input("enter a number: "))
if p%7==0:
    print("cube of number is: ",p**3)
else:
    print("number is not divisible by 7")

# WAP to check if a given character is in uppercase or lowercase.
ch=input("enter a characterr: ")
if ch>='A' and ch<='Z':
    print("chsrscter is in uppercase")
else:
    print("this is not a alphabet")

#WAP to check if the given input if float or not.
num = eval(input("Enter a value: "))
if type(num)==float:
    print("It is a float.")
else:
    print("It is not a float.")

#WAP to check if the given data is SVD or MVD.
data = eval(input("Enter data: "))

if type(data) in (list, tuple, set, dict):
    print("It is MVD (Multi-Valued Data).")
else:
    print("It is SVD (Single-Valued Data).")

# WAP to check if the given number is positive or negative number.
num = int(input("Enter a value: "))
if num>0:
    print("positive number")
else:
    print("negative number")

# WAP and consider a tuple collection which consist of 2 values and check if the collection id homogeneous or heterogeneous collection.
t = eval(input("Enter a tuple with 2 values: "))

if type(t[0]) == type(t[1]):
    print("Homogeneous tuple")
else:
    print("Heterogeneous tuple")

# Write a program to check whether a number is even or odd.
num=int(input("enter number: "))
if num%2==0:
    print("number is even")
else:
    print("number is odd")

# Write a program to check whether a person is eligible to vote (age ≥ 18).
age=int(input("enter your age: "))
if age>=18:
    print("eligible for vote")
else:
    print("not eligible for vote")

# Write a program to check whether a number is divisible by 10.
num=int(input("enter a number:"))
if num%10==0:
    print("number is divisible by 10")
else:
    print("number isn't divisible by 10")

# Write a program to check whether a number is greater than 100 or not.
num=int(input("enter a number:"))
if num>100:
    print("number is greater than 100")
else:
    print("number isn't greater than 100")

# Write a program to check whether a number is a multiple of 5.
num=int(input("enter a number:"))
if num%5==0:
    print(" number is multiple of 5")
else:
    print(" number is not multiple of 5")

# Write a program to check whether a student passed or failed (pass marks ≥ 35).
marks= int(input("enter your marks"))
if marks>=35:
    print("student is pass")
else:
    print("student is fail")

# Write a program to check whether a number is less than 50.
num=int(input("enter a number:"))
if num<50:
    print("number is less than 50")
else:
    print("number is greater than 50")

# Write a program to check whether a number is zero or not zero.
num=int(input("enter a number:"))
if num==0:
    print("number is zero")
else:
    print("number is not zero")

# Write a program to check whether a number is divisible by 3.
num=int(input("enter a number:"))
if num%3==0:
    print("number is divisible by 3")
else:
    print("number is not divisible by 3")

# Write a program to check whether a character is a vowel or not.
ch=input("enter a character:")
if ch in 'AEIOUaeiou':
    print("character is vowel")
else:
    print("character is not vowel")

# Write a program to check whether a number is greater than or equal to 500.
num=int(input("enter a number:"))
if num>=500:
    print("number is greater or equal to 500")
else:
    print("number is not greater or equal to 500")

# Write a program to check whether the temperature is hot (≥30°C) or not hot.
temp=float(input("enter temperature: "))
if temp>=30:
    print("temperature is hot")
else:
    print("temperature is not hot")

# Write a program to check whether a number is divisible by 2.
num=int(input("enter a number:"))
if num%2==0:
    print("number is divisible by 2")
else:
    print("number is not divisible by 2")

# Write a program to check whether salary is greater than 20000.
salary=int(input("enter your salary: "))
if salary>20000:
    print("high salary")
else:
    print("medium salary")

# Write a program to check whether a year is 2024 or not.
year=int(input("enter current year: "))
if year==2024:
    print("year is 2024")
else:
    print("year is not 2024")

# Write a program to check whether a number is greater than 0
num=int(input("enter a number:"))
if num>0:
    print("number is greater than 0")
else:
    print("number is not greater than 0")