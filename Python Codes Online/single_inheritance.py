# #Code example:

class Student:  #parent class
  def __init__(self,name,addrs,dob):
    self.name=name
    self.addrs=addrs
    self.dob=dob

  def display(self):  #object method to access
    print(f'Name: {self.name}, Address: {self.addrs}, Date of Birth: {self.dob}')

class School(Student):  #child class
  def __init__(self,name,addrs,dob,s_name,marks):
    super().__init__(name,addrs,dob) #constructor chaining
    self.s_name=s_name
    self.marks=marks
  def display_details(self):
    super().display() #method chaining
    print(f'School name: {self.s_name}, Percentage: {self.marks}')


#object creation

st1=School('Sneha','Kolkata','25-03-2000','SXI','88%')

# st1.display()
# print()
st1.display_details()



# Single Level Inheritance
# 1.Online Shopping User
# Create:
# User class → name, email
# Customer class → inherits from User and adds cart_items
# Task

class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email

    def display(self):
        print(f'user name : {self.name}, user email: {self.email}')

class Customer(User):
    def __init__(self,name,email,cart_items):
        super().__init__(name,email)    #constructor chaining
        self.cart_items=cart_items

    def disp(self):
        super().display()   #method chaining
        print(f'cart: {self.cart_items}')

cust=Customer('radha','radha123@gmail.com','bag')

cust.display()
print()
cust.disp()


# 2.Banking System (Interview Favorite)
# Create:
# Account → account_number, balance, method deposit()
# SavingsAccount → adds interest_rate and method apply_interest()
# Requirements:
# Use constructor chaining with super().Show balance before and after interest

class Account:
    def __init__(self,ac_no,balance):
        self.ac_no=ac_no
        self.balance=balance

    def deposite(self):
        print(f'your account number{self.ac_no} and balance {self.balance}')

class SavingsAccount(Account):
    def __init__(self,ac_no,balance,interest_rate):
        super().__init__(ac_no,balance)
        self.interest_rate=interest_rate

    def apply_interest(self):
        super().deposite()
        print(f'interest rate is :{self.interest_rate}')

ob1=SavingsAccount('AC223456',300000,'12%')

ob1.deposite()
print()
ob1.apply_interest()
        


