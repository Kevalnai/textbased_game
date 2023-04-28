#----------------------------------------------------------------------------
# Program Name: Milestone 1
# Created By  : KEVAL NAI
# Date:  19/03/2023
# ---------------------------------------------------------------------------
"""  In this game, the user is the player who will enter in responses to
prompts you give them.  The game will respond to the player’s inputs providing
feedback in the form of a story.  The adventure in this story is up to you to
create. Your program will ultimately include a continuous main loop constantly
receiving user input and providing output while using different functions based
on user input for processing.  """
# ---------------------------------------------------------------------------



# Define initial condition for the game
play_game = True

# Outer loop to replay the game
while play_game:

    # Introduction to the game
    print("\nWelcome to Escape the Island! You was on a solo sailing trip when your boat crashed onto a deserted island. You had limited supplies and knew you had to act fast if you wanted to make it out alive and survival skills to find a way back to civilization.\n")

    # Inner loop for gameplay
    while True:
        # Request user input
        user_input = input("\nWhat do you want to do? (explore/build/journey/fire/help/quit)\n ")

        # Check user input for validity
        if user_input.lower() not in ["explore", "build", "journey", "fire", "help", "quit"]:
            print("Invalid input. Please try again.")
            continue

        # If user chooses to explore
        if user_input.lower() == "explore":
            print(" As you explored the island, You discovered some old ruins and realized that the island may have been inhabited at one point. You started to investigate the ruins and eventually found a map hidden in a crevice. The map showed the location of a hidden boat on the other side of the island.")
     
        # If user chooses to build
        elif user_input.lower() == "build":
            print(" You quickly set up a shelter and started collecting food and water.")
        
        # If user chooses to journey
        elif user_input.lower() == "journey":
            print(" You journeyed across the rugged terrain, avoiding dangerous animals and treacherous cliffs. Finally, you reached the hidden boat and managed to get it working using his mechanical skills.")
       
        # If user chooses to start a fire
        elif user_input.lower() == "fire":
            print(" You find some dry leaves and use them to start a fire, providing warmth and a way to cook food.")
        
        # If user needs help
        elif user_input.lower() == "help":
            print(" You shout for help, hoping that someone will hear you and come to your rescue.")
        
        # If user chooses to quit the game
        elif user_input.lower() == "quit":
            print("\n Thanks for playing!")
            break
    
    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no) \n ")
    if play_again.lower() != "yes":
        play_game = False
