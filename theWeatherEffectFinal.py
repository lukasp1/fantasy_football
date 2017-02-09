import nflgame

totalColdRushes = 0
totalColdYards = 0
totalColdGames = 0

totalChillyRushes = 0
totalChillyYards = 0
totalChillyGames = 0

totalMediumRushes = 0
totalMediumYards = 0
totalMediumGames = 0

totalWarmRushes = 0
totalWarmYards = 0
totalWarmGames = 0

totalHotRushes = 0
totalHotYards = 0
totalHotGames = 0


totalSnowRushes = 0
totalSnowRushYards = 0
totalSnowGames = 0

totalRainRushes = 0
totalRainRushYards = 0
totalRainGames = 0

totalWindRushes = 0
totalWindRushYards = 0
totalWindGames = 0

totalPartlyCloudyDayRushes = 0
totalPartlyCloudyDayRushYards = 0
totalPartlyCloudyDayGames = 0

totalPartlyCloudyNightRushes = 0
totalPartlyCloudyNightRushYards = 0
totalPartlyCloudyNightGames = 0

totalCloudyRushes = 0
totalCloudyRushYards = 0
totalCloudyGames = 0

totalFogRushes = 0
totalFogRushYards = 0
totalFogGames = 0

totalNormalRushes = 0
totalNormalRushYards = 0
totalNormalGames = 0

currentWeekLocations = dict()
currentGameTemp = dict()
currentGameWeatherCondition = dict()


currentWeekLocationAndTemperatures = dict()
currentWeekLocationAndWeatherCondition = dict()


with open('weatherCollection.txt') as f:
	content = f.readlines()
# initialize a dictionary that holds all temperatures and 
count = 1
for current in content:
	currentWeekLocations[count] = str(current[29:32])
	print currentWeekLocations[count] + "j"
	count+=1
count = 1	
for current in content:
	
		
	currentGameTemp[count] = current[13:15]
	
	
	
	
	
	if "snow" in current:
		currentGameWeatherCondition[count] = str(current[71:77])
	elif "partly-cloudy-day" in current:
		currentGameWeatherCondition[count] = str(current[71:89])
	elif "rain" in current:
		currentGameWeatherCondition[count] = str(current[71:77])
	elif "partly-cloudy-night" in current:
		currentGameWeatherCondition[count] = str(current[71:92])
	elif "cloudy" in current:
		currentGameWeatherCondition[count] = str(current[71:79])
	elif "wind" in current:
		currentGameWeatherCondition[count] = str(current[71:77])
	elif "fog" in current:
		currentGameWeatherCondition[count] = str(current[71:76])
	elif "clear-day" in current:
		currentGameWeatherCondition[count] = str(current[71:82])
	if current == "\n":
		currentGameTemp[count] = 0
		currentGameWeatherCondition[count] = 0
	count += 1
for i in currentGameTemp:
	currentGameTemp[i] = int(currentGameTemp[i])
for i in currentGameWeatherCondition:
	print currentGameWeatherCondition[i], "j"

