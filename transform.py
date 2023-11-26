import sys
import json
import datetime as dt

pathToGameData = sys.argv[1]

# Load scraped terraforming mars game data
with open(pathToGameData, 'r') as jsonInFile:
    gameData = [json.loads(line) for line in jsonInFile]

def printTimestamp():
    print(dt.datetime.today().strftime("%m/%d/%Y"))
    print(f"{dt.datetime.today().strftime('%I:%M%p')}\n")

def printGameMode():
    numPlayers, startingCorporations, board, = gameData[0], gameData[2], gameData[3]
    print("GAME MODE:")
    print(f"\tnumber_of_players: {numPlayers['number_of_players']}")
    print(f"\tboard: {board['board']}")
    print(f"\tstarting_corporations: {startingCorporations['starting_corporations']}")
    # Extract all loopable game settings from the game data
    for gameSettingCategory in gameData[4:7]:
        print(f"\t{list(gameSettingCategory.keys())[0]}:") # Print the setting category name
        for setting in list(gameSettingCategory.values())[0]:
            print(f"\t\t{setting}")
    print()

def printWinner():
    winner, generationsPlayed = gameData[7], gameData[8]
    print(f"[WINNER] {winner['winner']}\n")
    print(f"generations_played: {generationsPlayed['generations_played']}\n")

def printPlayers():
    playerStats = gameData[9]
    for player in playerStats["player_statistics"]:
        # Print and remove player name from player dictionary
        print(player.pop("name"))
        print(f"\tcorporation: {player.pop('corporation')}")
        print(f"\ttotal: {player.pop('total')}")
        # Extract and remove specified statistics for printing after the loop
        # This is to achieve the desired output without having to manually print every statistic
        credits, playtime, actions = player.pop("final_credits"), player.pop("playtime"), player.pop("actions_taken")
        for stat, value in player.items():
            print(f"\t\t{stat}: {value}")
        print(f"\tfinal_credits: {credits}")
        print(f"\tactions_taken: {actions}")
        print(f"\tplaytime: {playtime}\n")

# Generate transformed (formatted) output
printTimestamp()
printGameMode()
printWinner()
printPlayers()