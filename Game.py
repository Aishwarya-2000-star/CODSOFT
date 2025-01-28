import random

def get_computer_choice():
    # Randomly select one of the choices for the computer
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    # Determine the winner based on the rules of Rock, Paper, Scissors
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def print_score(user_score, computer_score):
    print(f"\nCurrent Score:\nYou: {user_score} | Computer: {computer_score}")

def play_game():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors Game!")
    print("Choose 'rock', 'paper', or 'scissors'. Type 'quit' to stop playing.")

    while True:
        # Ask for the user's choice
        user_choice = input("\nEnter your choice: ").lower()

        if user_choice == "quit":
            print("Thanks for playing!")
            break
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice, please enter 'rock', 'paper', or 'scissors'.")
            continue
        
        # Get the computer's choice
        computer_choice = get_computer_choice()

        # Determine the winner
        result = determine_winner(user_choice, computer_choice)

        # Display choices and result
        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")
        
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("You lose this round!")
            computer_score += 1
        
        # Display the score
        print_score(user_score, computer_score)

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Run the game
play_game()
