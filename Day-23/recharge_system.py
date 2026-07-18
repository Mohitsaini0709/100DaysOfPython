def recharge():
    a = int(input("Enter Your Mobile Number: "))
    count = len(str(a))
    if (count == 10 ):
        print("\n========== CHOOSE YOUR RECHARGE PLANS ==========")
        print("1. ₹199  - 28 Days | 2GB/day | Unlimited Calls")
        print("2. ₹299  - 28 Days | 3GB/day | Unlimited Calls")
        print("3. ₹399  - 56 Days | 2GB/day | Unlimited Calls")
        print("4. ₹599  - 84 Days | 2GB/day | Unlimited Calls")
        print("5. ₹999  - 365 Days | 2GB/day | Unlimited Calls")

        plan_choice = int(input("Enter Your plan Choice :"))
        match plan_choice:
            case 1:
                print(f''' 
                    Mobile Number = {a}
                    Your plan =  ₹199  - 28 Days | 2GB/day | Unlimited Calls
                    ==========Your Recharge Is Succesfully Done ==========
                ''')
                
            case 2:
                print(f'''
                    Mobile Number = {a}
                    Your plan =  ₹299  - 28 Days | 3GB/day | Unlimited Calls
                    ==========Your Recharge Is Succesfully Done ==========
                ''')
                
            case 3:
                print(f'''
                    Mobile Number = {a}
                    Your plan =  ₹399  - 56 Days | 2GB/day | Unlimited Calls
                    ==========Your Recharge Is Succesfully Done ==========
                ''')
                
            case 4:
                print(f'''
                    Mobile Number = {a}
                    Your plan =  ₹599  - 84 Days | 2GB/day | Unlimited Calls 
                    ==========Your Recharge Is Succesfully Done ==========                    
                ''')
                
            case 5:
                print(f'''
                    Mobile Number = {a}
                    Your plan =  ₹999  - 365 Days | 2GB/day | Unlimited Calls 
                    ==========Your Recharge Is Succesfully Done ==========                    
                ''')
                
            case _:
                print("Invalid Input!")

    else:
        print("Invalid Number ")  


        
          
while True :
    print("\n","="*30 + "Mobile Recharge System" + "="*30)
    print('''
    Menu :- 
        1. Mobile recharge 
        2. Exit
    ''')
    user_choice = int(input("Enter Your Choice : "))

    match user_choice:
        case 1:
            recharge()
        case 2:
            print("Thanks To use These System")
            exit()

        


