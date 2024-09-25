# show_account_module.py

def show_account_info(account_number, accounts):
    if account_number in accounts:
        info = accounts[account_number]
        print("<--------Account Details--------->")
        print("Account Number:",account_number)
        print("Name:",info['holder_name'])
        print("Balance: $",info['balance'])
    else:
        print("Account not found.")
