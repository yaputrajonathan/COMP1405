#Jonathan 101161272



while True:
    userPrice = 0

    '''introduction'''
    print("-"*32)
    print("| Welcome to Seb's Sub Shoppe! |")
    print("-"*32)
    print("")

    '''Subs menu'''
    useSub = ""
    while True:
        useSub = input("\
Please select you sub:\n\
1. \"Meat\"-ball sub ($7.99)\n\
2. Cold-cut Club sub ($8.25)\n\
3. Philly's Cheese Mis-Steak sub ($9.55)\n\
4. Veggie Pile sub ($6.75)\n\
> ")
        
        if useSub != "1" and useSub !="2" and useSub !="3" and useSub!="4":     #error message if the user input is not in the range of 1 to 4, or other strings
            print(f"I'm sorry, {str(useSub)}, is not an available option.")
        else:
            break

    if useSub == "1":
        useSub = "\"Meat\"-ball sub"
        userPrice += 7.99
    elif useSub == "2":
        useSub = "Cold-cut Club sub"
        userPrice += 8.25
    elif useSub == "3":
        useSub = "Philly's Cheese Mis-Steak sub"
        userPrice += 9.55
    else:
        useSub = "Veggie Pile sub"
        userPrice += 6.75

    '''Topping Menu'''
    userTopping = ""    
    print("")
    print("\
Select your toppings.\n\
Type any of the following and hit enter:\n\
lettuce, tomatoes, onions, peppers, jalapenos, pickles, cucumbers, olives, or guacamole.\n\
Please note: guacamole costs an extra $1.50\n\
Type \"done\" to stop.")
    while True:
        toppingSub = input("> ")
        if toppingSub == "done":
            break
        elif toppingSub == "guacamole":         #if the user wants guacamole, $1.50 is added
            userPrice += 1.5
            userTopping += toppingSub+" "
        elif toppingSub != "lettuce" and toppingSub != "tomatoes" and toppingSub != "onions" and toppingSub != "peppers" and toppingSub != "jalapenos" and toppingSub != "pickles"\
            and toppingSub != "cucumbers" and toppingSub != "olives" and toppingSub != "guacamole":         #error message if the user did a spelling mistake
            print(f"Sorry, {toppingSub} is not an available topping.")
        else:
            userTopping += toppingSub +" "


    '''The Receipt'''
    print("")
    print("Your Order:")
    print(f"Sub: {useSub}")
    print(f"Toppings: {userTopping}")
    userConfirmation = input("Is this correct? (y/n) ")
    userHST = 0.13*userPrice          
    userTotal = userHST + userPrice

    if userConfirmation == "y":
        print("")
        print("-"*17)
        print(f"Subtotal: ${userPrice :.2f}")
        print(f"Tax: ${userHST :.2f}")
        print("-"*17)
        print(f"Total: ${userTotal :.2f}")
        print("-"*17)
        print("")
        print("Thanks for shopping at Seb's Subs.")
        print("Have a nice day!")
        print("")
        break
    else:
        print("I'm sorry, please try again.")       #if the user enters "n" they will start from the beginning again


