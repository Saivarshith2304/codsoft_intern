import random
while(True):
    user_action = input("\nEnter a choice as 'rock', 'paper', 'scissors') or 'Exit': ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou choice is {user_action}, computer choice is {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
         if computer_action == "scissors":
             print("Rock smashes scissors! You win!")
         else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
         if computer_action == "rock":
            print("Paper covers rock! You win!")
         else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
         if computer_action == "paper":
             print("Scissors cuts paper! You win!")
         else:
            print("Rock smashes scissors! You lose.")
    elif user_action=="exit" or user_action=="EXIT":
         break