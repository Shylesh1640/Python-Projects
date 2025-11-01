import random

user_score = 0
computer_score = 0

while True:
    user_input  = input("Enter rock, paper, scissors or Q to stop playing: ").lower()
    if user_input == 'q':
        break
    if user_input not  in ['rock','paper','scissors']:
        continue
    random_number = random.randint(0,2)
    if random_number == 0:
        computer_choice = 'rock'
    elif random_number == 1:
        computer_choice = 'paper'
    else:
        computer_choice = 'scissors'
        
    print("Computer chose:", computer_choice)
    if user_input == computer_choice:
        print("It's a tie!")
    elif (user_input == 'rock' and computer_choice == 'scissors') or (user_input == 'paper' and computer_choice == 'rock') or (user_input == 'scissors' and computer_choice == 'paper'):
            print("you win")
            user_score += 1
    else:
        print("computer wins")
        computer_score += 1
        
print("Final Scores - You:", user_score, "Computer:", computer_score)
                
    
print("Thanks for playing")
    
    
        