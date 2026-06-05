# a. Simulate a bank account with deposit, withdrawal, and balance enquiry operations

def deposit():
  global curr_balance
  value = float(input("Enter the deposit amount : "))
  curr_balance = +value
  print(value)

def withdrawal():
  global curr_balance
  withdw = float(input("Enter the amount to be withdrawed : "))

  if curr_balance < withdw:
    print("Not possible")
  else :
    print(f"Withdrwaed amount : {withdw}") 
  curr_balance-= withdw  
  #return widr

def balance():
  global curr_balance
  print(f"New balance : {curr_balance}")
  

curr_balance = 0
#user_choice = int(input("Enter the choice of user :"))
def main():
  print("Bank Account Manager")
  # bank_acc = int(input("Enter the bank account number : "))
  print("\n1 : Display current balance")
  print("2 : Deposit ")
  print("3 : Withdrawal")
  print("4 : Exit")

  status = True
  while(status):
    user_choice = int(input("Enter the choice of user :"))
    if user_choice == 1:
        print(f"Current balance : {curr_balance}")

    elif user_choice == 2:
        deposit()  
  
    elif user_choice == 3:

      withdrawal()
    elif user_choice == 4:
        print("Exit")
        break  
        
main()
  

