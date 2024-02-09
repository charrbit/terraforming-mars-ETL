from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json

endOfGameURL = "https://terraforming-mars.herokuapp.com/the-end?[...]"

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
playerStatSoup = soup.find(class_="game_end_table")

winner = winnerSoup.span.span.string

generations = generationSoup.h2.contents[1].strip()

playerStats = playerStatSoup.find_all("tr")[1:]
players = [list(player.stripped_strings) for player in playerStats]

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