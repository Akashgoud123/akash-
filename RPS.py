import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please try again!")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    score = {"user": 0, "computer": 0}
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "You win!":
            score["user"] += 1
        elif result == "You lose!":
            score["computer"] += 1
        print(f"Score - You: {score['user']}, Computer: {score['computer']}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

play_game()
