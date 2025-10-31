import random

top_of_range = input("Type a number:")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <=0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()
    
random_number = random.randint(0, top_of_range)

# This is just for debugging, you'll want to remove it for the actual game.
print("The random number is", random_number) 