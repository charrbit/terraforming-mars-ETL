import scrapy
            
class GameStatsSpider(scrapy.Spider):
    name = "gamestats"
    start_urls = [
        "file:///home/astrobits/Code/github/terraforming-mars-scraper/samplePage.html",
    ]

    def parse(self, response):
        # Winner
        winner = response.css(".game-end-winer-announcement")
        yield {
            "winner": winner.xpath("span//text()").get(),
        }

        # Number of Generations (length of the game)
        generationsPlayed = response.css(".game_end_victory_points")
        yield {
            "generations_played": generationsPlayed.xpath("h2//text()").getall()[1].strip(),
        }

        # Player
        # Exclude the table header
        for player in response.css(".game_end_table tr")[1:]:
            playerData = player.xpath("td//text()").getall()
            del(playerData[1]) # Remove empty string element
            yield {
                "name": playerData[0],
                "corporation": playerData[1],
                "terraformer_rating": playerData[2],
                "milestone_points": playerData[3],
                "award_points": playerData[4],
                "greenery_points": playerData[5],
                "city_points": playerData[6],
                "victory_points": playerData[7],
                "escape_velocity_penality": playerData[8],
                "total": playerData[9],
                "final_credits": playerData[10],
                "playtime": playerData[11],
                "actions_taken": playerData[12],
            }
        