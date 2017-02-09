import nflgame


for year in range(2009, 2015):
	totalInsideRushingYards = 0
	totalOutsideRushingYards = 0
	totalInsideRushingAttempts = 0
	totalOutsideRushingAttempts = 0
	totalInsideGameCount = 0
	totalOutsideGameCount = 0
	
	for week in range(1, 18):
		games = nflgame.games(year, week, kind="REG")
		players = nflgame.combine_game_stats(games)
		plays = nflgame.combine_plays(games)

		#opponents = {x[0]: x[1] for x in [(g.home, g.away) for g in games] + [(g.away, g.home) for g in games]}
		opponents = dict([(g.home, g.away) for g in games] + [(g.away, g.home) for g in games])
		print ""
		print year, week
		for player in players.rushing().sort('rushing_yds').limit(20):
			currentTeam = str(player.team)
			currentOpponentTeam = str(opponents[player.team])
			if currentTeam == "DET" or currentTeam == "ATL" or currentTeam == "MIN" or currentTeam == "NO" or currentOpponentTeam == "DET" or currentOpponentTeam == "ATL" or currentOpponentTeam == "MIN" or currentOpponentTeam == "NO":
				totalInsideRushingYards += player.rushing_yds
				totalInsideRushingAttempts += player.rushing_att
				totalInsideGameCount += 1
			else:
				totalOutsideRushingYards += player.rushing_yds
				totalOutsideRushingAttempts += player.rushing_att
				totalOutsideGameCount += 1
			print player, player.team, opponents[player.team]
		print "" 
	print "Inside: "
	print float(float(totalInsideRushingYards)/float(totalInsideRushingAttempts)), float(float(totalInsideRushingAttempts)/float(totalInsideGameCount))
	print "Outside: "
	print float(float(totalOutsideRushingYards)/float(totalOutsideRushingAttempts)), float(float(totalOutsideRushingAttempts)/float(totalOutsideGameCount))