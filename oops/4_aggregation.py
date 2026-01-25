"""
Aggregation
- It is a "Has-A" relationship between classes.
- One class contains a reference to an object of another class.
- Unlike Composition (where the contained object is destroyed when the owner is destroyed), 
  in Aggregation, the contained object can exist independently.
- In this example: Customer has an Address. The Address object is passed to the Customer.
"""
class Customer:
    def __init__(self,name,age,address):
        self.name = name 
        self.age = age
        self.address = address
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
        print("Address Details:")
        print(f"City: {self.address.city}")
        print(f"State: {self.address.state}")
        print(f"Pin Code: {self.address.pincode}")

    def edit_profile(self, new_city, new_state, new_pincode, new_name=None):
        if new_name is not None:
            self.name = new_name
        self.address.change_address(new_city,new_state,new_pincode)
        

class Address:
    def __init__(self,city,state,pincode):
        self.city = city
        self.state = state
        self.pincode = pincode

    def change_address(self,new_city,new_state,new_pincode):
        self.city = new_city
        self.state = new_state
        self.pincode = new_pincode


c1 = Customer("John", 30, Address("New York", "NY", "10001"))
c1.display()
c1.edit_profile("Los Angeles", "CA", "90001","Johnny")
c1.display()