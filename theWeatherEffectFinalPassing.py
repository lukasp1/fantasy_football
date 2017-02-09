import nflgame

totalColdPasses = 0
totalColdPassYards = 0
totalColdGames = 0

totalChillyPasses = 0
totalChillyPassYards = 0
totalChillyGames = 0

totalMediumPasses = 0
totalMediumPassYards = 0
totalMediumGames = 0

totalWarmPasses = 0
totalWarmPassYards = 0
totalWarmGames = 0

totalHotPasses = 0
totalHotPassYards = 0
totalHotGames = 0


totalSnowPasses = 0
totalSnowPassYards = 0
totalSnowGames = 0

totalRainPasses = 0
totalRainPassYards = 0
totalRainGames = 0

totalWindPasses = 0
totalWindPassYards = 0
totalWindGames = 0

totalPartlyCloudyDayPasses = 0
totalPartlyCloudyDayPassYards = 0
totalPartlyCloudyDayGames = 0

totalPartlyCloudyNightPasses = 0
totalPartlyCloudyNightPassYards = 0
totalPartlyCloudyNightGames = 0

totalCloudyPasses = 0
totalCloudyPassYards = 0
totalCloudyGames = 0

totalFogPasses = 0
totalFogPassYards = 0
totalFogGames = 0

totalNormalPasses = 0
totalNormalPassYards = 0
totalNormalGames = 0

currentWeekLocations = dict()
currentGameTemp = dict()
currentGameWeatherCondition = dict()


currentWeekLocationAndTemperatures = dict()
currentWeekLocationAndWeatherCondition = dict()


with open('weatherCollection.txt') as f:
	content = f.readlines()
# initialize a dictionary that holds the location of each game    
count = 1
for current in content:
	currentWeekLocations[count] = str(current[29:32])
	count+=1
