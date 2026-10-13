# #Practice Questions on nested if

# 1.ATM Withdrawal
# A user has:
# Account balance = ₹20,000 Correct PIN = 1234
# Take PIN and withdrawal amount as input.
# Conditions:
# First verify the PIN. If the PIN is correct, check whether the withdrawal amount is less than or equal to the balance. 
# If yes, deduct the amount and display the remaining balance. Otherwise, print "Insufficient Balance".

p=int(input('enter a pin: '))
amt=int(input('enter withdrawal amount: '))

if p==1234:
    if amt<=20000:
        print('remaining balance: ',20000-amt)
    else:
        print('insufficient balance')
else:
    print('pin is incorrect')

#     Scholarship Eligibility
# Take the following inputs:
# Percentage and Family income
# Conditions:
# If percentage is 80 or above, then: If family income is less than ₹3,00,000, print "Full Scholarship". Otherwise, print "Half Scholarship".
# If percentage is below 80, print "Not Eligible".

p=float(input('enter your percentage: '))
f=int(input('enter family income: '))

if p>=80:
    if f<300000:
        print('Full Scholarship')
    else:
        print('Half Scholarship')
else:
    print('Not Eligible')


#     Movie Ticket Booking
# Take:
# Age, Ticket availability (yes or no)
# Conditions:
# If tickets are available: If age is 18 or above, print "Adult Ticket Booked". Otherwise, print "Child Ticket Booked". 
# If tickets are unavailable, print "House Full".

age=int(input('enter your age: '))
t=input('ticket availability(yes/no): ')

if t.lower()=='yes':
    if age>=18:
        print('Adult Ticket Booked')
    else:
        print('Child Ticket Booked')
else:
    print('House Full')


#     Laptop Purchase
# Take:
# Budget, Is student? (yes or no)
# Conditions:
# If budget is ₹50,000 or more: If the user is a student, apply a 10% discount and display the final price. Otherwise, display the original price. 
# If budget is below ₹50,000, print "Increase Your Budget".

b=int(input('enter your budget: '))
s=input(' are you student?(yes/no): ')

if b>=50000:
    if s.lower()=='yes':
        print('10% discount is applied. final price is',b-b*10/100)
    else:
        print('original price is: ',b)
else:
    print('increase your budget')


#     Loan Approval
# Take:
# Monthly salary, Credit score
# Conditions:
# If salary is ₹40,000 or above: If credit score is 750 or above, print "Loan Approved". Otherwise, print "Loan Rejected due to Low Credit Score". 
# If salary is below ₹40,000, print "Loan Rejected due to Low Salary".

ms=int(input('enter your monthly salary: '))
cs=int(input('enter your credit score: '))

if ms>=40000:
    if cs>=750:
        print('loan approved')
    else:
        print('loan rejected due to low credit score')
else:
    print('loan rejected due to low salary')

    
#     Train Reservation
# Take:
# Seat availability (yes/no), Passenger age, Is senior citizen (yes/no)
# Conditions:
# If seats are available: If age is 60 or above: If senior citizen is yes, give a 40% discount. Otherwise, give a normal ticket.
#  Otherwise, book a normal ticket. Otherwise, print "Waiting List."

sa = input("Seat available? (yes/no): ")
p_age = int(input("Enter your age: "))
sc = input("Are you a senior citizen? (yes/no): ")

if sa.lower() == "yes":
    if p_age >= 60:
        if sc.lower() == "yes":
            print("40% discount applied")
        else:
            print("Normal Ticket Booked")
    else:
        print("Normal Ticket Booked")
else:
    print("Waiting List")


## Practice Questions Using Nested if (20 Questions)

# 1. Check if a number is positive, and if yes check whether it is even or odd.
num=int(input('enetr number: '))
if num>0:
    if num%2==0:
        print('number is even')
    else:
        print('number is odd')
else:
    print('number is negative')

# 2. Check if a student passed, and if passed check whether marks are above 75.
m=int(input('enter your marks: '))
if m>35:
    if m>75:
        print('student is passed with distinction')
    else:
        print('student got average marks')
else:
    print('student is fail')

# 3. Check if a number is divisible by 2, then check if it is also divisible by 4.
num=int(input('enter number: '))
if num%2==0:
    if num%4==0:
        print('number is divisible by 2 and 4 ')
    else:
        print('number is not divisible by 4')
else:
    print('number is not divisible by 2')

# 4. Check if age ≥18, then check if the person has a driving license.
age=int(input('enter your age: '))
if age>=18:
    license=input('do you have license:')
    
    if license.lower()=='yes':
        print('eligible for drive')
    else:
        print('not eligible for driving')
