#! /bin/bash

destinationDirectory=$1

# Extract
# Parse JSON object containing the settings used during the game
python3 extract/settingsParser.py

# Scrape game data from URL using playwright and beautifulsoup
python3 extract/endOfGameScraper.py

# Transform
# Transform extracted data to a human-readable formatted .txt file
python3 transform/transformForText.py

# Load
# Move transformed data to destination directory
bash load/loadText.sh $(date '+%m%d%y') $destinationDirectory