count = 1
# initialize 2 dictionaries that hold the temperature and the weather conditions 	
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
		for current in currentWeekLocationAndTemperatures:
			print current, currentWeekLocationAndTemperatures[current]
		print ""
		games = nflgame.games(year, week, kind="REG")
		players = nflgame.combine_game_stats(games)
		plays = nflgame.combine_plays(games)
		opponents = dict([(g.home, g.away) for g in games] + [(g.away, g.home) for g in games])
		print year, week
		for player in players.passing().sort('passing_yds').limit(20):
			currentTeam = str(player.team)
			if len(currentTeam) < 3:
				currentTeam += " "
			currentOpponentTeam = str(opponents[player.team])
			if len(currentOpponentTeam) < 3:
				currentOpponentTeam += " "
			if player.home:
				if (currentWeekLocationAndTemperatures[currentTeam] <= 10):
					totalColdPasses += player.passing_att
					totalColdPassYards += player.passing_yds
					totalColdGames += 1
				if (currentWeekLocationAndTemperatures[currentTeam] > 10) and (currentWeekLocationAndTemperatures[currentTeam] <= 32):
					totalChillyPasses += player.passing_att
					totalChillyPassYards += player.passing_yds
					totalChillyGames += 1
				if (currentWeekLocationAndTemperatures[currentTeam] > 32) and (currentWeekLocationAndTemperatures[currentTeam] <= 60):
					totalMediumPasses += player.passing_att
					totalMediumPassYards += player.passing_yds
					totalMediumGames += 1
				if (currentWeekLocationAndTemperatures[currentTeam] > 60) and (currentWeekLocationAndTemperatures[currentTeam] <= 80):
					totalWarmPasses += player.passing_att
					totalWarmPassYards += player.passing_yds
					totalWarmGames += 1
				if (currentWeekLocationAndTemperatures[currentTeam] > 80):
					totalHotPasses += player.passing_att
					totalHotPassYards += player.passing_yds
					totalHotGames += 1
				if currentWeekLocationAndWeatherCondition[currentTeam] == "snow\n":
					totalSnowPasses += player.passing_att
					totalSnowPassYards += player.passing_yds
					totalSnowGames += 1
				elif currentWeekLocationAndWeatherCondition[currentTeam] == "rain\n":
					totalRainPasses += player.passing_att
					totalRainPassYards += player.passing_yds
					totalRainGames += 1
				elif currentWeekLocationAndWeatherCondition[currentTeam] == "wind\n":
					totalWindPasses += player.passing_att
					totalWindPassYards += player.passing_yds
					totalWindGames += 1
				elif currentWeekLocationAndWeatherCondition[currentTeam] == "partly-cloudy-day\n":
					totalPartlyCloudyDayPasses += player.passing_att
					totalPartlyCloudyDayPassYards += player.passing_yds
					totalPartlyCloudyDayGames += 1
				elif currentWeekLocationAndWeatherCondition[currentTeam] == "partly-cloudy-night\n":
					totalPartlyCloudyNightPasses += player.passing_att
					totalPartlyCloudyNightPassYards += player.passing_yds
					totalPartlyCloudyNightGames += 1
				elif currentWeekLocationAndWeatherCondition[currentTeam] == "cloudy\n":
					totalCloudyPasses += player.passing_att
					totalCloudyPassYards += player.passing_yds
					totalCloudyGames += 1
				elif currentWeekLocationAndWeatherCondition[currentTeam] == "clear-day\n":
					totalNormalPasses += player.passing_att
					totalNormalPassYards += player.passing_yds
					totalNormalGames += 1
				elif currentWeekLocationAndWeatherCondition[currentTeam] == "fog\n":
					totalFogPasses += player.passing_att
					totalFogPassYards += player.passing_yds
					totalFogGames += 1
				
					
			else:
				if (currentWeekLocationAndTemperatures[currentOpponentTeam] <= 10):
					totalColdPasses += player.passing_att
					totalColdPassYards += player.passing_yds
					totalColdGames += 1
				if (currentWeekLocationAndTemperatures[currentOpponentTeam] > 10) and (currentWeekLocationAndTemperatures[currentOpponentTeam] <= 32):
					totalChillyPasses += player.passing_att
					totalChillyPassYards += player.passing_yds
					totalChillyGames += 1
				if (currentWeekLocationAndTemperatures[currentOpponentTeam] > 32) and (currentWeekLocationAndTemperatures[currentOpponentTeam] <= 60):
					totalMediumPasses += player.passing_att
					totalMediumPassYards += player.passing_yds
					totalMediumGames += 1
				if (currentWeekLocationAndTemperatures[currentOpponentTeam]) > 60 and (currentWeekLocationAndTemperatures[currentOpponentTeam] <= 80):
					totalWarmPasses += player.passing_att
					totalWarmPassYards += player.passing_yds
					totalWarmGames += 1
				if (currentWeekLocationAndTemperatures[currentOpponentTeam] > 80):
					totalHotPasses += player.passing_att
					totalHotPassYards += player.passing_yds
					totalHotGames += 1
					
				if currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "snow\n":
					totalSnowPasses += player.passing_att
					totalSnowPassYards += player.passing_yds
					totalSnowGames += 1
				elif currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "rain\n":
					totalRainPasses += player.passing_att
					totalRainPassYards += player.passing_yds
					totalRainGames += 1
				elif currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "wind\n":
					totalWindPasses += player.passing_att
					totalWindPassYards += player.passing_yds
					totalWindGames += 1
				elif currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "partly-cloudy-day\n":
					totalPartlyCloudyDayPasses += player.passing_att
					totalPartlyCloudyDayPassYards += player.passing_yds
					totalPartlyCloudyDayGames += 1
				elif currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "partly-cloudy-night\n":
					totalPartlyCloudyNightPasses += player.passing_att
					totalPartlyCloudyNightPassYards += player.passing_yds
					totalPartlyCloudyNightGames += 1
				elif currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "cloudy\n":
					totalCloudyPasses += player.passing_att
					totalCloudyPassYards += player.passing_yds
					totalCloudyGames += 1
				elif currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "clear-day\n":
					totalNormalPasses += player.passing_att
					totalNormalPassYards += player.passing_yds
					totalNormalGames += 1
				elif currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "fog\n":
					totalFogPasses += player.passing_att
					totalFogPassYards += player.passing_yds
					totalFogGames += 1
		currentWeekLocationAndTemperatures.clear()
		currentWeekLocationAndWeatherCondition.clear()

