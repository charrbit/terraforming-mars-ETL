import scrapy

# Website element structure
# .game_end_victory_points
    # .table .game_end_table
        # .player_translucent_bg_color_playerColor
            
class GameStatsSpider(scrapy.Spider):
    name = "gamestats"
    start_urls = [
        "file:///home/astrobits/Code/github/terraforming-mars-scraper/samplePage.html",
    ]

    def parse(self, response):
        pass
        