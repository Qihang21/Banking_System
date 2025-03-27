from banking_system import BankingSystem

if __name__ == "__main__":
    bank = BankingSystem()
    actions = {
        "1": bank.create_account,
        "2": bank.deposit_money,
        "3": bank.withdraw_money,
        "4": bank.transfer_money,
        "5": bank.check_balance,
        "6": bank.download_accounts
    }

    while True:
        print("\n")
        print("**** Welcome ****")
        print("1. Create Account \n" \
              "2. Deposit Money \n" \
              "3. Withdraw Money \n" \
              "4. Transfer Money \n" \
              "5. Check Balance \n" \
              "6. Download Accounts \n" \
              "7. Exit")
        choice = input("Choose an option: ")

        if choice == "7":
           print("Exit the system")
           break 
           
        action = actions.get(choice)
        if action:
           action()
        else:
           print("Invalid choice, please try again.")
