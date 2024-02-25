# ask user for input (player_choice)


player_choice = input("Enter rock, paper or scissor: ")
choice = {"rock", "paper", "scissors"}
computer_choice = random.choice()


def main():
    if player_choice == computer_generate:
        print("Draw!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("You lose!")
