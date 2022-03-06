import random


def user_selection():
    user_input = input("Rock (R), paper (P), or scissors(S)? Enter R, P or S: ")
    if user_input == "R":
        user_input = "Rock"
    elif user_input == "P":
        user_input = "Paper"
    elif user_input == "S":
        user_input = "Scissors"
    return user_input


def computer_selection():
    computer_output = random.choice(range(0, 3))
    if computer_output == 0:
        computer_output = "Rock"
    elif computer_output == 1:
        computer_output = "Paper"
    elif computer_output == 2:
        computer_output = "Scissors"
    return computer_output


def winner(user, computer):
    if user == computer:
        print("You drew!")
    else:
        if user == "Rock" and computer == "Scissors":
            print("Yay, you won! Rock beats Scissors")
        elif user == "Paper" and computer == "Rock":
            print("Yay, you won! Paper beats Rock")
        elif user == "Scissors" and computer == "Paper":
            print("Yay, you won! Scissors beats Paper")
        else:
            if computer == "Rock" and user == "Scissors":
                print("Oh no, you lost! Rock beats Scissors")
            elif computer == "Paper" and user == "Rock":
                print("Oh no, you lost! Paper beats Rock")
            elif computer == "Scissors" and user == "Paper":
                print("Oh no, you lost! Scissors beats Paper")



play_input = input("Do you want to play rock, paper, scissors against the computer? Y or N: ")

while play_input == "Y":
    user_action = user_selection()
    print(user_action)
    print("VS")
    computer_action = computer_selection()
    print(computer_action)
    winner(user_action, computer_action)
    play_input = input("Do you want to play rock, paper, scissors again? Y or N: ")