# II. Multilevel Inheritance
# 1.Employee Hierarchy
# Create a chain:
# Employee → Developer → BackendDeveloper
# Task
# Employee → name
# Developer → programming_language
# BackendDeveloper → framework
# Display all details from child class.

class Employee:
    def __init__(self,name):
        self.name=name

    def display_emp(self):
        print(f'name of emp: {self.name}')

class Developer(Employee):
    def __init__(self, name,programming_language):
        super().__init__(name)
        self.programming_language=programming_language

    def display_dev(self):
        super().display_emp()
        print(f'programming_language is:{self.programming_language}')

class BackendDeveloper(Developer):
    def __init__(self, name,programming_language,framework):
        super().__init__(name,programming_language)
        self.framework=framework

    def display_bd(self):
        super().display_dev()
        print(f'framework is: {self.framework}')

p1=BackendDeveloper('Rahul','Java','React')

p1.display_emp()
print()
p1.display_dev()
print()
p1.display_bd()