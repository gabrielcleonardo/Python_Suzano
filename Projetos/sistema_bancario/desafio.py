menu = """
==== Enter the desired option =====
[1] Deposit
[2] Withdraw
[3] Statement
[4] Exit

=>"""
balance = 0
statament = ""
limit = 500
withdraws_limit = 3
withdraws_count = 0

while True:

    user_option = int(input(menu))

    if user_option == 1:
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

    elif user_option == 4:
        break

    else:
        print("Try again")








