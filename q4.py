def intro():
    print("Larry: I'm Larry. I'll be your hunting instructor.")

def travel_to_camp():
    print("Larry: Let's go to the Meadow to begin your training!")
    user_travel = input("Press Enter to travel to the Meadow...")
    if user_travel == "": 
        print("Travelling to the Meadow...")
        print("Larry: This is your camp. Here you'll set up your mouse trap.")

def setup_trap():
    """Function that allows the player to select a trap from Larry.

    Returns
    -------
    tuple
        player's trap and cheese quantity by the end of the function
    """

    trap = " "
    cheese = 0

    print("Larry: Let's get your first trap...")
    user_enter = input("Press Enter to view traps that Larry is holding...")

    if user_enter == "":
        print("Larry is holding...\nLeft: High Strain Steel Trap\nRight: Hot Tub Trap")
        user_trap_select = input('Select a trap by typing "left" or "right": ')
        
        if user_trap_select.lower().strip() == 'left':
            trap = "High Strain Steel Trap"
            cheese = 1
            print(f'Larry: Excellent choice.\nYour "{trap}" is now set!\n'
            'Larry: You need cheese to attract a mouse.\n'
            'Larry places one cheddar on the trap!')
            return (trap, cheese)

        elif user_trap_select.lower().strip() == 'right':
            trap = "Hot Tub Trap"
            cheese = 1
            print(f'Larry: Excellent choice.\nYour "{trap}" is now set!\n'
            'Larry: You need cheese to attract a mouse.\n'
            'Larry places one cheddar on the trap!')
            return (trap, cheese)
            
        else:
            trap = "Cardboard and Hook Trap"
            cheese = 0
            print("Invalid command! No trap selected.\nLarry: Odds are slim with no trap!")
            return (trap, cheese)
        
def sound_horn(trap, cheese):
    """Function that starts the hunt depending on the user's input.

    Parameters
    ----------
    trap : str
        stores "High Strain Steel Trap", "Hot Tub Trap" or in case
        of the user having no trap, stores "Cardboard and Hook Trap"

    cheese : int
        stores the number of cheddar the player has

    Returns
    -------
    tuple
        user's trap and cheese quantity by the end of the function
        
    """
    print('Sound the horn to call for the mouse...')        
    user_horn = input('Sound the horn by typing "yes": ')

    if user_horn.lower().strip() == 'yes':
        if trap == "High Strain Steel Trap" or "Hot Tub Trap" and cheese == 1:
            cheese -= 1
            print('Caught a Brown mouse!')
            print('Congratulations. Ye have completed the training.')
            print('Good luck~')
            return (trap, cheese)

        elif trap == "Cardboard and Hook Trap" and cheese == 0:
            print('Nothing happens.\nTo catch a mouse, you need both trap and cheese!')
            return (trap, cheese)
    
    elif user_horn.lower().strip() != 'yes':
        if trap == "High Strain Steel Trap" or "Hot Tub Trap" and cheese == 1:
            cheese -= 1
            print('Nothing happens.\nTo catch a mouse, you need both trap and cheese!')
            return (trap, cheese)
            
        elif trap == "Cardboard and Hook Trap":
            print('Nothing happens.')
            return (trap, cheese)

    # else statement in case of any other input 
    else:
        print('Nothing happens.')
        return (trap, cheese)            
    
def main():
    intro()
    travel_to_camp()
    # store trap and cheese to both setup_trap() and sound_horn() to update
    trap, cheese = setup_trap()
    trap, cheese = sound_horn(trap, cheese)

if __name__ == "__main__":
     main()