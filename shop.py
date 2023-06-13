def buy_cheese(gold):
    """Function that allows the player to buy a certain amount of cheese for the hunt

    Parameters
    ----------
    gold : int
        amount of gold that the player currently has

    Returns
    -------
    tuple
        returns the amount of gold spent and cheese bought at the shop
    """
    gold_spent = 0
    cheese_bought = 0
    print(f'You have {gold} gold to spend.')
    user_cheese_quantity = input('State [cheese quantity]: ')
    if user_cheese_quantity.lower() == 'back':
        return (gold_spent, cheese_bought)
                
    user_cheese_quantity = user_cheese_quantity.split()
    if len(user_cheese_quantity) != 2:
        print('Sorry, did not understand.')
        return (gold_spent, cheese_bought)

    user_cheese = str(user_cheese_quantity[0])
    user_quantity = int(user_cheese_quantity[1])

    if user_cheese.lower() == 'cheddar' and 0 < user_quantity*10 <= gold:
        gold_spent = user_quantity * 10
        cheese_bought = user_quantity
        print(f'Successfully purchase {user_quantity} cheddar.')
        return (gold_spent, cheese_bought)
    
    elif user_cheese.lower() != 'cheddar' and user_quantity != int:
        print('Sorry, did not understand.')
        return (gold_spent, cheese_bought)

    elif user_quantity < 0:
        print('Must purchase a positive amount of cheese.')
        return (gold_spent, cheese_bought)
    
    # else statement for any other inputs not stated above
    else:
        print('Insufficient gold.')   
        return (gold_spent, cheese_bought)

def display_inventory(gold, cheese, trap):
    """_summary_

    Parameters
    ----------
    gold : int
        amount of gold the player has
    cheese : int
        amount of cheese the player has
    trap : str
        the type of trap the player has
    """
    print(f'Gold - {gold}\nCheddar - {cheese}\nTrap - {trap}')

def main():
    gold = 125
    cheese = 0
    trap = "Cardboard and Hook Trap"

    print("Welcome to The Cheese Shop!\nCheddar - 10 gold")

    menu = True
    while menu == True:
        user_select = int(input('\nHow can I help ye?\n1. Buy cheese\n2. View inventory\n3. Leave shop\n'))
        if user_select == 1:
            output = buy_cheese(gold)
            # set output variable to make it iterable
            if output == (0, 0):
                continue
            else:
                gold_spent, cheese_bought = output
                gold -= gold_spent
                cheese += cheese_bought
                continue
            
        elif user_select == 2:
            display_inventory(gold, cheese, trap)

        elif user_select == 3:
            menu = False
        
if __name__ == '__main__':
    main()