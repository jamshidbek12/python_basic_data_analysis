class Account():
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account({self.account_number}, {self.name}, balance={self.balance})"


class Bank():
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1001

    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            print("Initial deposit cannot be negative\n")
            return
        account_number = str(self.next_account_number)
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.next_account_number += 1
        print(f"Account created successfully! Your account number is {account_number}\n")

    def view_account(self, account_number):
        if str(account_number) not in self.accounts.keys():
            print("This account number does not exits\n")
            return
        account = self.accounts[str(account_number)]
        return f"Account({account.account_number}, {account.name}, {account.balance})\n"

    def deposit(self, account_number, amount):
        account_number = str(account_number)
        if account_number not in self.accounts.keys():
                print("This account number does not exits\n")
                return
        if amount <= 0:
            print("Deposit amount must be positive\n")
            return
        account = self.accounts[account_number]
        old_balance = account.balance
        account.balance += amount
        return f"Your balance increased from {old_balance} $ to {account.balance} $\n"


    def withdraw(self, account_number, amount):
        account_number = str(account_number)
        if account_number not in self.accounts.keys():
                print("This account number does not exits\n")
                return
        if amount <= 0:
            print("Withdrawal amount must be positive\n")
            return
        account = self.accounts[account_number]
        if amount > account.balance:
            print("Insufficient funds\n")
            return
        old_balance = account.balance
        account.balance -= amount
        return f"Your balance decreased from {old_balance} $ to {account.balance} $\n"

    def view_all(self):
        if not self.accounts:
            print("No accounts found\n")
            return
        for account in self.accounts.values():
            print(f"{account.account_number}, {account.name}, {account.balance}")
    
    def save(self):
        if not self.accounts:
            print("No accounts to save")
            return
        with open("bank_data.txt", 'w') as f:
            for account in self.accounts.values():
                f.write(f"{account.account_number}, {account.name}, {account.balance}\n")
        print("File saved successfully\n")

    def load(self):
        self.accounts = {}
        try: 
            with open("bank_data.txt") as f:
                for line in f.readlines():
                    parts = line.strip().split(",")
                    account_number = parts[0].strip()
                    name = parts[1].strip()
                    balance = float(parts[2].strip())

                    account = Account(account_number, name, balance)
                    self.accounts[account_number] = account
            if self.accounts:
                max_num = max(int(num) for num in self.accounts.keys())
                self.next_account_number = max_num + 1
            print("Account loaded successfully\n")
        except FileNotFoundError:
            print("No saved file found, starting fresh.\n")

    def run(self):
        self.load()
        while True:
            print("\n")
            print(f"1. Create account: \n2. View account: \n3. Deposit: \n4. Withdraw: \n5. Save to file: \n6. Load from file: \n7. Exit\n8. View all")
            choice = input("Select: ")
            if choice not in ["1","2","3","4","5","6","7", "8"]:
                print("Command not found\n")
                continue

            print("\n")
            if choice == "7":
                break
            elif choice == "1":
                name = input("Name: ")
                initial_deposit = float(input("Initial_deposit: "))
                self.create_account(name, initial_deposit)
            elif choice == "2":
                account_number = int(input("Give account number: "))
                result = self.view_account(account_number)
                if result:
                    print(result)
            elif choice == "3":
                account_number = int(input("Give account number: "))
                amount = float(input("Deposit number: "))
                result = self.deposit(account_number, amount)
                if result:
                    print(result)
            elif choice == "4":
                account_number = int(input("Give account number: "))
                amount = float(input("Withdraw number: "))
                result = self.withdraw(account_number, amount)
                if result:
                    print(result)
            elif choice == "5":
                self.save()
            elif choice == "6":
                self.load()
            elif choice == "8":
                self.view_all()

manager_bank = Bank()
manager_bank.run()