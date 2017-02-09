import nflgame

totalColdReceptions = 0
totalColdRecYards = 0
totalColdGames = 0

totalChillyReceptions = 0
totalChillyRecYards = 0
totalChillyGames = 0

totalMediumReceptions = 0
totalMediumRecYards = 0
totalMediumGames = 0

totalWarmReceptions = 0
totalWarmRecYards = 0
totalWarmGames = 0

totalHotReceptions = 0
totalHotRecYards = 0
totalHotGames = 0


totalSnowReceptions = 0
totalSnowRecYards = 0
totalSnowGames = 0

totalRainReceptions = 0
totalRainRecYards = 0
totalRainGames = 0

totalWindReceptions = 0
totalWindRecYards = 0
totalWindGames = 0

totalPartlyCloudyDayReceptions = 0
totalPartlyCloudyDayRecYards = 0
totalPartlyCloudyDayGames = 0

totalPartlyCloudyNightReceptions = 0
totalPartlyCloudyNightRecYards = 0
totalPartlyCloudyNightGames = 0

totalCloudyReceptions = 0
totalCloudyRecYards = 0
totalCloudyGames = 0

totalFogReceptions = 0
totalFogRecYards = 0
totalFogGames = 0

totalNormalReceptions = 0
totalNormalRecYards = 0
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
		for player in players.receiving().sort('receiving_yds').limit(50):
			currentTeam = str(player.team)
			if len(currentTeam) < 3:
				currentTeam += " "
			currentOpponentTeam = str(opponents[player.team])
			if len(currentOpponentTeam) < 3:
				currentOpponentTeam += " "
			if player.home:
				if (currentWeekLocationAndTemperatures[currentTeam] <= 10):
					totalColdReceptions += player.receiving_rec
					totalColdRecYards += player.receiving_yds
					totalColdGames += 1
				elif (currentWeekLocationAndTemperatures[currentTeam] > 10) and (currentWeekLocationAndTemperatures[currentTeam] <= 32):
					totalChillyReceptions += player.receiving_rec
					totalChillyRecYards += player.receiving_yds
					totalChillyGames += 1
				elif (currentWeekLocationAndTemperatures[currentTeam] > 32) and (currentWeekLocationAndTemperatures[currentTeam] <= 60):
					totalMediumReceptions += player.receiving_rec
					totalMediumRecYards += player.receiving_yds
					totalMediumGames += 1
				elif (currentWeekLocationAndTemperatures[currentTeam] > 60) and (currentWeekLocationAndTemperatures[currentTeam] <= 80):
					totalWarmReceptions += player.receiving_rec
					totalWarmRecYards += player.receiving_yds
					totalWarmGames += 1
				elif (currentWeekLocationAndTemperatures[currentTeam] > 80):
					totalHotReceptions += player.receiving_rec
					totalHotRecYards += player.receiving_yds
					totalHotGames += 1
				if currentWeekLocationAndWeatherCondition[currentTeam] == "snow\n":
					totalSnowReceptions += player.receiving_rec
					totalSnowRecYards += player.receiving_yds
					totalSnowGames += 1
				elif currentWeekLocationAndWeatherCondition[currentTeam] == "rain\n":
					totalRainReceptions += player.receiving_rec
					totalRainRecYards += player.receiving_yds
					totalRainGames += 1
				elif currentWeekLocationAndWeatherCondition[currentTeam] == "wind\n":
					totalWindReceptions += player.receiving_rec
					totalWindRecYards += player.receiving_yds
					totalWindGames += 1
				elif currentWeekLocationAndWeatherCondition[currentTeam] == "partly-cloudy-day\n":
					totalPartlyCloudyDayReceptions += player.receiving_rec
					totalPartlyCloudyDayRecYards += player.receiving_yds
					totalPartlyCloudyDayGames += 1
				elif currentWeekLocationAndWeatherCondition[currentTeam] == "partly-cloudy-night\n":
					totalPartlyCloudyNightReceptions += player.receiving_rec
					totalPartlyCloudyNightRecYards += player.receiving_yds
					totalPartlyCloudyNightGames += 1
				elif currentWeekLocationAndWeatherCondition[currentTeam] == "cloudy\n":
					totalCloudyReceptions += player.receiving_rec
					totalCloudyRecYards += player.receiving_yds
					totalCloudyGames += 1
				elif currentWeekLocationAndWeatherCondition[currentTeam] == "clear-day\n":
					totalNormalReceptions += player.receiving_rec
					totalNormalRecYards += player.receiving_yds
					totalNormalGames += 1
				elif currentWeekLocationAndWeatherCondition[currentTeam] == "fog\n":
					totalFogReceptions += player.receiving_rec
					totalFogRecYards += player.receiving_yds
					totalFogGames += 1
				
					
			else:
				if (currentWeekLocationAndTemperatures[currentOpponentTeam] <= 10):
					totalColdReceptions += player.receiving_rec
					totalColdRecYards += player.receiving_yds
					totalColdGames += 1
				elif (currentWeekLocationAndTemperatures[currentOpponentTeam] > 10) and (currentWeekLocationAndTemperatures[currentOpponentTeam] <= 32):
					totalChillyReceptions += player.receiving_rec
					totalChillyRecYards += player.receiving_yds
					totalChillyGames += 1
				elif (currentWeekLocationAndTemperatures[currentOpponentTeam] > 32) and (currentWeekLocationAndTemperatures[currentOpponentTeam] <= 60):
					totalMediumReceptions += player.receiving_rec
					totalMediumRecYards += player.receiving_yds
					totalMediumGames += 1
				elif (currentWeekLocationAndTemperatures[currentOpponentTeam]) > 60 and (currentWeekLocationAndTemperatures[currentOpponentTeam] <= 80):
					totalWarmReceptions += player.receiving_rec
					totalWarmRecYards += player.receiving_yds
					totalWarmGames += 1
				elif (currentWeekLocationAndTemperatures[currentOpponentTeam] > 80):
					totalHotReceptions += player.receiving_rec
					totalHotRecYards += player.receiving_yds
					totalHotGames += 1
					
				if currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "snow\n":
					totalSnowReceptions += player.receiving_rec
					totalSnowRecYards += player.receiving_yds
					totalSnowGames += 1
				elif currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "rain\n":
					totalRainReceptions += player.receiving_rec
					totalRainRecYards += player.receiving_yds
					totalRainGames += 1
				elif currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "wind\n":
					totalWindReceptions += player.receiving_rec
					totalWindRecYards += player.receiving_yds
					totalWindGames += 1
				elif currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "partly-cloudy-day\n":
					totalPartlyCloudyDayReceptions += player.receiving_rec
					totalPartlyCloudyDayRecYards += player.receiving_yds
					totalPartlyCloudyDayGames += 1
				elif currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "partly-cloudy-night\n":
					totalPartlyCloudyNightReceptions += player.receiving_rec
					totalPartlyCloudyNightRecYards += player.receiving_yds
					totalPartlyCloudyNightGames += 1
				elif currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "cloudy\n":
					totalCloudyReceptions += player.receiving_rec
					totalCloudyRecYards += player.receiving_yds
					totalCloudyGames += 1
				elif currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "clear-day\n":
					totalNormalReceptions += player.receiving_rec
					totalNormalRecYards += player.receiving_yds
					totalNormalGames += 1
				elif currentWeekLocationAndWeatherCondition[currentOpponentTeam] == "fog\n":
					totalFogReceptions += player.receiving_rec
					totalFogRecYards += player.receiving_yds
					totalFogGames += 1
		currentWeekLocationAndTemperatures.clear()
		currentWeekLocationAndWeatherCondition.clear()

