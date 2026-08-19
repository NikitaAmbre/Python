# Practice Questions on methods
# Q1 Create a class Student:
# object method → display details
# Class method → change school name 
# Static method → check if marks > 40 (pass/fail)

class Student:
    #class properties
    s_name='ABC INSTITUTE'
    s_time='9am-4pm'
    s_loc='Pune'

    #constructor method with object properties
    def __init__(self,name,id,phno,course,marks):
        self.name=name
        self.id=id
        self.phno=phno
        self.course=course
        self.marks=marks

    #access of object properties
    def display_details(self):
        print(self.name,self.id,self.phno,self.course,self.marks)

    #modify object properties
    def change_marks(self,new):
        self.marks=new
        print(self.marks)

    #class method to access the class property
    @classmethod
    def display(cls):
        print(cls.s_name,cls.s_time,cls.s_loc)

    #class method to modify the class property
    @classmethod
    def change_school_name(cls,new):
        cls.s_name=new
        print(cls.s_name)

    #static method
    @staticmethod
    def check_marks(self,marks):
        if marks>45:
            print('pass')
        else:
            print('fail')
# Object creation
s1=Student('Nikita',101,1234567890,'BCA',80)
s2=Student('Abhay',102,2345678910,'BCA',70)
s3=Student('Divya',103,6755894430,'MCA',35)

# print(s1.name,s1.id)

#display object properties
s1.display_details()
s2.display_details()
s3.display_details()
# change object properties    
s2.change_marks(65)
s2.display_details()

#display class method
s1.display()
s2.display()

#change class method
s3.change_school_name('SPPU University')
s3.display()

#Static Method
s2.check_marks(70)


# Q2 Create a class Bank:
# Object method → deposit/withdraw 
# Class method → change interest rate 
# Static method → calculate simple interest

class Bank:
        # 1. Class properties (Shared by ALL accounts in this bank) 
        # (Class properties are variables stored inside a class and used across all 
        # methods in that class, not just a single function)
     bank_name ='ABC Bank'
     location='Mumbai'
     interest_rate='20%'
     time='9am-6pm'
    
     def __init__(self, acc_holder,balance,phone_no,acc_no,email):   
        # 2. OBJECT PROPERTIES (Unique to each individual customer)
        self.acc_holder=acc_holder
        self.balance=balance
        self.phone_no=phone_no
        self.acc_no=acc_no
        self.email = email

    #Object method
     def deposite(self,amount):
         self.balance=self.balance+amount
         print('amount deposited:',amount)
         print('current balance is:',self.balance)

    # DISPLAY CLASS METHODS
     def display(cls):
         print(cls.bank_name,cls.location,cls.interest_rate,cls.time)

    #class method(change interest rate)
     @classmethod
     def change_rate(cls,new):
         cls.change_rate=new
         print('new interest rate:',cls.change_rate)

    # static method
     @staticmethod
     def simple_interest(principal,rate,time):
        si = (principal * rate * time) / 100
        return si
         
#object creation
c1=Bank('Nikita',10000,7684939999,1234,'nik12@gmail.com')  #class properties
c2=Bank('Ram',3000,489288388,4738,'ram12@gmail.com')
c3=Bank('Shyam',50000,2200294839,8910,'shyam23@gmail.com')
c4=Bank('Diva',56900,13049400,2347,'div34@gmail.com')
c5=Bank('Riva',93020,13948585,7629,'riva23@gmail.com')

# print(c1.acc_holder,c1.acc_no,c1.email)
# print(c2.acc_holder,c1.phone_no,c1.acc_no)
# print(c5.acc_holder,c5.email)
# print(Bank.bank_name,Bank.time,Bank.location)

#object method display deposite
c2.deposite(3000)

#display class properties
Bank.display()

#class method(change interest rate)
Bank.change_rate(30)

#static method
result = Bank.simple_interest(10000, 15, 2)
print("Simple Interest:", result)


# Q3 Create a class Product:
# Object method → calculate total price
# Class method → apply discount to all products 
# Static method → check if price is valid (>0)

class Product:

    # Class property
    discount = 10

    def __init__(self, name, price, quantity):
        # Object properties
        self.name = name
        self.price = price
        self.quantity = quantity

    # Object method
    def calculate_total_price(self):
        total = self.price * self.quantity
        return total

    # Class method
    @classmethod
    def apply_discount(cls, new_discount):
        cls.discount = new_discount
        print("Discount applied:", cls.discount, "%")

    # Static method
    @staticmethod
    def check_price(price):
        if price > 0:
            return True
        else:
            return False

# Object creation
p1 = Product('Laptop', 50000, 2)
p2 = Product('Mobile', 20000, 3)
p3 = Product('Mouse', 500, 4)

# Object method
print("Total price of p1:", p1.calculate_total_price())
print("Total price of p2:", p2.calculate_total_price())
print("Total price of p3:", p3.calculate_total_price())

# Class method
Product.apply_discount(20)

# Static method
print("Is price valid?", Product.check_price(500))
print("Is price valid?", Product.check_price(-100))



# Q4 Create a class Circle:
# Object method → calculate area 
# Class method → change default radius 
# Static method → return value of π (3.14)

class Circle:

    # Class property
    default_radius = 5

    def __init__(self, radius):
        # Object property
        self.radius = radius

    # Object method
    def calculate_area(self):
        area = 3.14 * self.radius * self.radius
        return area

    # Class method
    @classmethod
    def change_default_radius(cls, new_radius):
        cls.default_radius = new_radius
        print("New default radius:", cls.default_radius)

    # Static method
    @staticmethod
    def get_pi():
        return 3.14

# Object creation
c1 = Circle(5)
c2 = Circle(10)
c3 = Circle(7)

# Object method
print("Area of c1:", c1.calculate_area())
print("Area of c2:", c2.calculate_area())
print("Area of c3:", c3.calculate_area())

# Class method
Circle.change_default_radius(10)

# Static method
print("Value of PI:", Circle.get_pi())