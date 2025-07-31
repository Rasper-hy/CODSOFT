import random

def get_user_choice():
    print("\nChoose one: rock, paper, or scissors")
    choice = input("Your choice: ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose again.")
        choice = input("Your choice: ").lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user = get_user_choice()
        computer = get_computer_choice()

        print(f"\nYou chose: {user}")
        print(f"Computer chose: {computer}")

        result = decide_winner(user, computer)
        print("Result:", result)

        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

        print(f"\nScore -> You: {user_score} | Computer: {computer_score}")

        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break

# Run the game
play_game()