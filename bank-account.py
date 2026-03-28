class BankAccount:
    def __init__(self, name, balance=0): #attribute
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount): #method
        if amount > 0:
            self.balance += amount
            self.transactions.append(("deposit", amount))
    def withdraw(self, amount): #method
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(("withdraw", amount))
    def get_balance(self): #method
        return self.balance
    def transaction_history(self): #method
        return self.transactions

name= input("Enter account holder's name: ")
account = BankAccount(name)
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
        print(f"Deposited {amount}")
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
        print(f"Withdrew {amount}")
    elif choice == '3':
        balance = account.get_balance()
        print(f"Current balance: {balance}")
    elif choice == '4':
        transactions = account.transaction_history()
        for t in transactions:
            print(f"{t[0].capitalize()}: {t[1]}")
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid option, please try again.") 