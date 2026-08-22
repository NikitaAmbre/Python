# IV. Hierarchical Inheritance
# 1.School System
# Create:
# Person
# / \
# Student Teacher
# Task
# Person → name
# Student → marks
# Teacher → subject
# Print details for both subclasses.

class Person:
    def __init__(self,name):
        self.name=name

    def display_name(self):
        print(f'person name is {self.name}')

class Student(Person):
    def __init__(self, name,marks):
        super().__init__(name)
        self.marks=marks

    def display_student(self):
        super().display_name()
        print(f'student marks is {self.marks}%')

class Teacher(Person):
    def __init__(self, name,subject):
        super().__init__(name)
        self.subject=subject

    def display_teacher(self):
        super().display_name()
        print(f'subject:{self.subject}')

#student object
s=Student('Nikita',80)
s.display_student()

#teachers object 
p=Teacher('Nikita','Python')
p.display_teacher()