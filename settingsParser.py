import json

# Read downloaded game settings
settingsFilename = "tm_settings.json"
with open(settingsFilename, "r") as inFile:
    settings = json.load(inFile)

# Parse game settings dictionary
# Expansions
supportedExpansions = ["corporateEra", 
                        "prelude",
                        "prelude2Expansion",
                        "venusNext",
                        "colonies",
                        "turmoil",
                        "promoCardsOption"]
activeExpansions = [expansion for expansion in supportedExpansions if settings[expansion] == True]

# Options
supportedOptions = ["solarPhaseOption",
                    "undoOption",
                    "showTimers",
                    "escapeVelocityMode",
                    "shuffleMapOption"]
activeOptions = [option for option in supportedOptions if settings[option] == True]

# Multiplayer Options
supportedMultiplayerOptions = ["draftVariant",
                                "initialDraft",
                                "randomFirstPlayer",
                                "randomMA",
                                "showOtherPlayersVP",
                                "fastModeOption"]
activeMultiplayerOptions = [option for option in supportedMultiplayerOptions if settings[option] == True]

# Create active game settings dictionary
gameSettings = dict(
    seed = settings["seed"],
    number_of_players = len(settings["players"]),
    board = settings["board"],
    expansions = activeExpansions,
    starting_corporations = settings["startingCorporations"],
    options = activeOptions,
    multiplayer_options = activeMultiplayerOptions
)

# Save active game settings
outputFilename = "activeSettings.json"
with open(outputFilename, "w") as outFile:
    json.dump(gameSettings, outFile, indent=4)