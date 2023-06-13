from q4 import *

def train():
    """Function that allows the user to go through the training in q4.py but with 
    an option to either continue or stop the training.

    Returns
    -------
    tuple
        user's trap and cheese quantity by the end of the function
    """
    training = True
    while training == True:
        trap, cheese = setup_trap()
        trap, cheese = sound_horn(trap, cheese)
        train_again = input('\nPress Enter to continue training and "no" to stop training: ')
        if train_again == "":
            continue
        elif train_again.lower() == 'no':
            training = False
    return trap, cheese

def main():
    intro()
    travel_to_camp()
    train()

if __name__ == '__main__':
    main()