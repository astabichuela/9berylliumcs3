class BankAccount:  #define class
  def __init__(self, account_number, balance): 
    self.__account_number = account_number  # this defines and initializes both attributes.
    self.__balance = float(balance)

  @property  
  def account_number(self): 
    return self.__account_number # this returns the value of the attribute.

  @property
  def balance(self):
    return self.__balance 
    
  def get_account_number(self):
    return self.__account_number 

  def get_balance(self):
    return self.__balance

  def set_account_number(self, account_number):
    self.__account_number = account_number

  def set_balance(self, balance):
    if float(balance) >= 0:
      self.__balance = float(balance)
      print()
      print(f"Balance updated to {balance}")
    else:
      print()
      print(f"Balance updated to {balance}")
      print("The balance must be not be a negative number.") # this whole part of def set_balance is to check if the balance is negative or not.

accounts = []  # this creates an empty list to store the objects of the class

bank1 = BankAccount("564738", 789)
accounts.append(bank1)  #this appends or adds it to the empty list which is accounts.

print("\nAccount 1")
print(f"Account number: {accounts[0].get_account_number()}") # this prints the account number. it calls get_account_number method to get the account number of the account.
print(f"Balance: {accounts[0].get_balance()}") # this prints the balance. it calls get_balance method to get the balance of the account.

accounts[0].set_balance(-100) # sets balance to -100
print(f"Account Number: {accounts[0].account_number}") # same as above that prints the account number
print(f"Balance: {accounts[0].balance:.2f}") # same also as above that prints the balance.






        

        