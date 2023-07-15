import random
colour_choices = ["green", "cyan", "purple", "blue", "red", "orange"]


# The following function returns a list containing 4 colours selected from colour choices at random and is used to
# represent colours selected by the computer
def colour_generator():
    picked_colours = random.choices(colour_choices, k=4)
    return picked_colours


# Displays instructions to play the game "Mastermind"
def start_menu():
    print()
    print("Welcome, you are currently playing MASTERMIND!\n")
    print("In order to play this game you are required to select four colours from the given choices in order to "
          "guess the colours selected by the computer")
    print(f"Your choices are {colour_choices}")
    print("Please enter your input in the form: cyan purple blue red")
    print("You can enter the same colour multiple times as well")
    print("Good luck and have fun!\n")
    print("What are your guesses?")


# The following functions is used to check if the user input is valid. The function loops through users guesses
# and returns True if the user input is valid, that is the user has guessed only 4 colours and the guesses are in the
# choices provided in colour_choices, if not valid the function returns False
def input_checker(players_guess):

    if len(players_guess) < 4:
            print("Oops! You have guessed too little, please select four guesses")
            return False

    elif len(players_guess) > 4:
            print("Oops! You have guessed too much, please select four guesses")
            return False

    for guess in players_guess:
        if guess not in colour_choices:
            print(f"Oops! You have made an invalid choice '{guess}' please choose valid colours from the choices "
                  f"provided")
            return False

    return True


# The function is used to obtain users input and calls input checker to check if the function is valid, once a valid
# input is obtained is calls correct_spot to check how many colours are guessed correctly and are in their correct
# spot, once it obtains the numeric value for how many colours are in their correct spot, it calls the function wrong spot
# to check the number of colours guessed correctly but are in the wrong spot which would also return a numeric value.
# Once colours_in_correct_position has a value of 4 the user has guessed all colours correctly and the user has won,
# if not the user is provided with a message that indicates the number of colours in the wrong spot to help the user
# make a better guess
def guess_checker(computer_selection):
    player_won = False
    number_of_guesses = 0
    while not player_won:
        number_of_guesses += 1

        while True:
            players_guess = input("\n> ").lower()
            players_guess = players_guess.split(" ")
            if input_checker(players_guess):
                break

        colours_in_correct_position, correct_colours = correct_spot(computer_selection, players_guess)

        colours_in_wrong_position = wrong_spot(computer_selection, players_guess, correct_colours)

        if colours_in_correct_position == 4:

            if number_of_guesses == 1:
                print(f"Congratulations! You have won the game in your first guess! ")
                print("You have won the title master guesser! :P")
                player_won = True
            else:
                print(f"Congratulations! You took {number_of_guesses} guesses to win the game, well done!")
                player_won = True

        else:
            print("Aww looks like you did not win the game!")
            print(f"Guesses that are of the correct colour correct place: {colours_in_correct_position}, "
                  f"correct colour wrong place: {colours_in_wrong_position}")
            print("Please try again!")


# Loops through users_guess and checks with computer selection to see if guessed colours are at the correct position
# if correct the count is incremented and colour is added to correct index, both these value's are later returned to
# guess checker
def correct_spot(computer_selection, players_guess):
    count = 0
    correct_colours = []
    for index in range(len(players_guess)):
        if players_guess[index] == computer_selection[index]:
            count += 1
            correct_colours.append(computer_selection[index])
    return count, correct_colours


# This function checks for colours that are correct but in the wrong position, it first removes colours that are
# correctly guessed and are in the correct spot from the copy of users_guess and comp_selection. It then compares copy
# of users guesses with comp selection, if the users guess is in comp selection it increments colours_wrong_spot and
# removes it from copy_of_comp_selection. It finally returns the number of colours in the wrong spot
def wrong_spot(computer_selection, players_guess, correct_colours):
    copy_of_comp_selection = computer_selection[:]
    copy_of_players_guess = players_guess[:]
    colours_wrong_spot = 0
    for colours in correct_colours:
        copy_of_players_guess.remove(colours)
        copy_of_comp_selection.remove(colours)

    for colours in copy_of_players_guess:
        if colours in copy_of_comp_selection:
            colours_wrong_spot += 1
            copy_of_comp_selection.remove(colours)

    return colours_wrong_spot


computer_selection = colour_generator()
start_menu()
guess_checker(computer_selection)
