import random

choices =  ["rock", "paper", "scissors"]

human_score = 0
computer_score = 0

print("Let the battle begin! It's You vs. Computer — first to reach 5 points claims victory!")


while human_score < 5 and computer_score < 5:
    human_choice = input("Your move! Choose wisely: rock, paper , or scissors ").lower()

    if human_choice not in choices:
        print("Invalid choice. Try again.")
        continue

    computer_choice = random.choice(choices)

    print(f"You chose {human_choice}")
    print(f"Computer chose {computer_choice}")

    if (human_choice == computer_choice):
        print("It's a tie! Great minds think alike.")
    elif (
        (human_choice == "rock" and computer_choice == "scissors") or
        (human_choice == "scissors" and computer_choice == "paper") or
        (human_choice == "paper" and computer_choice == "rock")
    ) :
        print("You win this round! Well played.")
        human_score += 1
    else:
        print("Computer takes this one. Stay sharp!")
        computer_score += 1
    
    print(f"Score: You {human_score} - {computer_score} Computer")


print("Game Over!")
if human_score == 5:
    print("You reached 5 points first and claimed the crown!")
else:
    print("The Computer outplayed you this time...")