print "COLD STATS  <10          :", float(float(totalColdRecYards)/float(totalColdReceptions)), float(float(totalColdReceptions)/float(totalColdGames)), float(float(totalColdRecYards) / float(totalColdGames))
print "CHILLY STATS   10< <32   :", float(float(totalChillyRecYards)/float(totalChillyReceptions)), float(float(totalChillyReceptions)/float(totalChillyGames)), float(float(totalChillyRecYards) / float(totalChillyGames))
print "MEDIUM STATS   32< <60   :", float(float(totalMediumRecYards)/float(totalMediumReceptions)), float(float(totalMediumReceptions)/float(totalMediumGames)), float(float(totalMediumRecYards) / float(totalMediumGames))
print "WARM STATS     60< <80   :", float(float(totalWarmRecYards)/float(totalWarmReceptions)), float(float(totalWarmReceptions)/float(totalWarmGames)), float(float(totalWarmRecYards) / float(totalWarmGames))
print "HOT STATS      80>       :", float(float(totalHotRecYards)/float(totalHotReceptions)), float(float(totalHotReceptions)/float(totalHotGames)), float(float(totalHotRecYards) / float(totalHotGames))		
print "SNOW STATS               :", float(float(totalSnowRecYards)/float(totalSnowReceptions)), float(float(totalSnowReceptions)/float(totalSnowGames)), float(float(totalSnowRecYards) / float(totalSnowGames))
print "RAIN STATS               :", float(float(totalRainRecYards)/float(totalRainReceptions)), float(float(totalRainReceptions)/float(totalRainGames)), float(float(totalRainRecYards) / float(totalRainGames))
print "WIND STATS               :", float(float(totalWindRecYards)/float(totalWindReceptions)), float(float(totalWindReceptions)/float(totalWindGames)), float(float(totalWindRecYards) / float(totalWindGames))
print "FOG STATS                :", float(float(totalFogRecYards)/float(totalFogReceptions)), float(float(totalFogReceptions)/float(totalFogGames)), float(float(totalFogRecYards) / float(totalFogGames))
print "NORMAL STATS             :", float(float(totalNormalRecYards)/float(totalNormalReceptions)), float(float(totalNormalReceptions)/float(totalNormalGames)), float(float(totalNormalRecYards) / float(totalNormalGames))
print "PARTLY-CLOUDY-DAY STATS  :", float(float(totalPartlyCloudyDayRecYards)/float(totalPartlyCloudyDayReceptions)), float(float(totalPartlyCloudyDayReceptions)/float(totalPartlyCloudyDayGames)), float(float(totalPartlyCloudyDayRecYards) / float(totalPartlyCloudyDayGames))
print "PARTLY-CLOUDY-NIGHT STATS:", float(float(totalPartlyCloudyNightRecYards)/float(totalPartlyCloudyNightReceptions)), float(float(totalPartlyCloudyNightReceptions)/float(totalPartlyCloudyNightGames)), float(float(totalPartlyCloudyNightRecYards) / float(totalPartlyCloudyNightGames))
print "CLOUDY STATS             :", float(float(totalCloudyRecYards)/float(totalCloudyReceptions)), float(float(totalCloudyReceptions)/float(totalCloudyGames)), float(float(totalCloudyRecYards) / float(totalCloudyGames))