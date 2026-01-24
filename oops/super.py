"""
super() Function
- It is a built-in function that allows a subclass to call methods from its parent class.
- It returns a temporary object of the superclass that allows access to all of its methods.
- Key Benefits:
  1. Accessing Parent Methods: Useful when a method is overridden in the child class but you still want to use the parent's implementation.
  2. Constructor Chaining: Commonly used in __init__ to ensure the parent class is initialized properly.
  3. Multiple Inheritance: Handles the Method Resolution Order (MRO) automatically.
  4. Maintainability: Decouples the child class from the specific name of the parent class.
- In this example:
  - super().__init__() calls the Parent's constructor.
  - super().show() calls the Parent's show method.
"""
class Parent:
    def __init__(self):
        self.num = 100
    
    def show(self):
        return f"Parent num: {self.num}"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.val = 200
    
    def show(self):
        parent_info = super().show()
        return f"{parent_info}, Child val: {self.val}"
    
if __name__ == "__main__":
    child_instance = Child()
    print(child_instance.show())