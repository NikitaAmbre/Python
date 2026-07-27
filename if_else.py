# WAP to check if a given integer is greater than 200.
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

# WAP to check if the given data is SVD or MVD.
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