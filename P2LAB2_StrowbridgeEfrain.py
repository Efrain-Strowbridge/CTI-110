# Efrain Strowbridge
# 9/23/26
# P2LAB2
# Using Dictionaries to store, retrieve, calculate, and display data

def main():
    # A dictionary of games and their average 100 percent completion runtimes in hours
    games = {"Minecraft":377, "Marvel's Spider-Man Remastered":45, "Hogwarts Legacy":250, "Super Mario Odyssey":85}

    # Get the keys from the dictionary
    games_keys = games.keys()

    # Display the available games to the user
    print()
    print("The following games available in the dictionary are:")
    print(*games_keys, sep=", ")
    print()

    # Prompt the user to enter a game name
    games_name = input("Enter a game name: ")

    # Retrieve the average runtime for the specified game from the dictionary
    games_run = games.get(games_name)

    # Check if the game exists in the dictionary and display the average runtime
    if games_name in games:
        print(f"The average 100 percent completion runtime for {games_name} is {games_run} hours long.")
        print()
        # Prompt the user to enter the number of hours they will dedicate to playing the game
        hours_played = input(f"Enter the number of hours you will dedicate to playing {games_name}: ")

        # Calculate the percentage of completion based on the hours played and the average runtime
        percent_complete = (int(hours_played) / games_run) * 100

        # Display the percentage of completion to the user
        if percent_complete >= 100:
            print(f"You should be 100% complete with {games_name} after {hours_played} hours of playtime. You will have completed the game!")
            print()
        else:
            print(f"You should be around {percent_complete:.2f}% complete with {games_name} after {hours_played} hours of playtime.")
            print()
    else:
        print("Game not found in the dictionary.")
        print()

main()