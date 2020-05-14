secret_number = 8
guess_limit = 0
guess_count = 0
outOfGuesses = False
#number guessing game
#set the various guess limit for each level,
# i wanted the guess limit to reduce as the user makes a wrong guess until they were out of guesses
#i don't think i did this correctly.
def guess_limit(level):
    if level == "Easy":
        guess_limit = 6
        guess_count = 0
        guess_count += 1

    if level == "Medium":
        guess_limit = 4
        guess_count = 0
        guess_count += 1

    if level == "Hard":
        guess_limit = 3
        guess_count = 0
        guess_count += 1

    return guess_limit

#if the user makes a wrong guess here, I tell the user that there are 3 levels and ask them to choose one.

while True:
    guess = int(input("Enter guess: "))
    if guess != secret_number:
        print("""
    There are 3 levels;
    Easy: You get a chance to choose a number from 1 to 10 and you have 6 guesses,
    Medium: You get a chance to choose a number from 1 to 20 and you have 3 guesses,
    Hard: You get a chance to choose a number from 1 to 50 and you have 3 guesses.
    """)
        choice = input("Make a choice: ")
#if the coice is easy, I ask them to enter their guess and wanted to ensure that the guess limit reduces as they guessed wrong
        if choice == "Easy":
            input("Enter guess: ")
            guess_limit = 6
            guess_count += 1
#i want to print out a msg showing the number of guess they have as their guess limit reduces.
            if guess !=secret_number:
                print("That was wrong")
                guess_count = print(f"You have {guess_limit}")
#i want to do the same to the hard  and to the medium level.
        elif choice == "Medium":
            input("Enter guess: ")
            guess_limit = 4
            guess_count += 1
            if guess !=secret_number:
                print("That was wrong")
                guess_count = print(f"You have {guess_limit}")

        elif choice == "Hard":
            input("Enter guess: ")
            guess_limit = 3
            guess_count += 1
            if guess !=secret_number:
                print("That was wrong")
                guess_count = print(f"You have {guess_limit}")
#i want the program to print out an error msg if a msg if a wrong selection is made.
        elif choice != "Easy" or choice != "Medium" or choice != "Hard":
            print("Invalid selection.")
        elif outOfGuesses:
            outOfGuesses = True
            print("Game over you lose.")
            break
#if the user guesses right, then they win.
    else:
        print("You are right!")
        break
