import random

choices = ["rock", "paper", "scissors"]
emoji = {
    "rock": "✊",
    "paper": "✋",
    "scissors": "✌️"
}

while True:
    user_choice = input("Enter your choice from (Rock ✊, Paper ✋, Scissors ✌️): ").lower()
    if user_choice not in choices:
        print("Invalid choice, Please Try Again !!")
    else:
        computer_choice = random.choice(choices)
        if user_choice == "rock":
            if computer_choice == "rock":
                print(f"Computer also chose Rock {emoji['rock']}, It's a Tie !!")
            elif computer_choice == "paper":
                print(f"Computer chose Paper {emoji['paper']}, Computer Wins !!")
            else:
                print(f"Computer chose Scissors {emoji['scissors']}, You win !!")

        elif user_choice == "paper":
            if computer_choice == "rock":
                print(f"Computer chose Rock {emoji['rock']}, You win !!")
            elif computer_choice == "paper":
                print(f"Computer also chose Paper {emoji['paper']}, It's a Tie !!")
            else:
                print(f"Computer chose Scissors {emoji['scissors']}, Computer Wins !!")      
        
        else:
            if computer_choice == "rock":
                print(f"Computer chose Rock {emoji['rock']}, Computer Wins !!")
            elif computer_choice == "paper":
                print(f"Computer chose Paper {emoji['paper']}, You win !!")
            else:
                print(f"Computer also chose Scissors {emoji['scissors']}, It's a Tie !!")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for playing! Goodbye!")
        break
