# account_module.py

def create_account(account_number, holder_name, accounts):
    if account_number in accounts:
         print("Account already exists...!")
    else:
        accounts[account_number] = {"holder_name": holder_name,"balance": 0 }
        return "SuccessFull Account created for", holder_name," with account Number:",account_number
         
