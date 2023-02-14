# Name : Shahriar Mahmud Arman
# ID: C221055

print("********************************************************************************")
print("********************************************************************************")
print("*******************_________Welcome to our Bank__________***********************")
print("********************************************************************************")
print("********************************************************************************")

class Bank:

    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 500
        self.max_withdraw = 50000
        
        
    def show_balance(self):
        return self.balance
    def withdraw (self , amount):
        if amount < self.min_withdraw:
            return f"You have to withdraw a minimul money which is {self.min_withdraw} taka"
        elif amount > self.max_withdraw:
            return f"You cannot withdraw the maximum withdraw limit is  {self.max_withdraw} taka"
        elif amount > self.balance:
            return "Sorry You do not have enough balamce"
        elif amount == self.balance:
            return "   Withdraw Successful  "
       
       
        else:
            self.balance = self.balance-amount
            return f" Here is your money :{self.balance}. Thanks for staying with us "
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    
print("")
print("")
print("")

def menu():
        print("                     ******  Enter Your Choice  ******")
        print("                     ---------------------------------")
        print("                     ---------------------------------")

        print("[1] Enter How much money you want to add in Your Account : ")
        print("[2] Current balance")
        print("[3] Withdraw ")
        print("[4] Deposite money")
        print("[0] TO EXIT ")

menu()
option=int(input("ENTER  : ")) 



while option !=0:

    if option == 1:
        print("Enter amount: ")
        my_bank = Bank(int(input()))
       
    elif option == 2:
        print("Your current balance: ")
        print(my_bank.show_balance())
       
    
    elif option == 3:
        print("Enter how much money you want to withdraw: ")
        reply = my_bank.withdraw(int(input()))
        print(reply)
        

    elif option == 4:
        print("How much money do you want to deposite?: ")
        my_bank.deposit(int(input()))
        print("Here is your money: ")
        print(my_bank.show_balance())
    
    else:
        print("Invalid option")
        
    
    print()
    menu()
    option=int(input("PRESS YOUR DESIRED BUTTON: ")) 
    