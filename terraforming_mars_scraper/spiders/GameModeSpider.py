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

        # Expansions Used
        expansionCategory = gameSettingCategories[1]
        expansions = [expansion.attrib["name"] for expansion in expansionCategory.css("input[checked]")]
        yield {
            "expansions": expansions,
        }

        # Board
        boardCategory = gameSettingCategories[2]
        yield {
            "board": boardCategory.css("input[checked]").attrib["value"],
        }