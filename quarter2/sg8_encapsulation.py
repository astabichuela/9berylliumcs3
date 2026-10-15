class BankAccount:  #define class
  def __init__(self, account_number, balance):  # initializes a new bank account object with the attributes of account number and balance.
    self.__account_number = account_number # assigns the value of the account number to the private attribute __account_number.
    self.__balance = float(balance) # assigns the value of the balance to the private attribute __balance. it also converts the value of the balance to a float data type.
# a space
  @property # allows us to read private attributes like a public attribute. and it removes the parentheses to make the code cleaner and easier to read. 
  def account_number(self): # defines the method account_number.
    return self.__account_number # this returns the value of the attribute.
# a space
  @property # allows us to read private attributes like a public attribute. and it removes the parentheses to make the code cleaner and easier to read.
  def balance(self): # defines the method balance.
    return self.__balance # this returns the value of the attribute.
# a space  
  def get_account_number(self): # defines the method get_account_number.
    return self.__account_number # this returns the value of the attribute.
# a space
  def get_balance(self): # defines the method get_balance.
    return self.__balance # this returns the value of the attribute.
# a space
  def set_account_number(self, account_number): # defines the method set_account_number.
    self.__account_number = account_number # this sets the value of the attribute to the value of the updated account number.
# a space
  def set_balance(self, balance): # defines the method set_balance.
    if float(balance) >= 0: # sets the condition
      self.__balance = float(balance) # sets the balance to the value of the updated balance if the value of the balance is greater than or equal to zero.
      print() # a new line
      print(f"Balance updated to {balance}") # tells that the balance has been updated to a value.
    else: # if the balance does not meet the condition at the top.
      print() # a new line 
      print(f"Balance updated to {balance}") # tells that the balance has been updated to a value. 
      print("The balance must be not be a negative number.") # prints the message outputed if the balance is a negative number.
#  a space
accounts = []  # this creates an empty list to store the objects of the class
# a space
bank1 = BankAccount("564738", 789) # sets values of the attributes which is account number and balance.
accounts.append(bank1)  #this appends or adds it to the empty list which is accounts.
# a space
print("\nAccount 1") # prints "Account 1"
print(f"Account number: {accounts[0].get_account_number()}") # this prints the account number. it calls get_account_number method to get the account number of the account.
print(f"Balance: {accounts[0].get_balance()}") # this prints the balance. it calls get_balance method to get the balance of the account.
# a space
accounts[0].set_balance(-100) # sets balance to -100
print(f"Account Number: {accounts[0].account_number}") # same as above that prints the account number
print(f"Balance: {accounts[0].balance:.2f}") # same also as above that prints the balance. adds 2 decimal places.
# a space
# the accounts[0] if you might ask, is the first object in the list "accounts". since indexing starts at index zero, and the index zero is the bank 1. and at line 39, 40, 43, 44 it calls the methods on the first object in the list which is bank1.

        

        