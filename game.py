import random

from name import *
from train import *
from shop import *

def game_title():
    title = 'Mousehunt'
    # Logo
    logo = r"""
       ____()()
      /      @@
`~~~~~\_;m__m._>o
"""
    # Author
    author = 'An INFO1110/COMP9001 Student'
    # Credits
    credits = f"""Inspired by Mousehunt© Hitgrab
Programmer - {author}
Mice art - Joan Stark"""

    print(title)
    print(logo)
    print(credits)

def train():
    training = True
    while training == True:
        trap, cheese = setup_trap()
        trap, cheese = sound_horn(trap, cheese)
        train_again = input('\nPress Enter to continue training and "no" to stop training: ')
        if train_again == "":
            continue
        elif train_again.lower() == 'no':
            training = False
            return (trap, cheese)
            

def hunt(points, gold, cheese):
    """Function that initiates the hunt, which allows the user to use
    their acquired cheese, as well as gain points.

    Parameters
    ----------
    points : int
        amount of points the player has
    gold : int
        amount of gold the player has
    cheese : int
        amount of cheese the player has

    Returns
    -------
    tuple
        returns the amount of points and gold acquired, as well the 
        amount of cheese used for the hunt
    """
    count = 0
    hunting = True

    while hunting == True:

        print('Sound the horn to call for the mouse...')        
        user_horn = input('Sound the horn by typing "yes": ')

        if user_horn.lower().strip() == 'yes':

            if cheese >= 1:
                if random.random() > 0.5:
                    cheese -= 1
                    points = points
                    gold = gold
                    count += 1
                    print('Nothing happens.')
                    print(f'My gold: {gold}, My points: {points}')
                    print()

                    if count == 5:
                        user_continue = input('Do you want to continue to hunt? ')
                        if user_continue.lower() == 'yes':
                            count = 0
                        elif user_continue.lower() == 'no':
                            count = 0
                            hunting = False
                            return (points, gold, cheese)

                else:
                    points += 115
                    gold += 125
                    cheese -= 1
                    count = 0
                    print('Caught a Brown mouse!')
                    print(f'My gold: {gold}, My points: {points}')
                    print()
            
            elif cheese == 0:
                count += 1
                print('Nothing happens. You are out of cheese!')
                print(f'My gold: {gold}, My points: {points}')
                print()

                if count == 5:
                    user_continue = input('Do you want to continue to hunt? ')
                    if user_continue.lower() == 'yes':
                        count = 0
                    elif user_continue.lower() == 'no':
                        count = 0
                        hunting = False
                        return (points, gold, cheese)
                    
        elif user_horn.lower().strip() == 'stop hunt':
            hunting = False
            return (points, gold, cheese)
                
        elif user_horn.lower().strip() != 'yes':
            print('Do nothing.')
            print(f'My gold: {gold}, My points: {points}')
            print()
    
    return (points, gold, cheese)

def store(gold, cheese, trap):
    print("Welcome to The Cheese Shop!\nCheddar - 10 gold")

    menu = True
    while menu == True:
        user_select = int(input('\nHow can I help ye?\n1. Buy cheese\n2. View inventory\n3. Leave shop\n'))
        if user_select == 1:
            output = buy_cheese(gold)
            if output == (0, 0):
                continue
            else:
                gold_spent, cheese_bought = output
                gold -= gold_spent
                cheese += cheese_bought
            
        elif user_select == 2:
            display_inventory(gold, cheese, trap)

        elif user_select == 3:
            menu = False
            
    return (gold, cheese) # outside function so that it returns


def game_menu(name, points, gold, cheese, trap):
    """Function for the game menu, which consists of options for the user 
    to either exit the game, join the hunt or visit the cheese shop.

    Parameters
    ----------
    name : str
        name of the player
    points : int
        amount of points the player has
    gold : int
        amount of gold the player has
    cheese : int
        amount of cheese the player has
    trap : str
        type of trap the user has
    
    Returns
    -------
    tuple
        returns the amount of points, gold, cheese and type of trap
        back to the main function where the variables are stored
    """
    menu = True
    while menu == True:
            user_select = input(f'\nWhat do ye want to do now, Hunter {name}?\n1. Exit game\n2. Join the Hunt\n3. The Cheese Shop\n')
            if user_select == '1':
                menu = False
                
            elif user_select == '2':
                hunting = hunt(points, gold, cheese)
                # returns only when player has gained something out of the hunt
                if hunting is not None:
                    points, gold, cheese = hunting
                
            elif user_select == '3':
                output = store(gold, cheese, trap)
                if output is not None:
                    gold, cheese = output

    return(points, gold, cheese, trap)
                    

def main():
    points = 0
    gold = 125
    cheese = 0
    trap = "Cardboard and Hook Trap"

    game_title()
    
    name = input("\nWhat's ye name, Hunter?\n")
    if is_valid_name(name) == True:
        print(f"Welcome to the Kingdom, Hunter {name}!")
    else:
        name = "Bob"
        print(f"Welcome to the Kingdom, Hunter Bob!")

    print("Before we begin, let's train you up!")

    user_choice = input('Press "Enter" to start training or "skip" to Start Game: ')
    if user_choice == "":
        print()
        intro()
        travel_to_camp()
        trap, cheese = train()
        points, gold, cheese, trap = game_menu(name, points, gold, cheese, trap)
        
    elif user_choice.lower() == "skip":
        game_menu(name, points, gold, cheese, trap)


if __name__ == '__main__':
    main()