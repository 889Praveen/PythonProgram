#from create_account import create_account
from bank.create_account import create_account
from bank.deposit import deposit,withdraw
from bank.show import show_account_info
accounts={}
while(1):
    print("<-------------------------------->")
    print("1:Creating a new account")
    print("2:Deposit")
    print("3:Withdraw")
    print("4:Show Account information")
    choice=int(input("Enter choice:"))
    if(choice==1):
        accou=input("Enter Account Number:")
        name=input("Enter Name:")
        print(create_account(accou,name,accounts))
    elif(choice==2):
        accou=input("Enter Account Number:")
        balance=int(input("Enter Deposit Balance:"))
        print(deposit(accou,balance,accounts))
    elif(choice==3):
        accou=input("Enter Account Number:")
        balance=int(input("Enter withdraw Balance:"))
        print(withdraw(accou,balance,accounts))
    elif(choice==4):
        accou=input("Enter Account Number:")
        print("<--------Account Details--------->")
        print(show_account_info(accou,accounts))
    else:
        print("Enter Valid Choice..")