print "COLD STATS  <10          :", float(float(totalColdPassYards)/float(totalColdPasses)), float(float(totalColdPasses)/float(totalColdGames)), float(float(totalColdPassYards) / float(totalColdGames))
print "CHILLY STATS   10< <32   :", float(float(totalChillyPassYards)/float(totalChillyPasses)), float(float(totalChillyPasses)/float(totalChillyGames)), float(float(totalChillyPassYards) / float(totalChillyGames))
print "MEDIUM STATS   32< <60   :", float(float(totalMediumPassYards)/float(totalMediumPasses)), float(float(totalMediumPasses)/float(totalMediumGames)), float(float(totalMediumPassYards) / float(totalMediumGames))
print "WARM STATS     60< <80   :", float(float(totalWarmPassYards)/float(totalWarmPasses)), float(float(totalWarmPasses)/float(totalWarmGames)), float(float(totalWarmPassYards) / float(totalWarmGames))
print "HOT STATS      80>       :", float(float(totalHotPassYards)/float(totalHotPasses)), float(float(totalHotPasses)/float(totalHotGames)), float(float(totalHotPassYards) / float(totalHotGames))		
print "SNOW STATS               :", float(float(totalSnowPassYards)/float(totalSnowPasses)), float(float(totalSnowPasses)/float(totalSnowGames)), float(float(totalSnowPassYards) / float(totalSnowGames))
print "RAIN STATS               :", float(float(totalRainPassYards)/float(totalRainPasses)), float(float(totalRainPasses)/float(totalRainGames)), float(float(totalRainPassYards) / float(totalRainGames))
print "WIND STATS               :", float(float(totalWindPassYards)/float(totalWindPasses)), float(float(totalWindPasses)/float(totalWindGames)), float(float(totalWindPassYards) / float(totalWindGames))
print "FOG STATS                :", float(float(totalFogPassYards)/float(totalFogPasses)), float(float(totalFogPasses)/float(totalFogGames)), float(float(totalFogPassYards) / float(totalFogGames))
print "NORMAL STATS             :", float(float(totalNormalPassYards)/float(totalNormalPasses)), float(float(totalNormalPasses)/float(totalNormalGames)), float(float(totalNormalPassYards) / float(totalNormalGames))
print "PARTLY-CLOUDY-DAY STATS  :", float(float(totalPartlyCloudyDayPassYards)/float(totalPartlyCloudyDayPasses)), float(float(totalPartlyCloudyDayPasses)/float(totalPartlyCloudyDayGames)), float(float(totalPartlyCloudyDayPassYards) / float(totalPartlyCloudyDayGames))
print "PARTLY-CLOUDY-NIGHT STATS:", float(float(totalPartlyCloudyNightPassYards)/float(totalPartlyCloudyNightPasses)), float(float(totalPartlyCloudyNightPasses)/float(totalPartlyCloudyNightGames)), float(float(totalPartlyCloudyNightPassYards) / float(totalPartlyCloudyNightGames))
print "CLOUDY STATS             :", float(float(totalCloudyPassYards)/float(totalCloudyPasses)), float(float(totalCloudyPasses)/float(totalCloudyGames)), float(float(totalCloudyPassYards) / float(totalCloudyGames))
print totalChillyGames
print totalColdGames
print totalMediumGames
print totalWarmGames
print totalHotGames