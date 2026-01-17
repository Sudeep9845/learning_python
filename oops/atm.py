"""
### Encapsulation

- Nothing is truly hidden in Python
- Because Python was created for programmers who trust each other.
- But we can suggest that an attribute or method is intended for internal use only.
- This is called "Encapsulation"
- It is a way to restrict access to methods and variables.
- This is to prevent the accidental modification of data.
- We can use single underscore "_" or double underscores "__" before an attribute or method name to
  indicate that it is intended for internal use.
- To hide an attribute or method from others we can use "__"(double underscores)
- example: self.__pin
- Internally: _ATM__pin 
"""

class ATM:

    # Constructor to initialize balance and pin
    # __init__ is a special method in Python classes. 
    # It is called when an object is created from the class and allows the class to initialize the attributes of the class.
    def __init__(self):
        # Hiding attributes using double underscores
        self.__balance=0
        self.__pin=""
        self.__menu()
    # getters and setters can also be used for encapsulation
    def get_pin(self):
        return self.__pin
    
    def set_pin(self,new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN updated successfully.")
        else:
            print("Invalid PIN. PIN must be a 4-digit number.")

        
    def __menu(self):
        user_input = input("Welcome to the ATM. Choose an option: 1. Create PIN 2. Deposit 3. Withdraw 4. Check Balance 5. Exit\n")

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            self.exit()
            return
        else:
            print("Invalid option. Please try again.")
        self.__menu()
    def create_pin(self):
        self.__pin = input("Enter a new PIN: ")
        print("PIN created successfully.")
    
    def deposit(self):
        temp = input("Enter your PIN: ")
        if temp == self.__pin:
            amount = int(input("Enter amount to deposit: "))
            self.__balance = self.__balance + amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Incorrect PIN.")
    
    def withdraw(self):
        temp = input("Enter your PIN: ")
        if temp == self.__pin:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print(f"Withdrew: {amount}. New __balance: {self.__balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Incorrect PIN.")
    
    def check_balance(self):
        temp = input("Enter your PIN: ")
        if temp == self.__pin:
            print(f"Current balance: {self.__balance}")
        else:
            print("Incorrect PIN.")
    
    def exit(self):
        print("Thank you for using the ATM. Goodbye!")
        

## main code
if __name__ == "__main__":
        atm = ATM()
        