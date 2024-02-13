import json
from printFunctions import *

# Read parsed and scraped game data
gameDataFilename = "gameData.json"
with open(gameDataFilename, "r") as inFile:
    gameData = json.load(inFile)

# Transform, format, and write game data to text file
outputFilename = "gameData.txt"
with open(outputFilename, "w") as outFile:
    printTimestamp(outFile)
    outFile.write("\n[WINNER]\n")
    printWinner(gameData, outFile)
    outFile.write("\n[GAME MODE]\n")
    printGameMode(gameData, outFile)
    outFile.write("\n[SETTINGS]\n")
    settingCategories = ["expansions", "options", "multiplayer_options"]
    printSettings(gameData, settingCategories, outFile)
    outFile.write("\n[PLAYER DATA]\n")
    printPlayers(gameData, outFile)