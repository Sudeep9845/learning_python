from atm import ATM

if __name__ == "__main__":
    atm2=ATM()
    pin = atm2.get_pin()
    print(f"Current PIN is: {pin}")
    atm2.set_pin("1234")
    pin = atm2.get_pin()
    print(f"New PIN is: {pin}")