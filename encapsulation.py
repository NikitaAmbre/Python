#Practise Question
# 1. Employee Salary Protection
# Create a class Employee:
# Private attribute: salary
# Methods:
# set_salary(amount) → validate salary > 0
# get_salary() → return salary.

class Employee:
    def __init__(self,salary):
        self.__salary=salary

    def set_salary(self,amount):
        if amount>0:
            self.__salary=amount #modify

    def get_salary(self):
        return self.__salary

e1=Employee(200000)
print(e1.get_salary())

e1.set_salary(300000)
print(e1.get_salary())


# 5. User Login System
# Create a User class:
# Private attributes: username, password
# Methods:
# set_password(new_password) (min length validation)
# check_password(input_password)

class LoginSystem:
    def __init__(self,username,password):
        self.__username=username
        self.__password=password

    def set_password(self,new_password):
        if len(new_password)>=8:
            self.__password=new_password

    def check_password(self,input_password):
        if self.__password==input_password:
            print('correct password')
        else:
            print('incorrect password')


    def get_username(self):
        return self.__username

l1=LoginSystem('Nikita23','ABc@1234')
print(l1.get_username())
print(l1.check_password('ABc@1234'))
l1.set_password('Pqr$3869')
print(l1.get_username())
print(l1.check_password('Pqr$3869'))

# 8. Hospital Patient Record System
# Create a Patient class:
# Private attributes: medical_history, diagnosis
# Methods:
# add_record(record)
# view_records(authorized_user)

class Patient:
    def __init__(self,medical_history,diagnosis):
        self.__medical_history=medical_history
        self.__diagnosis=diagnosis

    def add_record(self,record):
        self.__medical_history.append(record)
        print('record added !')

    def view_record(self,authorzed_user):
        if authorzed_user==True:
            print('medical history:',self.__medical_history)
            print('diagnosis:',self.__diagnosis)
        else:
            print('user is unauthorized')

p1 = Patient(["Fever", "Cold"], "Viral Infection")

p1.add_record("Headache")

p1.view_records(True)

print()

p1.view_records(False)
        




# 9. Inventory Management System
# Create an InventoryItem class:
# Private attributes: stock_quantity
# Methods:
# add_stock(qty)
# remove_stock(qty)
# get_stock()

class InventoryItem:
    def __init__(self, stock_quantity):
        self.__stock_quantity = stock_quantity

    def add_stock(self, qty):
        self.__stock_quantity += qty
        print("Stock added successfully.")

    def remove_stock(self, qty):
        if qty <= self.__stock_quantity:
            self.__stock_quantity -= qty
            print("Stock removed successfully.")
        else:
            print("Not enough stock available.")

    def get_stock(self):
        return self.__stock_quantity


i1 = InventoryItem(100)

print("Current stock:", i1.get_stock())

i1.add_stock(50)
print("Current stock:", i1.get_stock())

i1.remove_stock(30)
print("Current stock:", i1.get_stock())

i1.remove_stock(150)
print("Current stock:", i1.get_stock())


        



        