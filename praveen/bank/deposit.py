def deposit(account_number, amount, accounts):
    if account_number in accounts:
        if amount > 0:
            accounts[account_number]["balance"] += amount
            return "\n SuccessFull Deposit..."
            #print(f"Account Number:{account_number} Deposited: ${amount:.2f}. New balance: ${accounts[account_number]['balance']:.2f}")
        else:
            print("Deposit amount must be positive.")
    else:
          print("Account not found...!")


def withdraw(account_number, amount, accounts):
    if account_number in accounts:
        if 0 < amount :
            if amount<= accounts[account_number]["balance"]:
                accounts[account_number]["balance"] -= amount
                return "\nwithdraw SuccessFull...."
                #print("Withdrew: $",amount ,". New balance: $", accounts[account_number]['balance'])
            else: 
                if amount > accounts[account_number]["balance"]:
                    return "\nInsufficient funds for this withdrawal...!"
        else:
            return "\nWithdrawal amount must be positive."