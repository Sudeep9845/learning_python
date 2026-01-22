class Customer:
    def __init__(self,name=""):
        
        self.name = name


# pass by reference example
def greet(customer):
    print(id(customer))
    customer.name = input("Enter your name: ")
    print(f"Hello, {customer.name}! Welcome to the bank.")
    print(id(customer))

if __name__ == "__main__":
    # customer is a Reference variable that refers to the object of the Customer class.
    customer1 = Customer("Ankita")
    print(id(customer1))
    greet(customer1)
    print(customer1.name)
## Output:
# 129852222163664
# 129852222163664
# Enter your name: Joe
# Hello, Joe! Welcome to the bank.
# 129852222163664
# Joe

# Both customer1 and customer inside the greet function refer to the same object in memory. Hence, any changes made to the object's attributes inside the function are reflected outside the function as well.