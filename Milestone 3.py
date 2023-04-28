#-------------------------------------------------------------------------------
# Program Name: Milestone 3
# Created By  : KEVAL NAI
# Date:  23/04/2023
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



def start():
    print("Recently you just went into the cave and found a map of the island. ")
    print("PRESS 1 : To escape the island by using the map.")
    print("PRESS 2 : To find the treasure of the island by the map given on the back of map.\n ")

def combat():
    hp = 200
    fight = 100
    if hp > fight:
        print("You won the previous level.\n")
    else:
        print("You lose it.")
        
def animal():
    hp = int(input("Enter you hp (Less the 200):"))
    if hp < 200:
        print("Yes you can fight.")
    else:
        print("Your Adreline dose is too high.")
        print("you lose it.")
        
def venom():
    hp = 0
    if hp == 0:
        print("You are infacted. ")

def choose_path():
    path = ""
    while path != "1" and path != "2":
        path=input("What do you wanna do? (Press 1 :- Escape/ Press 2 :- Treasure)\n")
        if path == "1":
            print("Now you have to head towards a mountain which is situated in the center of the island.")
            escape()
        elif path == "2":
            print("For finding the treaure you have to deal with various types of difficulties and player may lose thier lives also!! ")
            treasure()

def escape():
    # Define decision points
    decision_points = {
    "start": {
        "description": "For escaping you have two ways terrain way or forest way. \n\nWhat do you do?",
        "options": {
            "terrain way": {
                "description": "You decide to go by the terrain way.",
                "next_decision_point": "mountain"
            },
            "forest way": {
                "description": "You decide to go through forest.",
                "next_decision_point": "forest"
            }
        }
    },
    "mountain": {
        "description": "You come across a mountain. Do you want to climb it or pass by sides?",
        "options": {
            "climb it": {
                "description": "You decide to climb the mountain.",
                "next_decision_point": "fight"
            },
            "pass by": {
                "description": "You decide to pass by sides.",
                "next_decision_point": "return"
            }
        }
    },
    "fight": {
        "description": "Here you find the king of the island fight with him and win to escape or be a slave of him. Do you want to fight or be a slave?",
        "options": {
            "fight": {
                "description": "You fought well and you won the match not you can have access to the assets of king which also have a hot air balloon.",
                "next_decision_point":"balloon"
            },
            "slave": {
                "description": "You become slave of king now you never escape without his permission.",
                "next_decision_point": "end"
            }
        }
    },
    "return": {
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
    "forest": {
        "description": "You are in the middle of the forest and came across an animal. Do you kill with it or save you life by going back?",
        "options": {
            "kill": {
                "description": "You finally kill it bt your health is low.",
                "next_decision_point":"end"
            },
            "back": {
                "description": "You choose another way.",
                "next_decision_point": "return"
            }
        }
    },
    "balloon": {
        "description": "You have balloon but now resources to fly it. What do you do next?",
        "options": {
            "find woods": {
                "description": "You decide to explore the island to see what other resources are available.",
                "next_decision_point": "end"
            },
            "go ahead": {
                "description": "choosing the passing way.",
                "next_decision_point": "return"
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
    

def treasure():
    # Define decision points
    decision_points = {
    "start": {
        "description": "For escaping you have two ways desert way or forest way. \n\nWhat do you do?",
        "options": {
            "desert": {
                "description": "You decide to go by the dessert.",
                "next_decision_point": "desert"
            },
            "forest": {
                "description": "You decide to go through forest.",
                "next_decision_point": "forest"
            }
        }
    },
    "desert": {
        "description": "You come across a desert. Do you want to cross it or back to forest?",
        "options": {
            "cross it": {
                "description": "You decide to cross the desert.",
                "next_decision_point": "mirage"
            },
            "back": {
                "description": "You decide to pass by sides.",
                "next_decision_point": "forest"
            }
        }
    },
    "mirage": {
        "description": "you are thristy and you saw a water body follow it for water or head towards sand dunes. Do you want to follow water or sand dunes?",
        "options": {
            "water": {
                "description": "You lost the way and end up losing your health.",
                "next_decision_point": "end"
            },
            "sand dunes": {
                "description": "You reached to sand dunes now you have two option go to cactus valley or main route.",
                "next_decision_point": "next"
            }
        }
    },
    "return": {
        "description": "You come across a river. Do you try to cross it or follow it?",
        "options": {
            "cross": {
                "description": "You decide to try to cross the river.Now kill the gaurd to get treasure.",
                "next_decision_point": "end"
            },
            "follow": {
                "description": "You decide to follow the river. After a while, you come across a fishing village where you are able to signal for help and get rescued.",
                "next_decision_point": "end"
            }
        }
    },
    "forest": {
        "description": "You are in the middle of the forest and came across an animal. Do you kill with it or save you life by going back?",
        "options": {
            "kill": {
                "description": "You cannat defeat him.",
                "next_decision_point": "end"
            },
            "back": {
                "description": "You choose another way.",
                "next_decision_point": "return"
            }
        }
    },
    "next": {
        "description": "You have main route go by it kill the gaurd and you will get treasure or go through posinous cactus valley. What do you do next?",
        "options": {
            "main route": {
                "description": "You killed that gaurd and now dig at the cross to get treasure.",
                "next_decision_point": "end"
            },
            "cactus valley": {
                "description": "be safe you will get killed if you do not take proper care.",
                "next_decision_point": "end"
            }
        }
    },
    "end": {
        "description": "OOPS! , you died better luck next time",
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
start()
combat()
animal()
venom()
choose_path()
