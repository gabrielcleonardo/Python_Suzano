menu = """
==== Enter the desired option =====
[1] Deposit
[2] Withdraw
[3] Statement
[4] Exit

=>"""
balance = 0
statament = ""
limit_value = 500
withdraws_limit = 3
withdraws_count = 0

while True:

    user_option = int(input(menu))

    if user_option == 1: ##DEPOSIT##
        try:
            deposit = float(input("Amount do you want to deposit: "))
            if deposit > 0:
                balance += deposit
                statament += f"R$ {deposit:.2f}\n"
                print(f"R$ {deposit:.2f} deposited successfully")

            else:
                print("==== No value to deposit ====")
        except ValueError:
            print("==== Invalid Value, try again ====")

    elif user_option == 2: ## WITHDRAWN ##

        if withdraws_count >= withdraws_limit:
            print("Number of withdraws exceeded")

        else:
            value = float(input("Amount do you want to withdraw: "))

            if value > limit_value:
                print(f"Your limit is {limit_value}, please try again")

            elif value > balance:
                print(f"Your balance is {balance}, please try again")

            elif value <= 0:
                print("Invalid value")

            else:
                balance -= value
                withdraws_count += 1
                statament += (f"R$ {value:.2f}\n")
                print(f"Withdrawal of R$ {value:.2f} successfully completed")


    elif user_option == 4:
        break

    else:
        print("==== Please, Try again ====")








