import random

hand = {
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
    "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

win_conditions = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

def print_result(user_choice, computer_choice, result):
    print(f"{result}\nYou ({user_choice}): {hand[user_choice]}\nComputer ({computer_choice}): {hand[computer_choice]}")

def play_game():
    choices = ["rock", "paper", "scissors"]
    
    while True:
        computer_choice = random.choice(choices)
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        if user_choice == computer_choice:
            print_result(user_choice, computer_choice, "It's a tie!")
        elif win_conditions[user_choice] == computer_choice:
            print_result(user_choice, computer_choice, "You won!")
        else:
            print_result(user_choice, computer_choice, "You lost!")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
