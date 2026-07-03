# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit

balance = 0

while True:
    atm = input('''
 1. Check Balance
 2. Deposit
 3. Withdraw
 4. Exit
\n''')
    
    if atm == "1":
        print("Current balance is -",balance)

    elif atm == "2":
        deposit = int(input("Entre deposit amount here : "))
        if (deposit > 0):
            balance = deposit + balance
            print(f"{deposit} Amount Deposit Succesfully !\n")
        else:
            print("please entre a valid amount \n")

    elif atm == "3":      
        withdraw = int(input("Entre withdraw amount here :"))
        if (withdraw <= balance ):
            balance = balance - withdraw
            print(f"{withdraw} ruppee withdraw succesfully ! \n")
        else:
            print("not enough cash to withdraw \n ")

    elif atm == "4":
        break 

    else:
        print("Please entre a valid number")           

        

      


