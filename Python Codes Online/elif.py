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

#     take input of user's age and check if the user is eligible for voting (age>=18) 
# as well as eligible to apply for driving license (age>=21).
age=int(input("enter your age: "))
if age>=18:
    print("eligible for vote")
elif age>=21:
    print("eligible for driving license and vote")
else:
    print("not eligible for vote and driving license")


#     take input of temperature and predict the weather. if the temperature is below 0 it's 'Freezing' ; 
# 0-15 temperature it's 'Cold' ; 16-30 temperature it's 'Warm' and above 30 temperature it's 'Hot'.
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


#     ATM Withdrawal Assume account balance = ₹20,000. Input withdrawal amount. 
# Print: Invalid amount (≤0) Insufficient balance Withdrawal successful Exact balance withdrawal
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

# Practice Questions Using elif (20 Questions)

# 1. Write a program to classify a number as positive, negative, or zero.
n=int(input('enter a number: '))
if n>0:
    print('number is positive')
elif n<0:
    print('number is negative')
else:
    print('number is zero')

# 2. Write a program to assign grades:
    # o Marks ≥ 90 → A
    # o Marks ≥ 75 → B
    # o Marks ≥ 50 → C
    # o Otherwise Fail

marks=int(input('enter your marks: '))
if marks>=90:
    print('A')
elif marks>=75:
    print('B')
elif marks>=50:
    print('C')
else:
    print('fail')

# 3. Write a program to check whether a number is:
    # o One-digit
    # o Two-digit
    # o Three-digit

num=int(input('enter a number: '))
if 1<=num<=9:
    print('one digit')
elif 10<=num<=99:
    print('two digit')
elif 100<=num<=999:
    print('three digit')
else:
    print('not a number')

# 4. Write a program to display the day type:
    # o 1–5 → Weekday
    # o 6–7 → Weekend
    # o Otherwise invalid.

day=int(input('enter day number: '))
if day>=1 and day<=5:
    print('weekday')
elif day>=6 and day<=7:
    print('weekend')
else:
    print('not a day number')

# 5. Write a program to categorize age:
    # o Child (<13)
    # o Teen (13–19)
    # o Adult (20–59)
    # o Senior (60+)
age=int(input('enter your age: '))
if age<13:
    print('child')
elif 13<=age<=19:
    print('teen')
elif 20<=age<=59:
    print('adult')
else:
    print('senior')

# 6. Write a program to check temperature:
    # o Below 10 → Cold
    # o 10–25 → Normal
    # o Above 25 → Hot
temp=int(input('enter temperature: '))
if temp<10:
    print('cold')
elif 10<=temp<=25:
    print('normal') 
else:
    print('hot')

# 7. Write a program to check exam result:
    # o ≥75 → Distinction
    # o ≥60 → First Class
    # o ≥40 → Pass
    # o Otherwise Fail
marks=int(input('enter your marks: '))
if marks>=75:
    print('distinction')
elif marks>=60:
    print('first class')
elif marks>=40:
    print('pass')
else:
    print('fail')

# 8. Write a program to check traffic signal color:
    # o Red → Stop
    # o Yellow → Wait
    # o Green → Go
ts=input('enter traffic signal: ')
if ts.lower()=='red':
    print('stop')
elif ts.lower()=='yellow':
    print('wait')
else:
    print('go')


# 9. Write a program to categorize salary:
    # o <20000 → Low
    # o 20000–50000 → Medium
    # o Above 50000 → High
sal=int(input('enter your salary: '))
if sal<20000:
    print('low salary')
elif 20000<=sal<=50000:
    print('medium salary')
else:
    print('high salary')
    
# 10. Write a program to check month number and print season.
# Program to check month number and print season

month = int(input("Enter month number (1-12): "))

if month in [12, 1, 2]:
    print("Season: Winter")
elif month in [3, 4, 5]:
    print("Season: Summer")
elif month in [6, 7, 8, 9]:
    print("Season: Monsoon")
elif month in [10, 11]:
    print("Season: Autumn")
else:
    print("Invalid month number!")

# 11. Write a program to check rating:
    # • 5 → Excellent
    # • 4 → Good
    # • 3 → Average
    # • Others → Poor
# Program to check rating

rating = int(input("Enter rating (1-5): "))

if rating == 5:
    print("Excellent")
elif rating == 4:
    print("Good")
elif rating == 3:
    print("Average")
else:
    print("Poor")


# 12. Write a program to identify character type:
    # • Digit
    # • Alphabet
    # • Special character
ch = input("Enter a character: ")

if ch.isdigit():
    print("Digit")
elif ch.isalpha():
    print("Alphabet")
else:
    print("Special character")

# 13. Write a program to check electricity units category:
    # • ≤100 → Low usage
    # • 101–300 → Medium usage
    # • Above 300 → High usage
units = int(input("Enter electricity units: "))

if units <= 100:
    print("Low usage")
elif units <= 300:
    print("Medium usage")
else:
    print("High usage")

# 14. Write a program to classify speed:
    # • <40 → Slow
    # • 40–80 → Normal
    # • 80 → Fast
speed = int(input("Enter speed: "))

if speed < 40:
    print("Slow")
elif speed <= 80:
    print("Normal")
else:
    print("Fast")

# 15. Write a program to categorize BMI value.
bmi = float(input("Enter BMI: "))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

# 16. Write a program to check score level:
    # • ≥80 → High score
    # • ≥50 → Medium score
    # • Otherwise Low score
score = int(input("Enter score: "))

if score >= 80:
    print("High score")
elif score >= 50:
    print("Medium score")
else:
    print("Low score")

# 17. Write a program to check login attempts:
    # • 1 → First attempt
    # • 2 → Second attempt
    # • 3 → Last attempt
    # • More → Blocked
attempt = int(input("Enter login attempt number: "))

if attempt == 1:
    print("First attempt")
elif attempt == 2:
    print("Second attempt")
elif attempt == 3:
    print("Last attempt")
else:
    print("Blocked")

# 18. Write a program to check ticket price category based on age.
age = int(input("Enter age: "))

if age < 5:
    print("Free Ticket")
elif age <= 12:
    print("Child Ticket")
elif age < 60:
    print("Adult Ticket")
else:
    print("Senior Citizen Ticket")

# 19. Write a program to classify rainfall level.
rainfall = float(input("Enter rainfall (in mm): "))

if rainfall < 50:
    print("Low Rainfall")
elif rainfall <= 100:
    print("Moderate Rainfall")
else:
    print("Heavy Rainfall")

# 20. Write a program to display performance level based on percentage.
percentage = float(input("Enter percentage: "))

if percentage >= 90:
    print("Excellent")
elif percentage >= 75:
    print("Very Good")
elif percentage >= 50:
    print("Good")
elif percentage >= 35:
    print("Pass")
else:
    print("Fail")



    