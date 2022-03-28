from data import racers
from replit import clear
from art import logo, stage_art
import random

print(logo)
print("""Pick a game mode
1 - Guess driver's number
2 - Guess driver's manufacturer
3 - Guess driver's crew chief""")

# Choosing a game mode
game_mode = int(input("Type 1, 2 or 3: "))

# Initial variable
game_is_on = True
stage = 1
points = 0
msg = ""

# Main game logic
while game_is_on:

    # Clear console, print message, stage, art
    clear()
    print(msg)
    print(stage_art[stage - 1])
    print(f"Stage {stage}/10")

    # Pick a guess
    racer = random.choice(list(racers.items()))

    # Playing the first game mode
    if game_mode == 1:
        # Getting user's input
        users_input = int(input(f"Number of {racer[0]}: #"))
        
        # If the input is correct, add point and display message
        if users_input == racer[1]["number"]:
            msg = "Correct! +1 point"
            points += 1
        else:
            msg = f"Not correct. The number is {racer[1]['number']}"

    # Playing the second game mode
    elif game_mode == 2:
        users_input = input(f"Manufacturer of {racer[0]}: ")
        
        if users_input == racer[1]["manufacturer"]:
            msg = "Correct! +1 point"
            points += 1
        else:
            msg = f"Not correct. The manufacturer is {racer[1]['manufacturer']}"

    # Playing the third game mode
    elif game_mode == 3:
        users_input = input(f"Crew chief of {racer[0]}: ")
        
        if users_input == racer[1]["chief"]:
            msg = "Correct! +1 point"
            points += 1
        else:
            msg = f"Not correct. The crew chief is {racer[1]['chief']}"

    stage += 1

    # Game over when stage reaches 10, display the result
    if stage > 10:
        clear()
        print(msg)
        print(logo)
        print(f"Game over. Your score is {points}/10")
        game_is_on = False