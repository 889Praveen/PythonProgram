#from create_account import create_account
from create_account import create_account
from deposit import deposit,withdraw
from show import show_account_info
accounts={}
while(1):
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
        deposit(accou,balance,accounts)
    elif(choice==3):
        accou=input("Enter Account Number:")
        balance=int(input("Enter withdraw Balance:"))
        withdraw(accou,balance,accounts)
    elif(choice==4):
        accou=input("Enter Account Number:")
        show_account_info(accou,accounts)
    else:
        print("Enter Valid Choice..")

