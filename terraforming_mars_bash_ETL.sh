#! /bin/bash

# Path to GameSetupSpider that scrapes the Terraforming Mars new game setup page
# Scraped data will be saved as .jsonl
gameSetupSpider=$1

# Path to downloaded game setup source .html file
gameSetupSource=$2

# Path to EndOfGameSpider that scrapes the Terraforming Mars end of game page
# Scraped data will be saved in the same .jsonl file
endOfGameSpider=$3

# Path to downloaded end of game source .html file
endOfGameSource=$4

# Path to script that transforms the Spiders .jsonl output
transformScript=$5

# Path to directory where extracted and transformed data should be loaded
destination=$6

# Name of output file without an extension
# Transformed data will be saved as .txt
outputFilename=$7

# Extract
# Run scrapy spiders on source pages with desired information
scrapy runspider $gameSetupSpider -o $outputFilename.jsonl -a startURL=$gameSetupSource
scrapy runspider $endOfGameSpider -o $outputFilename.jsonl -a startURL=$endOfGameSource

# Transform
# Convert json format to a human-readable text output
python3 $transformScript $outputFilename.jsonl > $outputFilename.txt

# Load
mv $outputFilename.txt $destination
mv $outputFilename.jsonl $destination