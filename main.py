# PRO 100 - ATM Machine
"""
Due to the problem of writing a dictionary into a file: (which is apparently not allowed - TypeError: write() argument must be str, not dict)
I have used JavaScript linked with Python for this process.
"""
import json
import hashlib
import random
import os
import sys
import msvcrt
customers = json.loads(open("C:/Users/TayoYuva/Documents/Mine/Studies/White Hat JR/Project/C100/cred.json", "r").read())
#print(customers)

class Bank:
    def __init__ (self):
        print()
        print("Welcome to the Bank!")

    def register(self, name, password):
        for i in range(len(list(customers["users"][0].keys()))):
            if (name == list(customers["users"][0].keys())[i]):
                print("Already taken. Try again.")
            else:
                customers["users"].append({
                        name: {
                            "password": (hashlib.md5(password.encode())).hexdigest(),
                            "bank_no": f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}",
                            "bank_id": f"customer_{random.randint(10,99)}@",
                            "cvv":f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}",
                            "amount": 0
                        }
                    })
                os.system(f'node ./Project/C100/index.js "{customers}"')

class ATM:
    def __init__(self, bank_no, name, cvv):
        self.bank_no = bank_no
        self.name  = name
        self.cvv = cvv
        self.amount = int(customers["users"][0][name]["amount"])

    def withdraw(self, wd_amount): #wd means withdraw
        if (wd_amount <= self.amount):
            self.amount -= wd_amount

            print(f"Remaining Amount: {self.amount}")
            print()
            customers["users"][0][self.name]["amount"] = self.amount
            os.system(f'node ./Project/C100/index.js "{customers}"')

    def deposit(self, dp_amount): #dp means deposit
        if (dp_amount <= self.amount):
            self.amount += dp_amount

            print(f"Remaining Amount: {self.amount}")
            print()
            customers["users"][0][self.name]["amount"] = self.amount
            os.system(f'node ./Project/C100/index.js "{customers}"')

    def show_balance(self):
        print(f"Balance Amount: {self.amount}")

# bank = Bank(False)
# bank.register("name", "password")

# atm = ATM("2721020408", "Yuvanth", "123")
# atm.withdraw(1000)
# atm.deposit(1000)
# atm.show_balance()

def secure_password_input(prompt=''): # Got this from the internet
    p_s = ''
    proxy_string = [' '] * 64
    while True:
        sys.stdout.write('\x0D' + prompt + ''.join(proxy_string))
        c = msvcrt.getch()
        if c == b'\r':
            break
        elif c == b'\x08':
            p_s = p_s[:-1]
            proxy_string[len(p_s)] = " "
        else:
            proxy_string[len(p_s)] = "•"
            p_s += c.decode()

    sys.stdout.write('\n')
    return p_s

print("Hello! Welcome to Yuvanth Bank!")
print()
input1 = input("Do you want to go to the bank or the ATM? (type b for bank and a for atm): ")

if(input1.lower() == "a"):
    number = input("Enter your bank number: ")
    print()
    name = input("Enter your name: ")
    print()
    cvv = input(f"{name}, enter your CVV: ")
    print()
    atm = ATM(number, name, cvv)
    task = input("Do you want to deposit (d) or withdraw (w) or show balance (s): ")
    if(task == "d"):
        atm.deposit(input("Enter the amount to deposit: "))
    elif(task == "w"):
        atm.withdraw(input("Enter the amount to withdraw: "))
    elif(task == "s"):
        atm.show_balance()
elif(input1.lower() == "b"):
    print("The bank has only one option that is to register your account.")
    name = input("Enter your name (for register): ")
    print()
    password = secure_password_input(prompt="Enter your password: ")
    print()
    bank = Bank()
    bank.register(name, password)