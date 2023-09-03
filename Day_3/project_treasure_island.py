print('''
*******************************************************************************
           _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")
if direction == "left":
    action = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across\n")
    # action = "wait" or "swim"
    if action == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        if door == "red":
            print("It's a room full of fire. Game over!")
        elif door == "blue":
            print("You enter a room of beasts. Game over!")
        elif door == "yellow":
            print("You found the treasure! You are Winner!")
        else:
            print("You should to choose a red, or blue, or yellow colour. Try again!")
    elif action == "swim":
        print("You get attacked by an angry trout. Game over!")
elif direction == "right":
    print("You fell into a hole. Game over!")
else:
    print("You didn't choose any direction! Please start your game again!")