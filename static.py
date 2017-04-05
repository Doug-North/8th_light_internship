import os

HUMAN = -1
OPPOSITION = 1


def clear_screen():
    """Helps to make the game look visually clean"""
    os.system('cls' if os.name == 'nt' else 'clear')


def game_style():
    """
    initial questions displayed only if it is first
    :returns
    player, only changed if human vs human thus overriding standard formula
    """
    pvp_choice = None
    player2 = None
    while pvp_choice is None:  # Player v Player or Player v Computer
        pvp_choice = input("Would you like to play against man or machine?[MAN/MACHINE]: ")
        if pvp_choice.lower() == 'man':
            player2 = 'HUMAN2'
            return player2
        elif pvp_choice.lower() == 'machine':
            continue
        else:
            print("I'm not getting you...")
            pvp_choice = None


def who_goes_first():
    """
    Determines which player initiates first move
    :returns
    opposition or human on who goes second

    """
    first = None
    while first is None:
        first = input("Would you like to go first? [Y/N]: ")
        if first.lower() == 'y':
            next_move = HUMAN
        elif first.lower() == 'n':
            next_move = OPPOSITION
        else:
            print("Not an option buddy, give it another shot. \n")
            first = None
    return next_move


def choose_symbol():
    """
    Allows player to pick from 'O' and 'X'
    :return:
    list of XO or OX and list indices are then used in-game
    """
    symbol_choice = None
    while symbol_choice is None:  # Player1 chooses their symbol
        symbol_choice = input("Would you like to be 'O' or 'X'?: ")
        if symbol_choice.lower() == 'o':
            symbol = 'OX'
        elif symbol_choice.lower() == 'x':
            symbol = 'XO'
        else:
            print("Woah, what is that symbol? Nope not having it.\n")
            symbol_choice = None
    return symbol