else:
    print('you are under 18')

# 5. Check if username is correct, then check if password is correct.
uname=input('enter username:')
pwd=input('enter password:')
if uname=='Python':
    if pwd=='Abc@123':
        print('log in successful')
    else:
        print('invalid password')
else:
    print('wrong username')

# 6. Check if temperature is high, then check if humidity is also high.
temp = int(input("Enter temperature: "))
humidity = int(input("Enter humidity (%): "))

if temp > 35:
    print("Temperature is high.")

    if humidity > 70:
        print("Humidity is also high.")
    else:
        print("Humidity is not high.")
else:
    print("Temperature is not high.")

# 7. Check if a number is greater than 100, then check if it is less than 500.
num = int(input("Enter a number: "))

if num > 100:
    if num < 500:
        print("The number is greater than 100 and less than 500.")
    else:
        print("The number is greater than or equal to 500.")
else:
    print("The number is 100 or less.")

# 8. Check if a character is an alphabet, then check if it is a vowel.
ch = input("Enter a character: ")

if ch.isalpha():
    if ch.lower() in "aeiou":
        print("It is a vowel.")
    else:
        print("It is a consonant.")
else:
    print("It is not an alphabet.")

# 9. Check if salary > 30000, then check if experience > 5 years.
salary = int(input("Enter salary: "))
experience = int(input("Enter experience (years): "))

if salary > 30000:
    if experience > 5:
        print("Eligible.")
    else:
        print("Not enough experience.")
else:
    print("Salary is not greater than 30000.")

# 10. Check if a year is divisible by 4, then check leap year condition.
year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print("Leap Year")
    else:
        print("Not a Leap Year")
else:
    print("Not a Leap Year")

# 11. Check if marks ≥40, then check if marks ≥80 for distinction.
marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
    if marks >= 80:
        print("Distinction")
else:
    print("Fail")

# 12. Check if a number is positive, then check if it is a multiple of 5.
num = int(input("Enter a number: "))

if num > 0:
    if num % 5 == 0:
        print("Positive and multiple of 5")
    else:
        print("Positive but not a multiple of 5")
else:
    print("Number is not positive")

# 13. Check if a person is logged in, then check admin access.
login = input("Are you logged in? (yes/no): ")

if login.lower() == "yes":
    admin = input("Are you an admin? (yes/no): ")

    if admin.lower() == "yes":
        print("Admin Access Granted")
    else:
        print("User Access Granted")
else:
    print("Please log in first")

# 14. Check if electricity units exceed 100, then apply extra charge.
units = int(input("Enter electricity units: "))

if units > 100:
    print("Extra charge applied")
else:
    print("No extra charge")

# 15. Check if purchase amount ≥1000, then check membership status for extra discount.
amount = int(input("Enter purchase amount: "))
member = input("Are you a member? (yes/no): ")

if amount >= 1000:
    if member.lower() == "yes":
        print("Extra discount applied")
    else:
        print("No extra discount")
else:
    print("Purchase amount is less than 1000")

# 16. Check if a number is even, then check if it is greater than 50.
num = int(input("Enter a number: "))

if num % 2 == 0:
    if num > 50:
        print("Even and greater than 50")
    else:
        print("Even but not greater than 50")
else:
    print("Odd number")

# 17. Check if a student attended exam, then check passing marks.
attended = input("Did the student attend the exam? (yes/no): ")

if attended.lower() == "yes":
    marks = int(input("Enter marks: "))

    if marks >= 40:
        print("Passed")
    else:
        print("Failed")
else:
    print("Student did not attend the exam")

# 18. Check if internet is connected, then check signal strength.
internet = input("Is internet connected? (yes/no): ")

if internet.lower() == "yes":
    signal = int(input("Enter signal strength (1-5): "))

    if signal >= 3:
        print("Good Signal")
    else:
        print("Weak Signal")
else:
    print("No Internet Connection")

# 19. Check if balance is sufficient, then allow withdrawal amount.
balance = int(input("Enter account balance: "))
withdraw = int(input("Enter withdrawal amount: "))

if balance >= withdraw:
    print("Sufficient balance")

    if withdraw > 0:
        print("Withdrawal Successful")
else:
    print("Insufficient balance")

# 20. Check if input is a digit, then check whether it is greater than 5.
value = input("Enter a value: ")

if value.isdigit():
    num = int(value)

    if num > 5:
        print("Digit is greater than 5")
    else:
        print("Digit is 5 or less")
else:
    print("Input is not a digit")