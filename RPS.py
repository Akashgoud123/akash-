import random

def get_user_choice():
    """Prompt the user to choose rock, paper, or scissors."""
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Your score: {user_score} | Computer's score: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Have a great day!")
            break

if __name__ == "__main__":
    main()


'''
output:
PS D:\akash internship> & C:/Users/akash/AppData/Local/Microsoft/WindowsApps/python3.12.exe "d:/akash internship/RPS.py"
Choose rock, paper, or scissors: rock

Your choice: rock
Computer's choice: scissors
You win!
Your score: 1 | Computer's score: 0
Do you want to play again? (yes/no): yes
Choose rock, paper, or scissors:
Invalid choice. Please enter 'rock', 'paper', or 'scissors'.
Choose rock, paper, or scissors: paper

Your choice: paper
Computer's choice: rock
You win!
Your score: 2 | Computer's score: 0
Do you want to play again? (yes/no): yes
Choose rock, paper, or scissors: scissors

Your choice: scissors
Computer's choice: paper
You win!'''