currentGame = 1
for year in range(2009, 2015):
	for week in range(1, 18):
		while not content[currentGame] == '\n':
			currentWeekLocationAndTemperatures[currentWeekLocations[currentGame]] = currentGameTemp[currentGame]
			currentWeekLocationAndWeatherCondition[currentWeekLocations[currentGame]] = currentGameWeatherCondition[currentGame]
			currentGame += 1
		currentWeekLocationAndTemperatures[currentWeekLocations[currentGame]] = currentGameTemp[currentGame]
		currentWeekLocationAndWeatherCondition[currentWeekLocations[currentGame]] = currentGameWeatherCondition[currentGame]
		
		currentGame += 2
	
		print ""
		games = nflgame.games(year, week, kind="REG")
		future_games = nflgame.live._games_in_week(year, week)
		players = nflgame.combine_game_stats(games)
		plays = nflgame.combine_plays(games)
		opponents = dict([(g.home, g.away) for g in games] + [(g.away, g.home) for g in games])
		print year, week
		for player in players.rushing().sort('rushing_yds').limit(50):
			currentTeam = str(player.team)
			if len(currentTeam) < 3:
				currentTeam += " "
			currentOpponentTeam = str(opponents[player.team])
			if len(currentOpponentTeam) < 3:
				currentOpponentTeam += " "
			if player.home:
				if currentWeekLocationAndTemperatures[currentTeam] <= 10:
					totalColdRushes += player.rushing_att
					totalColdYards += player.rushing_yds
					totalColdGames += 1
				elif currentWeekLocationAndTemperatures[currentTeam] > 10 and currentWeekLocationAndTemperatures[currentTeam] <= 32:
					totalChillyRushes += player.rushing_att
					totalChillyYards += player.rushing_yds
					totalChillyGames += 1
				elif currentWeekLocationAndTemperatures[currentTeam] > 32 and currentWeekLocationAndTemperatures[currentTeam] <= 60:
					totalMediumRushes += player.rushing_att
					totalMediumYards += player.rushing_yds
					totalMediumGames += 1
				elif currentWeekLocationAndTemperatures[currentTeam] > 60 and currentWeekLocationAndTemperatures[currentTeam] <= 80:
					totalWarmRushes += player.rushing_att
					totalWarmYards += player.rushing_yds
					totalWarmGames += 1
				elif currentWeekLocationAndTemperatures[currentTeam] > 80:
					totalHotRushes += player.rushing_att
					totalHotYards += player.rushing_yds
					totalHotGames += 1
				if currentWeekLocationAndWeatherCondition[currentTeam] == "snow\n":
					totalSnowRushes += player.rushing_att
					totalSnowRushYards += player.rushing_yds
					totalSnowGames += 1
				elif currentWeekLocationAndWeatherCondition[currentTeam] == "rain\n":
					totalRainRushes += player.rushing_att
					totalRainRushYards += player.rushing_yds
					totalRainGames += 1
				elif currentWeekLocationAndWeatherCondition[currentTeam] == "wind\n":
					totalWindRushes += player.rushing_att
					totalWindRushYards += player.rushing_yds
					totalWindGames += 1
				elif currentWeekLocationAndWeatherCondition[currentTeam] == "partly-cloudy-day\n":
					totalPartlyCloudyDayRushes += player.rushing_att
					totalPartlyCloudyDayRushYards += player.rushing_yds
					totalPartlyCloudyDayGames += 1
				elif currentWeekLocationAndWeatherCondition[currentTeam] == "partly-cloudy-night\n":
					totalPartlyCloudyNightRushes += player.rushing_att
					totalPartlyCloudyNightRushYards += player.rushing_yds
					totalPartlyCloudyNightGames += 1
				elif currentWeekLocationAndWeatherCondition[currentTeam] == "cloudy\n":
					totalCloudyRushes += player.rushing_att
					totalCloudyRushYards += player.rushing_yds
					totalCloudyGames += 1
				elif currentWeekLocationAndWeatherCondition[currentTeam] == "clear-day\n":
					totalNormalRushes += player.rushing_att
					totalNormalRushYards += player.rushing_yds
					totalNormalGames += 1
				elif currentWeekLocationAndWeatherCondition[currentTeam] == "fog\n":
					totalFogRushes += player.rushing_att
					totalFogRushYards += player.rushing_yds
					totalFogGames += 1
				
					
			else:
				if currentWeekLocationAndTemperatures[currentOpponentTeam] <= 10:
					totalColdRushes += player.rushing_att
					totalColdYards += player.rushing_yds
					totalColdGames += 1
				elif currentWeekLocationAndTemperatures[currentOpponentTeam] > 10 and currentWeekLocationAndTemperatures[currentOpponentTeam] <= 32:
					totalChillyRushes += player.rushing_att
					totalChillyYards += player.rushing_yds
					totalChillyGames += 1
				elif currentWeekLocationAndTemperatures[currentOpponentTeam] > 32 and currentWeekLocationAndTemperatures[currentOpponentTeam] <= 60:
					totalMediumRushes += player.rushing_att
					totalMediumYards += player.rushing_yds
					totalMediumGames += 1
				elif currentWeekLocationAndTemperatures[currentOpponentTeam] > 60 and currentWeekLocationAndTemperatures[currentOpponentTeam] <= 80:
					totalWarmRushes += player.rushing_att
					totalWarmYards += player.rushing_yds
					totalWarmGames += 1
				elif currentWeekLocationAndTemperatures[currentOpponentTeam] > 80:
					totalHotRushes += player.rushing_att
					totalHotYards += player.rushing_yds
					totalHotGames += 1
					
				if currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "snow":
					totalSnowRushes += player.rushing_att
					totalSnowRushYards += player.rushing_yds
					totalSnowGames += 1
				elif currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "rain":
					totalRainRushes += player.rushing_att
					totalRainRushYards += player.rushing_yds
					totalRainGames += 1
				elif currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "wind":
					totalWindRushes += player.rushing_att
					totalWindRushYards += player.rushing_yds
					totalWindGames += 1
				elif currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "partly-cloudy-day":
					totalPartlyCloudyDayRushes += player.rushing_att
					totalPartlyCloudyDayRushYards += player.rushing_yds
					totalPartlyCloudyDayGames += 1
				elif currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "partly-cloudy-night":
					totalPartlyCloudyNightRushes += player.rushing_att
					totalPartlyCloudyNightRushYards += player.rushing_yds
					totalPartlyCloudyNightGames += 1
				elif currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "cloudy":
					totalCloudyRushes += player.rushing_att
					totalCloudyRushYards += player.rushing_yds
					totalCloudyGames += 1
				elif currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "clear-day":
					totalNormalRushes += player.rushing_att
					totalNormalRushYards += player.rushing_yds
					totalNormalGames += 1
				elif currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "fog":
					totalFogRushes += player.rushing_att
					totalFogRushYards += player.rushing_yds
					totalFogGames += 1
		currentWeekLocationAndTemperatures.clear()
		currentWeekLocationAndWeatherCondition.clear()
