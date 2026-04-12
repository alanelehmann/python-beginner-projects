import random

def get_computer_choice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)
    
def get_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"
        
player_score = 0
computer_score = 0

print("Rock Paper Scissors!")
print("First to 3 wins.  Type rock, paper, or scissors.")

while player_score < 3 and computer_score < 3:
    player_choice = input("\nYour choice: ").lower()
    
    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Type rock, paper, or scissors.")
        continue
        
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    result = get_winner(player_choice, computer_choice)
    
    if result == "tie":
        print("It's a tie!")
    elif result == "player":
        player_score += 1
        print(f"You win this round! Score - You: {player_score} | Computer: {computer_score}")
    else:
        computer_score += 1
        print(f"Computer wins this round! Score - You: {player_score} | Computer: {computer_score}")
        
if player_score == 3:
    print("\nYou won the game!  Yaay oh my gosh im screaming and crying rn!")
else:
    print("\nComputer won the game! Better luck next time.")
        