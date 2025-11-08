import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val, max_val)
    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2<=players<=4:
            break
        else:
            print("Must be between 2 - 4 players")
    else:
        print("Invalid, try again")
        
max_score = 50
players_scores = [0 for _ in range(players)]

while max(players_scores)<max_score:
    print("\n--- New Round ---")
    for player_idx in range(players):
        print(f"\n--- Player {player_idx + 1}'s Turn ---")
        print(f"Your total score is: {players_scores[player_idx]}")
        current_score =0
        
        while True:
            should_roll = input("Would you like to roll? (y/n): ").lower()
            if should_roll != 'y':
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Your turn is done and you lose your points for this round.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a: {value}")
            
            print(f"Your score this turn is: {current_score}")

        players_scores[player_idx] += current_score
        print(f"Your total score is now: {players_scores[player_idx]}")

        if players_scores[player_idx] >= max_score:
            break 
    else:
        continue
    break

max_final_score = max(players_scores)
winning_player_idx = players_scores.index(max_final_score)
print(f"\n--- Game Over! ---")
print(f"Player {winning_player_idx + 1} is the winner with a score of {max_final_score}!")
