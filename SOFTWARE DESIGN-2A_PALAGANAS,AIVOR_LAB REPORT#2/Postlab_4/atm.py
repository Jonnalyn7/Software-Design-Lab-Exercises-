from breezypythongui import EasyFrame
from bank import Bank, createBank
class ATM(EasyFrame):
"""Represents an ATM window.
The window tracks the bank and the current account.
The current account is None at startup and logout.
"""
def __init__(self, bank):
"""Initialize the frame and establish the data model."""
    EasyFrame.__init__(self, title="ATM")
# Create refernces to the data model.
self.bank = bank
self.account = None
# Create and add the widgets to the window."""
self.nameLabel = self.addLabel(row=0, column=0,
text="Name")
self.pinLabel = self.addLabel(row=1, column=0, text="PIN")
self.amountLabel = self.addLabel(row=2, column=0,
text="Amount")
self.statusLabel = self.addLabel(row=3, column=0,
text="Status")
self.nameField = self.addTextField(row=0, column=1,
text="")
self.pinField = self.addTextField(row=1, column=1,
text="")
self.amountField = self.addFloatField(row=2, column=1,
value=0.0)
self.statusField = self.addTextField(row=3, column=1,
text="Welcome to the Bank!",
state="readonly")
self.balanceButton = self.addButton(row=0, column=2,
text="Balance",
command=self.getBalance,
state="disabled")
self.depositButton = self.addButton(row=1, column=2,
text="Deposit",
command=self.deposit,
state="disabled")
self.withdrawButton = self.addButton(row=2, column=2,
text="Withdraw",
command=self.withdraw,
state="disabled")
self.loginButton = self.addButton(row=3, column=2,
text="Login",
command=self.login)
Question: The ATM program allows a user an inde!nite number of atte
My Textbook Solutions
Mechanics of
Materials
7th Edition
Introduction
to Chemical...
6th Edition
Introduction
to Chemical...
7th Edition
View all solutions
Post a question
Answers from our experts for your tough
homework questions
Enter question
Continue to post
19 questions remaining
Find solutions for your homework Search
! ! Home Study tools " My courses " My books My folder Career Life "
def login(self):
"""Attempts to login the customer. If successful,
enables the buttons, including logout."""
name = self.nameField.getText()
pin = self.pinField.getText()
self.account = self.bank.get(name, pin)
if self.account:
self.statusField.setText("Hello, " + name + "!")
self.balanceButton["state"] = "normal"
self.depositButton["state"] = "normal"
self.withdrawButton["state"] = "normal"
self.loginButton["text"] = "Logout"
self.loginButton["command"] = self.logout
else:
self.statusField.setText("Name and pin not found!")
def logout(self):
"""Logs the cusomer out, clears the !elds, disables the
buttons, and enables login."""
self.account = None
self.nameField.setText("")
self.pinField.setText("")
self.amountField.setNumber(0.0)
self.statusField.setText("Welcome to the Bank!")
self.balanceButton["state"] = "disabled"
self.depositButton["state"] = "disabled"
self.withdrawButton["state"] = "disabled"
self.loginButton["text"] = "Login"
self.loginButton["command"] = self.login
def getBalance(self):
"""Displays the current balance in the status !eld."""
text = "Balance = $" + str(self.account.getBalance())
self.statusField.setText(text)
def deposit(self):
"""Attempts a deposit. If not successful, displays
error message in status!eld; otherwise, announces
success."""
amount = self.amountField.getNumber()
message = self.account.deposit(amount)
if not message:
self.statusField.setText("Deposit successful")
else:
self.statusField.setText(message)
def withdraw(self):
"""Attempts a withdrawal. If not successful, displays
error message in status!eld; otherwise, announces
success."""
amount = self.amountField.getNumber()
message = self.account.withdraw(amount)
if not message:
self.statusField.setText("Withdrawal successful")
else:
self.statusField.setText(message)
def main(!leName=None):
"""Creates the bank with the optional !le name,
wraps the window around it, and opens the window.
Saves the bank when the window closes."""
if not !leName:
bank = createBank(5)
else:
bank = Bank(!leName)
print(bank)
atm = ATM(bank)
atm.mainloop()
if __name__ == "__main__":
main()