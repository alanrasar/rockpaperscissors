import random

continue_game = True
user_score = 0
computer_score = 0

while continue_game:
    user_input = input("Rock, paper, or scissors? (Type 'quit' to exit): ").lower()
    
    if user_input == 'quit':
        continue_game = False
        break
    
    if user_input not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")
        continue

    random_num = random.randint(1, 3)
    
    if random_num == 1:
        computer_answer = "rock"
    elif random_num == 2:
        computer_answer = "paper"
    else:
        computer_answer = "scissors"

    print(f"Computer chooses: {computer_answer}")

    if user_input == computer_answer:
        print("It's a tie!")
    elif (
        (user_input == 'rock' and computer_answer == 'scissors') or
        (user_input == 'paper' and computer_answer == 'rock') or
        (user_input == 'scissors' and computer_answer == 'paper')
    ):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

print(f"Final score - You: {user_score}, Computer: {computer_score}")
print("Thanks for playing!")
