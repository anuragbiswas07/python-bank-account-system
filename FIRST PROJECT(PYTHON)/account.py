class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.acc_no = acc

    # Debit method
    def debit(self, bal):
        self.balance -= bal
        print("Rs", bal, "was debited from your account")
        print("Total balance:", self.getbalance())

    # Credit method
    def credit(self, bal):
        self.balance += bal
        print("Rs", bal, "was credited to your account")
        print("Total balance:", self.getbalance())

    # Get balance method
    def getbalance(self):
        return self.balance


# Create account
acc1 = Account(1000, int(input("Enter your account number: ")))

print("Account Number:", acc1.acc_no)

if (acc1.acc_no == 220077):
    print("Current Balance:", acc1.balance)

    debit_amount = int(input("Enter amount to debit: "))
    acc1.debit(debit_amount)

    credit_amount = int(input("Enter amount to credit: "))
    acc1.credit(credit_amount)
else:
    print("Wrong account number!")