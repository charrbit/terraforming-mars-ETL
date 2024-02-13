# Printing/Formatting helper functions
import datetime as dt

def printTimestamp():
    print(dt.datetime.today().strftime("%m/%d/%Y"))
    print(dt.datetime.today().strftime('%I:%M%p'))

def printWinner(gameData):
    print(f"\t{gameData['winner'].upper()}")
    for player in gameData["players"]:
        print(f"\t\t{player['name']} ({player['final_score']})")
    print(f"\tgenerations_played: {gameData['generations_played']}")

def printGameMode(gameData):
    print(f"\tnumber_of_players: {gameData['number_of_players']}")
    print(f"\tboard: {gameData['board']}")
    print(f"\tstarting_corporations: {gameData['starting_corporations']}")

def printSettings(gameData, settingCategories):
    for category in settingCategories:
        print(f"\t{category}:")
        for setting in gameData[category]:
            print(f"\t\t{setting}")

def printPlayers(gameData):
    for player in gameData["players"]:
        printPlayer(player)
    
def printPlayer(player):
    print(f"\t{player['name']}")
    print(f"\t\tcorporation: {player['corporation']}")
    # Show the final score at the top of the list
    print(f"\t\tfinal_score: {player.pop('final_score')}")
    # Extra formatting for the categories that sum to final_score
    for key, value in list(player.items())[2:-3]:
        print(f"\t\t\t{key}: {value}")
    for key, value in list(player.items())[-3:]:
        print(f"\t\t{key}: {value}")