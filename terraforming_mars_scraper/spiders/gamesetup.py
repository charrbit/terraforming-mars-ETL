import scrapy
            
class GameSetupSpider(scrapy.Spider):
    name = "gamesetup"
    
    def start_requests(self):
        yield scrapy.Request(f"file://{self.startURL}", self.parse)

    def parse(self, response):
        gameSettingCategories = response.css("div.create-game-page-column")

        # Number of Players
        playerCategory = gameSettingCategories[0]
        yield {
            "number_of_players": playerCategory.css("input[checked]").attrib["value"],
        }

        # Players
        players = []
        for player in response.css("div.columns > div"):
            name = player.css("input.create-game-player-name").attrib["value"].title()
            color = player.css("div.create-game-page-color-row input[checked]").attrib["value"].title()
            # Build a player object and add it to the list of players
            players.append({"name": name, "color": color})
        yield {
            "players": players,
        }

        # Number of Starting Corporations
        optionCategory = gameSettingCategories[3]
        startingCorporations = optionCategory.xpath("label//input").attrib["value"]
        yield {
            "starting_corporations": startingCorporations,
        }

        # Board
        boardCategory = gameSettingCategories[2]
        yield {
            "board": boardCategory.css("input[checked]").attrib["value"].title(),
        }

        # Specify the game settings that can be looped over (Expansions, Options, Multiplayer Options)
        gameSettingIndices = [1, 3, 4]
        for index in gameSettingIndices:
            gameSettingCategory = gameSettingCategories[index]
            settingTitle = gameSettingCategory.xpath("h4//text()").get().replace(" ", "_").lower()
            settings = []
            # Add each user-selected setting to the settings list for this specific setting category
            for setting in gameSettingCategory.css("input[checked]"):
                # Find the label associated with the input element and parse its data
                inputID = setting.attrib["id"]
                label = gameSettingCategory.css(f"label[for='{inputID}']")
                settings.append(label.xpath("span//text()").get().title())
            yield {
                settingTitle: settings,
            }