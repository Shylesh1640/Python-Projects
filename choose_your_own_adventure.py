name = input("Enter your name:")
print("Welcome", name, "to this adventure!")
answer = input("You are in a dark room. There is a door to your right and left. Which one do you take? (right/left) ")
if answer == "left":
    answer = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: ")
    if answer == "wait":
        answer = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
        if answer == "red":
            print("It's a room full of fire. Game Over.")
        elif answer == "yellow":
            print("You found the treasure! You Win!")
        elif answer == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
    