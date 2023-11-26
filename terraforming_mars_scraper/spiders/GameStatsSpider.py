import scrapy
            
class GameStatsSpider(scrapy.Spider):
    name = "gamestats"
    
    def start_requests(self):
        yield scrapy.Request(self.startURL, self.parse)

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

        # Player Game Statistics
        playerStats = []
        for player in response.css(".game_end_table tr")[1:]: # Exclude table header
            playerData = player.xpath("td//text()").getall()
            # Build a player stats object and add it to the list of player statistics
            playerStats.append({
                "name": playerData[0],
                "corporation": playerData[2],
                "terraformer_rating": playerData[3],
                "milestone_points": playerData[4],
                "award_points": playerData[5],
                "greenery_points": playerData[6],
                "city_points": playerData[7],
                "victory_points": playerData[8],
                "escape_velocity_penality": playerData[9],
                "total": playerData[10],
                "final_credits": playerData[11],
                "playtime": playerData[12],
                "actions_taken": playerData[13],
            })
        yield {
            "player_statistics": playerStats,
        }
        