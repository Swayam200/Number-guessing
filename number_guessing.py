from random import randint

logo = """

   _____                       _   _                                  _               _ 
  / ____|                     | | | |                                | |             | |
 | |  __ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __| |
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__| |
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |  |_|
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|  (_)
                                                                                        
                                                                                        

"""

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def attempts_calculator(input_difficulty):
    if input_difficulty == 'easy':
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS


def condition_check(guess, act_num):
    if guess < act_num:
        print("Too low.")
    elif guess > act_num:
        print("Too high.")
    elif guess == act_num:
        print(f"You got it! The answer was {act_num}")
        return True
    return False


def game():
    # Initial Welcome Statements
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Choosing a difficulty
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts_remaining = attempts_calculator(difficulty)

    # Computer selects a random number
    number = randint(1, 100)

    # While the attempts are greater than 0 the game continues
    # We also initialise a game_over which when user guesses correct number stops the loop
    game_over = False
    while attempts_remaining != 0 and not game_over:
        print(f"You have {attempts_remaining} attempts remaining to guess the number.")
        guessed_number = int(input("Make a guess: "))

        # If user guesses the number wrong, attempts remaining is subtracted by one
        if condition_check(guessed_number, number) is False:
            attempts_remaining -= 1
        # If user guesses correct number, the loop ends
        else:
            game_over = True
        if not game_over:
            # If attempts remaining reaches 0, user loses
            if attempts_remaining == 0:
                print("You are out of guesses, you lose.")
            # While the attempts remaining are greater than zero, the user is prompted to guess again
            if attempts_remaining > 0:
                print("Guess again.")


game_flag = True
while game_flag:
    want_to_play = input("Do you wish to play a game of Number Guessing ('y' or 'n'): ").lower()
    if want_to_play == 'y':
        game()
    else:
        game_flag = False
        print("Good Bye!")

