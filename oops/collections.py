"""
Collections in Python:
- Collections are containers that are used to store collections of data.
- Built-in collection data types: List, Tuple, Set, Dictionary.
- In OOP, we often use collections to store multiple objects of a class.
- This allows for efficient management and iteration over groups of objects.
- Collections store references to objects, meaning modifications to an object in a collection affect the original object.
- Common operations include adding, removing, sorting, and filtering objects within the collection.
"""
class Student:
    def __init__(self,age,name):
        self.names = name
        self.ages = age
    def display(self):
        print("Name:",self.names)
        print("Age:",self.ages)

s1 = Student(20,"Alice")
s2 = Student(22,"Bob")
s3 = Student(19,"Charlie")

# Creating a collection (List) of Student objects
# The list stores references to the Student instances s1, s2, and s3
stu_list = [s1,s2,s3]

for student in stu_list:
    student.display()