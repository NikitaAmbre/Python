# Create a class called Bank and object will be cusomer. 
# Take atleast 4 class properties and atleast 5 object properties. 
# print the object properties as per your own wish.

class Bank:
        # 1. Class properties (Shared by ALL accounts in this bank) 
        # (Class properties are variables stored inside a class and used across all 
        # methods in that class, not just a single function)
     bank_name ='ABC Bank'
     location='Mumbai'
     website='www.ABCBank.com'
     time='9am-6pm'
    
     def __init__(self, acc_holder,balance,phone_no,acc_no,email):   
        # 2. OBJECT PROPERTIES (Unique to each individual customer)
        self.acc_holder=acc_holder
        self.balance=balance
        self.phone_no=phone_no
        self.acc_no=acc_no
        self.email = email

#object creation
c1=Bank('Nikita',10000,7684939999,1234,'nik12@gmail.com')  #class properties
c2=Bank('Ram',3000,489288388,4738,'ram12@gmail.com')
c3=Bank('Shyam',50000,2200294839,8910,'shyam23@gmail.com')
c4=Bank('Diva',56900,13049400,2347,'div34@gmail.com')
c5=Bank('Riva',93020,13948585,7629,'riva23@gmail.com')

print(c1.acc_holder,c1.acc_no,c1.email)
print(c2.acc_holder,c1.phone_no,c1.acc_no)
print(c5.acc_holder,c5.email)
print(Bank.bank_name,Bank.time,Bank.location)