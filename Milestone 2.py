#-------------------------------------------------------------------------------
# Program Name: Milestone 2
# Created By  : KEVAL NAI
# Date:  06/04/2023
# ------------------------------------------------------------------------------
"""  Your program should use a data structure to store the game world’s data.
The best structure for this would be a dictionary of dictionaries. The outer
dictionary is set of decision points with each decision point being its own
dictionary. The nature of your game’s decision points will be based on the kind
of game you are creating. The following are some examples to give you food for 
thought about what your decision points can be and what data those decision
points will store.
  """
# ------------------------------------------------------------------------------


# Define decision points
decision_points = {
    "start": {
        "description": "You find yourself on a deserted island with nothing but the clothes on your back. \n\nWhat do you do?",
        "options": {
            "explore": {
                "description": "You decide to explore the island to see what resources are available.",
                "next_decision_point": "explore"
            },
            "build": {
                "description": "You decide to build a shelter to protect yourself from the elements.",
                "next_decision_point": "build"
            }
        }
    },
    "explore": {
        "description": "You come across a cave. Do you want to enter or keep exploring?",
        "options": {
            "enter": {
                "description": "You decide to enter the cave.",
                "next_decision_point": "cave"
            },
            "keep exploring": {
                "description": "You decide to keep exploring the island.",
                "next_decision_point": "explore_2"
            }
        }
    },
    "cave": {
        "description": "You find a treasure chest. Do you want to open it or leave it?",
        "options": {
            "open": {
                "description": "You decide to open the chest. Inside, you find a map that leads to a hidden boat on the other side of the island.",
                "next_decision_point": "end"
            },
            "leave": {
                "description": "You decide to leave the chest and continue exploring the island.",
                "next_decision_point": "explore_2"
            }
        }
    },
    "explore_2": {
        "description": "You come across a river. Do you try to cross it or follow it?",
        "options": {
            "cross": {
                "description": "You decide to try to cross the river. Unfortunately, you slip and get swept away by the current.",
                "next_decision_point": "end"
            },
            "follow": {
                "description": "You decide to follow the river. After a while, you come across a fishing village where you are able to signal for help and get rescued.",
                "next_decision_point": "end"
            }
        }
    },
    "build": {
        "description": "You start building a shelter. Do you focus on building a sturdy shelter or collecting resources?",
        "options": {
            "sturdy shelter": {
                "description": "You focus on building a sturdy shelter. After a few days, you finish your shelter and begin to collect resources.",
                "next_decision_point": "collect resources"
            },
            "collect resources": {
                "description": "You decide to focus on collecting resources. After a few days, you have enough supplies to build a decent shelter.",
                "next_decision_point": "build_2"
            }
        }
    },
    "build_2": {
        "description": "You have built a shelter and collected some resources. What do you do next?",
        "options": {
            "explore": {
                "description": "You decide to explore the island to see what other resources are available.",
                "next_decision_point": "explore"
            },
            "signal for help": {
                "description": "You build a signal fire to try to attract the attention of any passing ships or planes.",
                "next_decision_point": "end"
            }
        }
    },
    "end": {
        "description": "Congratulations, you have escaped the island!",
        "options": {}
    }
}

# Define player character data
player_character = {
    "name": input("What's your name? "),
    "current_decision_point": "start"
}

# Main gameplay loop
while True:
    current_point = decision_points[player_character["current_decision_point"]]
    
    # Print the description for the current decision point
    print(current_point["description"])
    
    # Print the options available at the current decision point
    for option_key, option_value in current_point["options"].items():
        print(f"Option {option_key}: {option_value['description']}")
    
    # Get player input and update the player's current decision point
    player_input = input("\nWhat do you choose? ")
    if player_input in current_point["options"].keys():
        player_character["current_decision_point"] = current_point["options"][player_input]["next_decision_point"]
    else:
        print("Invalid input, try again.")
    
    # Check if the player has reached a terminal point and end the game if so
    if not decision_points[player_character["current_decision_point"]]["options"]:
        print(decision_points[player_character["current_decision_point"]]["description"])
        break
