# Printing/Formatting helper functions
import datetime as dt

def printTimestamp(fs):
    fs.write(f"{dt.datetime.today().strftime('%m/%d/%Y')}\n")
    fs.write(f"{dt.datetime.today().strftime('%I:%M%p')}\n")

def printWinner(gameData, fs):
    fs.write(f"\t{gameData['winner'].upper()}\n")
    for player in gameData["players"]:
        fs.write(f"\t\t{player['name']} ({player['final_score']})\n")
    fs.write(f"\tgenerations_played: {gameData['generations_played']}\n")

def printGameMode(gameData, fs):
    fs.write(f"\tnumber_of_players: {gameData['number_of_players']}\n")
    fs.write(f"\tboard: {gameData['board']}\n")
    fs.write(f"\tstarting_corporations: {gameData['starting_corporations']}\n")

def printSettings(gameData, settingCategories, fs):
    for category in settingCategories:
        fs.write(f"\t{category}:\n")
        for setting in gameData[category]:
            fs.write(f"\t\t{setting}\n")

def printPlayers(gameData, fs):
    for player in gameData["players"]:
        printPlayer(player, fs)
    
def printPlayer(player, fs):
    fs.write(f"\t{player['name']}\n")
    fs.write(f"\t\tcorporation: {player['corporation']}\n")
    # Show the final score at the top of the list
    fs.write(f"\t\tfinal_score: {player.pop('final_score')}\n")
    # Extra formatting for the categories that sum to final_score
    for key, value in list(player.items())[2:-3]:
        fs.write(f"\t\t\t{key}: {value}\n")
    for key, value in list(player.items())[-3:]:
        fs.write(f"\t\t{key}: {value}\n")