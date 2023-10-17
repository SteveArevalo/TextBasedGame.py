# Steve Arevalo

current_room = 'Grand Foyer'
# Created a function to validate directions.
def directions(direction):
    valid_directions = ["north", "south", "east", "west"]
    return direction.lower() in valid_directions


# Function to display game instructions and information.
def show_instructions():
    print('** SPOOKY MANSION GAME **')
    print('Collect all 8 items to defeat Revenant and stop him from leaving the mansion.')
    print("Move commands: go south, go north, go east, go west")
    print("Add to Inventory: get 'item name'")
    print('-----------------------------------------')
    print(f'You are currently in the {current_room}')


# The main game function
def main():
    # Dictionary representing the rooms  and items in the mansion.
    rooms = {
        'Grand Foyer': {'south': 'Library', 'east': 'Dining Hall', 'Items': 'flashlight'},
        'Dining Hall': {'west': 'Grand Foyer', 'Items': 'recorder'},
        'Library': {'north': 'Grand Foyer', 'east': 'Bedroom', 'west': 'Seance Chamber', 'south': 'Locked Study', 'Items': 'old diary'},
        'Bedroom': {'north': 'Attic of Shadows', 'west': 'Library', 'Items': 'enchanted robe'},
        'Attic of Shadows': {'south': 'Bedroom', 'Items': "It's Revenant!"},
        'Seance Chamber': {'east': 'Library', 'south': 'Kitchen', 'Items': 'mirror of truth'},
        'Kitchen': {'north': 'Seance Chamber', 'Items': 'silver dagger'},
        'Conservatory': {'west': 'Locked Study', 'Items': 'skeleton key'},
        'Locked Study': {'north': 'Library', 'east': 'Conservatory', 'Items': 'talisman of protection'}
    }


    # Calls function to display the initial game instructions.
    show_instructions()

    current_room = 'Grand Foyer'

    #keep track of items the player needs to collect, the number of items collected, and a list of collected items
    items_to_collect = 8
    items_collected = 0
    collected_items = []

    # Start of the game loop. The game continues to run as long as the condition is True
    while True:
        print('Inventory:', collected_items) # Displays the items in the player's inventory.
        if 'Items' in rooms[current_room]: # Checks if the current room has items.
            items_in_room = rooms[current_room]['Items']
            if items_in_room:
                print(f'You see the {items_in_room}.')
                print('----------------------------')

        # User input for their next action and convert it to lowercase for consistency.
        action = input("What is your next move?").lower()
        print('-------------------------------')

        # If statements that handles player movement
        if action.startswith('go '):
            direction = action[3:]
            if directions(direction):
                if direction in rooms[current_room]:
                    current_room = rooms[current_room][direction]
                    print(f'You are in Revenant\'s {current_room}.')
                else:
                    print("You just ran into a wall. Please choose a valid direction.")
            else:
                print('Invalid direction. Please try again.')

        # Else if statement that handles item collection.
        elif action.startswith('get '):
            item_name = action[4:]
            if 'Items' in rooms[current_room] and item_name == rooms[current_room]['Items']:
                if item_name in collected_items:
                    print(f'You already collected the {item_name}.')
                else:
                    items_collected += 1 # If item collected add one to list.
                    rooms[current_room]['Items'] = None
                    collected_items.append(item_name)
                    print(f'You added the {item_name} to your inventory.')

                    # Remove the item line from the room's description.
                    if 'Items' in rooms[current_room]:
                        rooms[current_room]['Items'] = None

                    # If all 8 items collected user has won game.
                    if items_collected == items_to_collect:
                        print("Congratulations! You have collected all items and defeated Revenant!")
                        print("Thanks for playing the game. Hope you enjoyed it.")
                        break
            else:
                print(f'The {item_name} is not available in this room.')

        # If the player input does not match the expected 'go' or 'get' format,
        # it prompts them to use the correct format.
        else:
            print("Please use 'go' or 'get' before your command.")

        # Checks if the player entered the "Attic of Shadows." without collecting all 8 items
        # If so, they encounter Revenant, and the game is lost.
        if current_room == 'Attic of Shadows':
            print("You fool!. You found Revenant before collecting all 8 items! \nRevenant will now take over the world!!!!!")
            print("Thanks for playing the game. Better luck next time.")
            break


main()