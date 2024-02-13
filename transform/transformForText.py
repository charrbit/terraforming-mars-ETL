from printFunctions import *

def transformForText(gameData):
    printTimestamp()
    print() # newline
    print("[WINNER]") # section title
    printWinner(gameData) # section values
    print()
    print("[GAME MODE]")
    printGameMode(gameData)
    print()
    print("[SETTINGS]")
    settingCategories = ["expansions", "options", "multiplayer_options"]
    printSettings(gameData, settingCategories)
    print()
    print("[PLAYER DATA]")
    printPlayers(gameData)