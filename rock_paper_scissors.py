import random

play_input = input("Do you want to play rock, paper, scissors against the computer? Y or N: ")

while play_input == "Y":
    user_input = input("Rock (R), paper (P), or scissors(S)? Enter R, P or S: ")
    if user_input == "R":
        print("You = Rock")
    elif user_input == "P":
        print("You = Paper")
    elif user_input == "S":
        print("You = Scissors")
    else:
        user_input = input("Re-enter input, either R, P or S: ")

    print("VS")

    computer_output = random.choice(range(0,3))
    if computer_output == 0:
        computer_output = "R"
        print("Computer = Rock")
    elif computer_output == 1:
        computer_output = "P"
        print("Computer = Paper")
    elif computer_output == 2:
        computer_output = "S"
        print("Computer = Scissors")

    # if user_input == computer_output:
    #     print("You drew!")
    # else:
    #     if user_input == "R" and computer_output == "S" or user_input == "P" and computer_output == "R" or user_input == "S" and computer_output == "P":
    #         print("Yay, you won!")
    #     else:
    #         print("Oh no, you lost!")

    if user_input == computer_output:
        print("You drew!")
    else:
        if user_input == "R" and computer_output == "S":
            print("Yay, you won! Rock beats Scissors")
        elif user_input == "P" and computer_output == "R":
            print("Yay, you won! Paper beats Rock")
        elif user_input == "S" and computer_output == "P":
            print("Yay, you won! Scissors beats Paper")
        else:
            if computer_output == "R" and user_input == "S":
                print("Oh no, you lost! Rock beats Scissors")
            elif computer_output == "P" and user_input == "R":
                print("Oh no, you lost! Paper beats Rock")
            elif computer_output == "S" and user_input == "P":
                print("Oh no, you lost! Scissors beats Paper")

    play_input = input("Do you want to play rock, paper, scissors again? Y or N: ")