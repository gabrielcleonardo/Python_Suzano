menu = """
==== Enter the desired option =====
[1] Deposit
[2] Withdrawl
[3] Statement
[4] Exit

=>"""
balance = 0
statement = ""
limit_value = 500
withdrawl_limit = 3
withdrawl_count = 0

while True:

    user_option = int(input(menu).strip())

    if user_option == 1: ##DEPOSIT##

        deposit = float(input("Enter the amount you want to deposit: ").strip())
        if deposit > 0:
            balance += deposit
            statement += f"Deposit: +R$ {deposit:.2f}\n"
            print(f"R$ {deposit:.2f} deposited successfully")

        else:
            print("==== Invalid amount. Deposit must be greater than zero. ====")

    elif user_option == 2: ## WITHDRAWL ##

        if withdrawl_count >= withdrawl_limit:
            print("==== Daily number of withdrawals exceeded. ====")

        else:
            value = float(input("Enter the amount you want to withdraw: ").strip())

            if value > limit_value:
                print(f"==== Your limit is {limit_value}, please try again ====")

            elif value > balance:
                print(f"==== Insufficient balance. Your balance is ${balance:.2f}. ====")

            elif value <= 0:
                print("==== Invalid amount. ====")

            else:
                balance -= value
                withdrawl_count += 1
                statement += (f"Withdrawl: -R$ {value:.2f}\n")
                print(f"Withdrawal of R$ {value:.2f} completed successfully")

    elif user_option == 3: ## STATEMENT
        print("\n======== Bank Statement ========")
        print("No transactions found") if not statement else print(statement)
        print("======== Current Balance ========")
        print(f"R$ {balance:.2f}")
        print("================================\n")
    elif user_option == 4:
        print("==== Thank you for using our banking system. Goodbye! ====")
        break

    else:
        print("==== Invalid option. Please try again. ====")








