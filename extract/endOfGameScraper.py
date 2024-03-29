from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json

endOfGameURL = "https://terraforming-mars.herokuapp.com/the-end?id=pe231633bd7a0"

with sync_playwright() as pw:
    # Go to URL and wait for dynamic content to finish loading
    browser = pw.firefox.launch()
    page = browser.new_page()
    page.goto(endOfGameURL)
    page.wait_for_load_state("networkidle")

    # Extract dynamically loaded HTML
    soup = BeautifulSoup(page.content(), features="html.parser")

# Parse HTML
winnerSoup = soup.find(class_="game-end-winer-announcement")
generationSoup = soup.find(class_="game_end_victory_points")
playerDataSoup = soup.find(class_="game_end_table")

winner = winnerSoup.span.span.string

generations = generationSoup.h2.contents[1].strip()

playerData = playerDataSoup.find_all("tr")[1:]
# Names of the values to be extracted
playerDataKeys = [
    "name",
    "corporation",
    "terraformer_rating",
    "milestone_points",
    "award_points",
    "greenery_points",
    "city_points",
    "victory_points",
    "escape_velocity_deduction",
    "final_score",
    "final_credits", 
    "playtime", 
    "actions_taken"]
playerDataValues = [list(player.stripped_strings) for player in playerData]
players = [dict(zip(playerDataKeys, playerValueList)) for playerValueList in playerDataValues]

# Read the settings used for this game
settingsFilename = "activeSettings.json"
with open(settingsFilename, "r") as inFile:
    gameData = json.load(inFile)

# Create JSON object with all game data
# (settings plus end of game stats)
gameData["winner"] = winner
gameData["generations_played"] = generations
gameData["players"] = players

# Save game data
gameDataFilename = "gameData.json"
with open(gameDataFilename, "w") as outFile:
    json.dump(gameData, outFile, indent=4)