print ""
print ""
print ""
print "COLD STATS  <10          :", float(float(totalColdYards)/float(totalColdRushes)), float(float(totalColdRushes)/float(totalColdGames))
print "CHILLY STATS   10< <32   :", float(float(totalChillyYards)/float(totalChillyRushes)), float(float(totalChillyRushes)/float(totalChillyGames))
print "MEDIUM STATS   32< <60   :", float(float(totalMediumYards)/float(totalMediumRushes)), float(float(totalMediumRushes)/float(totalMediumGames))
print "WARM STATS     60< <80   :", float(float(totalWarmYards)/float(totalWarmRushes)), float(float(totalWarmRushes)/float(totalWarmGames))
print "HOT STATS      80>       :", float(float(totalHotYards)/float(totalHotRushes)), float(float(totalHotRushes)/float(totalHotGames))			
print "SNOW STATS               :", float(float(totalSnowRushYards)/float(totalSnowRushes)), float(float(totalSnowRushes)/float(totalSnowGames))
print "RAIN STATS               :", float(float(totalRainRushYards)/float(totalRainRushes)), float(float(totalRainRushes)/float(totalRainGames))
print "WIND STATS               :", float(float(totalWindRushYards)/float(totalWindRushes)), float(float(totalWindRushes)/float(totalWindGames))
print "FOG STATS                :", float(float(totalFogRushYards)/float(totalFogRushes)), float(float(totalFogRushes)/float(totalFogGames))
print "NORMAL STATS             :", float(float(totalNormalRushYards)/float(totalNormalRushes)), float(float(totalNormalRushes)/float(totalNormalGames))
print "PARTLY-CLOUDY-DAY STATS  :", float(float(totalPartlyCloudyDayRushYards)/float(totalPartlyCloudyDayRushes)), float(float(totalPartlyCloudyDayRushes)/float(totalPartlyCloudyDayGames))
print "PARTLY-CLOUDY-NIGHT STATS:", float(float(totalPartlyCloudyNightRushYards)/float(totalPartlyCloudyNightRushes)), float(float(totalPartlyCloudyNightRushes)/float(totalPartlyCloudyNightGames))
print "CLOUDY STATS             :", float(float(totalCloudyRushYards)/float(totalCloudyRushes)), float(float(totalCloudyRushes)/float(totalCloudyGames))
			