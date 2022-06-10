
#Importing random for cpu selection
import random

# Brief game information 
print("welcome to the Game")
print("R = Rock", "P = Paper", "S = scissors")

while True:
    game_options = ["R", "P", "S"]
    
    CPU = random.choice(game_options) #To initiate the ramdom select for computer
    playerOption = input("Enter either R, P, S: ")
    player_option = playerOption.upper()

    # To validate player's entry
    while player_option not in game_options:
        print("Error!, try again.")
        break

    # To compare player's entry and computer entry 
    if player_option == CPU:
        print("player: ", player_option)
        print("computer: ", CPU)
        print("it's a Tie!")

    elif player_option == "R":
        if CPU == "P":
            print("player: ", player_option)
            print("computer: ", CPU)
            print("You Lose")
        if CPU == "S":
            print("player: ", player_option)
            print("computer: ", CPU)
            print("you Win")

    elif player_option == "P":
        if CPU == "S":
            print("player: ", player_option)
            print("computer: ", CPU)
            print("You Lose")
        if CPU == "R":
            print("player: ", player_option)
            print("computer: ", CPU)
            print("you Win")

    elif player_option == "S":
        if CPU == "R":
            print("player: ", player_option)
            print("computer: ", CPU)
            print("You Lose")
        if CPU == "P":
            print("player: ", player_option)
            print("computer: ", CPU)
            print("you Win")        
    
    # To request if the player will love to try again
    playAgain = input("Do want to try again? Yes/No: ")
    play_again = playAgain.lower()

    if play_again != "yes":
        break

print("See you again, Bye.")
