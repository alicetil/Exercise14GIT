# Task A: Create a Game: Rock, Paper, Scissors!
# You are going to create a command line version of the game: Rock...Paper...Scissors!
# The user will play against the computer at this game. You should design a program that does the following:
# • Prompts the user to enter a value: R, P or S
# • The program should convert this value into Rock, Paper, or Scissors respectively
# • Asks the computer to generate a random value between 0 and 2
# • Convert the computer’s choice. 0 becomes Rock; 1 becomes Paper; 2 becomes Scissors
# • Compare the user’s choice with the computer’s choice to display a message indicating whether
# the user won, lost or drew against the computer
# Showcase what you have learned about conditional statements and create your own functions

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
    weapon_of_choice = ["Rock", "Paper", "Scissors"]
    computer_output = weapon_of_choice[random.choice(range(0, 2))]
    return computer_output


def check_winner(user, computer):
    if user == computer:
        print("You drew!")
        outcome = "draw"
    else:
        if user == "Rock" and computer == "Scissors":
            print("You won! Rock beats Scissors")
            outcome = "win"
        elif user == "Paper" and computer == "Rock":
            print("You won! Paper beats Rock")
            outcome = "win"
        elif user == "Scissors" and computer == "Paper":
            print("You won! Scissors beats Paper")
            outcome = "win"
        else:
            outcome = "lose"
            if computer == "Rock" and user == "Scissors":
                print("You lost! Rock beats Scissors")
            elif computer == "Paper" and user == "Rock":
                print("You lost! Paper beats Rock")
            elif computer == "Scissors" and user == "Paper":
                print("You lost! Scissors beats Paper")
    return outcome

def check_user_score(outcome, user_points):
    if outcome == "draw":
        user_points += 1
    elif outcome == "win":
        user_points += 2
    print("Your score = ", user_points)
    return user_points


def check_computer_score(outcome, computer_points):
    if outcome == "draw":
        computer_points += 1
    elif outcome == "lose":
        computer_points += 2
    print("Computer score = ", computer_points)
    return computer_points


def final_scores(user_points, computer_points):
    print("Final scores from the 3 games! \n You =", user_points, ", Computer =", computer_points)
    if user_points == computer_points:
        print("You drew!")
    elif user_points > computer_points:
        print("Yay, you won!")
    elif user_points < computer_points:
        print("Oh no, you lost!")


play_input = input("Do you want to play rock, paper, scissors against the computer? \n Y or N: ")
print("Best of 3: Win for 2 points, draw for 1 point and lose for 0 points.")
tries = 0
user_points = 0
computer_points = 0
while play_input == "Y":
    while tries < 3:
        user_action = user_selection()
        computer_action = computer_selection()
        print(user_action, "vs", computer_action)
        output_winner = check_winner(user_action, computer_action)
        user_points = check_user_score(output_winner, user_points)
        computer_points = check_computer_score(output_winner, computer_points)
        tries += 1
    final_scores(user_points, computer_points)
    play_input = input("Do you want to play rock, paper, scissors again? Y or N: ")