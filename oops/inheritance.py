"""
Inheritance
- It is a mechanism where a new class inherits properties and behaviors (methods and attributes) from an existing class.
- It represents an "Is-A" relationship (e.g., Student is a User).
- Parent Class (Base/Super Class): The class being inherited from.
- Child Class (Derived/Sub Class): The class that inherits.
- Benefits: Code Reusability and cleaner code structure.
- In this example: 'User' is the parent class; 'Tutor' and 'Student' are child classes.
"""
class User:
    def __init__(self, name=None, age=None):
        self.name = name if name is not None else "Default User"
        self.age = age if age is not None else 18
    
    def login(self):
        return f"{self.name} has logged in."
    
    def logout(self):
        return f"{self.name} has logged out."
    
    def signup(self):
        return f"{self.name} has signed up."
    
class Tutor(User):
    def upload_course(self, course_name):
        return f"{self.name} has uploaded the course: {course_name}."
    def delete_course(self, course_name):
        return f"{self.name} has deleted the course: {course_name}."

class Student(User):
    def enroll_course(self, course_name):
        return f"{self.name} has enrolled in the course: {course_name}."
    
    def submit_assignment(self, assignment_name):
        return f"{self.name} has submitted the assignment: {assignment_name}."

if __name__ == "__main__":
    tutor = Tutor(name="Alice", age=30)
    student = Student(name="Bob", age=20)
    
    print(tutor.signup())
    print(tutor.upload_course("Python Programming"))
    print(student.signup())
    print(student.enroll_course("Python Programming"))