import json
from transformForText import transformToText

# Read terraforming mars game data
gameDataFilename = "gameData.json"
with open(gameDataFilename, 'r') as inFile:
    gameData = json.load(inFile)

# Transform game data for human-readable text output
# (Redirect standard output to load to destination .txt file)
transformToText(gameData)