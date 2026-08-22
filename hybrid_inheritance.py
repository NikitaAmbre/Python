# 2. University Portal (Diamond Structure)
# Create:
#          Person
#         /      \
#     Student   Teacher
#         \      /
#      TeachingAssistant
#
# Requirements:
# Use super() in constructors
# Ensure attributes from Person are not initialized twice


class Person:
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name

    def display_name(self):
        print(f'Person name is {self.name}')


class Student(Person):
    def __init__(self, name, marks, **kwargs):
        super().__init__(name=name, **kwargs)
        self.marks = marks

    def display_student(self):
        print(f'Student marks is {self.marks}%')


class Teacher(Person):
    def __init__(self, subject, **kwargs):
        super().__init__(**kwargs)
        self.subject = subject

    def display_teacher(self):
        print(f'Teacher subject is {self.subject}')


class TeachingAssistant(Student, Teacher):
    def __init__(self, name, marks, subject, assistant_email):
        super().__init__(
            name=name,
            marks=marks,
            subject=subject
        )
        self.assistant_email = assistant_email

    def display_all(self):
        self.display_name()
        self.display_student()
        self.display_teacher()
        print(f'Assistant email is: {self.assistant_email}')


# TeachingAssistant object
t = TeachingAssistant(
    'Aananya',
    60,
    'English',
    'aananya123@gmail.com'
)

t.display_all()