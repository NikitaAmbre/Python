# Practise Question on elif statement

#     WAP to find the smallest value among 4 given integer numbers.
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))
if a < b and a < c and a < d:
    print(f"{a} is the smallest")
elif b < a and b < c and b < d:
    print(f"{b} is the smallest")
elif c < a and c < b and c < d:
    print(f"{c} is the smallest")
elif d < a and d < b and d < c:
    print(f"{d} is the smallest")
else:
    print("Two or more numbers are equal or all numbers are the same.")
    
#     predict the status of the student result based on the obtained percentage.
percentage=float(input("enter your percentage: "))
if percentage>75:
    print("first class with distinction")
elif percentage>60 and percentage<75:
    print("first class")
elif percentage>=35:
    print("studnt is pass")
else:
    print("student is fail")

#     consider 2 coordinates i.e. x and y and check in which quadrant the point lies.
# WAP to check in which quadrant the point lies

x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))
if x > 0 and y > 0:
    print("The point lies in First Quadrant.")
elif x < 0 and y > 0:
    print("The point lies in Second Quadrant.")
elif x < 0 and y < 0:
    print("The point lies in Third Quadrant.")
elif x > 0 and y < 0:
    print("The point lies in Fourth Quadrant.")
elif x == 0 and y == 0:
    print("The point lies at the Origin.")
elif x == 0:
    print("The point lies on the Y-axis.")
else:
    print("The point lies on the X-axis.")

#     take input of user's age and check if the user is eligible for voting (age>=18) as well as eligible to apply for driving license (age>=21).
age=int(input("enter your age: "))
if age>=18:
    print("eligible for vote")
elif age>=21:
    print("eligible for driving license and vote")
else:
    print("not eligible for vote and driving license")


#     take input of temperature and predict the weather. if the temperature is below 0 it's 'Freezing' ; 0-15 temperature it's 'Cold' ; 16-30 temperature it's 'Warm' and above 30 temperature it's 'Hot'.
temp=int(input("enter temperature: "))
if temp<0:
    print("freezing")
elif temp<=15:
    print("cold")
elif temp>=16 and temp<=30:
    print("warm")
else:
    print("hot")

#     Movie Ticket Price Input age. Print ticket price: Below 5 → Free 5–12 → ₹100 13–59 → ₹250 60 and above → ₹150
age=int(input("enter your age: "))
if age<5:
    print("free ticket")
elif age>=5 and age<=12:
    print("ticket price is rs 100")
elif age>=13 and age<=59:
    print("ticket price is rs 250")
else:
    print("ticket price is rs 150")

#     Login System
# Assume:
# username = "admin" password = "python123"
# Input username and password. Print: Login Successful Incorrect Password Username Not Found
username = "admin" 
password = "python123"
u=input("enter username: ")
p=input("enter password: ")
if username==u and password==p:
    print("login successful")
elif username==u and password!=p:
    print("incorrect password")
elif username!=u and password==p:
    print("incorrect username")
else:
    print("user not found")


#     ATM Withdrawal Assume account balance = ₹20,000. Input withdrawal amount. Print: Invalid amount (≤0) Insufficient balance Withdrawal successful Exact balance withdrawal
# ATM Withdrawal

balance = 20000
amt = int(input("Enter withdrawal amount: "))
if amt <= 0:
    print("Invalid amount")
elif amt > balance:
    print("Insufficient balance")
elif amt == balance:
    print("Exact balance withdrawal")
    print("Remaining balance:", balance - amt)
else:
    print("Withdrawal successful")
    print("Remaining balance:", balance - amt)

#     Triangle Type Input three sides. Print: Equilateral Isosceles Scalene Not a valid triangle
# Input three sides of a triangle
# WAP to check the type of triangle

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
if a + b <= c or a + c <= b or b + c <= a:
    print("Not a valid triangle")
elif a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

#     Character Type
# Input a single character. Print whether it is: Uppercase letter Lowercase letter Digit Special character
# WAP to check character type

ch = input("Enter a character: ")
if 'A' <= ch <= 'Z':
    print("Uppercase Letter")
elif 'a' <= ch <= 'z':
    print("Lowercase Letter")
elif '0' <= ch <= '9':
    print("Digit")
else:
    print("Special Character")