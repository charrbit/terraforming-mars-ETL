import scrapy
            
class GameModeSpider(scrapy.Spider):
    name = "gamemode"
    start_urls = [
        "file:///home/astrobits/Code/github/terraforming-mars-scraper/samplePage.html",
    ]

    def parse(self, response):
        gameSettingCategories = response.css("div.create-game-page-column")

        # Number of Players
        playerCategory = gameSettingCategories[0]
        yield {
            "number_of_players": playerCategory.css("input[checked]").attrib["value"],
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

        # Expansions Used
        expansionCategory = gameSettingCategories[1]
        expansions = []
        for expansion in expansionCategory.css("input[checked]"):
            inputID = expansion.attrib["id"]
            label = expansionCategory.css(f"label[for='{inputID}']")
            expansions.append(label.xpath("span//text()").get())
        yield {
            "expansions": expansions,
        }

        # Special Options
        optionCategory = gameSettingCategories[3]
        options = []
        for option in optionCategory.css("input[checked]"):
            inputID = option.attrib["id"]
            label = optionCategory.css(f"label[for='{inputID}']")
            options.append(label.xpath("span//text()").get())
        yield {
            "options": options,
        }

        # Multiplayer Options
        mpOptionCategory = gameSettingCategories[4]
        options = []
        for option in mpOptionCategory.css("input[checked]"):
            inputID = option.attrib["id"]
            label = mpOptionCategory.css(f"label[for='{inputID}']")
            options.append(label.xpath("span//text()").get())
        yield {
            "multiplayer_options": options,
        }