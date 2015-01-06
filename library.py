import requests
import json
##servers

BRAZIL = 'br'
EU_NE = 'eune'
EU_WEST = 'euw'
KOREA = 'kr'
LATIN_AMERICA_NORTH = 'lan'
LATIN_AMERICA_SOUTH = 'las'
NORTH_AMERICA = 'na'
OCEANIA = 'oce'
RUSSIA = 'ru'
TURKEY = 'tr'

queue_types = [
	'CUSTOM', # Custom games
	'NORMAL_5x5_BLIND', # Normal 5v5 blind pick
	'BOT_5x5', # Historical Summoners Rift coop vs AI games
	'BOT_5x5_INTRO', # Summoners Rift Intro bots
	'BOT_5x5_BEGINNER', # Summoner's Rift Coop vs AI Beginner Bot games
	'BOT_5x5_INTERMEDIATE', # Historical Summoner's Rift Coop vs AI Intermediate Bot games
	'NORMAL_3x3', # Normal 3v3 games
	'NORMAL_5x5_DRAFT', # Normal 5v5 Draft Pick games
	'ODIN_5x5_BLIND', # Dominion 5v5 Blind Pick games
	'ODIN_5x5_DRAFT', # Dominion 5v5 Draft Pick games
	'BOT_ODIN_5x5', # Dominion Coop vs AI games
	'RANKED_SOLO_5x5', # Ranked Solo 5v5 games
	'RANKED_PREMADE_3x3', # Ranked Premade 3v3 games
	'RANKED_PREMADE_5x5', # Ranked Premade 5v5 games
	'RANKED_TEAM_3x3', # Ranked Team 3v3 games
	'RANKED_TEAM_5x5', # Ranked Team 5v5 games
	'BOT_TT_3x3', # Twisted Treeline Coop vs AI games
	'GROUP_FINDER_5x5', # Team Builder games
	'ARAM_5x5', # ARAM games
	'ONEFORALL_5x5', # One for All games
	'FIRSTBLOOD_1x1', # Snowdown Showdown 1v1 games
	'FIRSTBLOOD_2x2', # Snowdown Showdown 2v2 games
	'SR_6x6', # Hexakill games
	'URF_5x5', # Ultra Rapid Fire games
	'BOT_URF_5x5', # Ultra Rapid Fire games played against AI games
	'NIGHTMARE_BOT_5x5_RANK1', # Doom Bots Rank 1 games
	'NIGHTMARE_BOT_5x5_RANK2', # Doom Bots Rank 2 games
	'NIGHTMARE_BOT_5x5_RANK5', # Doom Bots Rank 5 games
	'ASCENSION_5x5', # Ascension games
	'HEXAKILL', # 6v6 games on twisted treeline
	'KING_PORO_5x5', # King Poro game games
]
game_maps = [
	{'map_id': 1, 'name': "Summoner's Rift", 'notes': "Summer Variant"},
	{'map_id': 2, 'name': "Summoner's Rift", 'notes': "Autumn Variant"},
	{'map_id': 3, 'name': "The Proving Grounds", 'notes': "Tutorial Map"},
	{'map_id': 4, 'name': "Twisted Treeline", 'notes': "Original Version"},
	{'map_id': 8, 'name': "The Crystal Scar", 'notes': "Dominion Map"},
	{'map_id': 10, 'name': "Twisted Treeline", 'notes': "Current Version"},
	{'map_id': 11, 'name': "Summoner's Rift", 'notes': "Current Version"},
	{'map_id': 12, 'name': "Howling Abyss", 'notes': "ARAM Map"},
]
game_modes = [
	'CLASSIC', # Classic Summoner's Rift and Twisted Treeline games
	'ODIN', # Dominion/Crystal Scar games
	'ARAM', # ARAM games
	'TUTORIAL', # Tutorial games
	'ONEFORALL', # One for All games
	'ASCENSION', # Ascension games
	'FIRSTBLOOD', # Snowdown Showdown games
	'KINGPORO', # King Poro games
]
game_types = [
	'CUSTOM_GAME', # Custom games
	'TUTORIAL_GAME', # Tutorial games
	'MATCHED_GAME', # All other games
]
sub_types = [
	'NONE', # Custom games
	'NORMAL', # Summoner's Rift unranked games
	'NORMAL_3x3', # Twisted Treeline unranked games
	'ODIN_UNRANKED', # Dominion/Crystal Scar games
	'ARAM_UNRANKED_5v5', # ARAM / Howling Abyss games
	'BOT', # Summoner's Rift and Crystal Scar games played against AI
	'BOT_3x3', # Twisted Treeline games played against AI
	'RANKED_SOLO_5x5', # Summoner's Rift ranked solo queue games
	'RANKED_TEAM_3x3', # Twisted Treeline ranked team games
	'RANKED_TEAM_5x5', # Summoner's Rift ranked team games
	'ONEFORALL_5x5', # One for All games
	'FIRSTBLOOD_1x1', # Snowdown Showdown 1x1 games
	'FIRSTBLOOD_2x2', # Snowdown Showdown 2x2 games
	'SR_6x6', # Hexakill games
	'CAP_5x5', # Team Builder games
	'URF', # Ultra Rapid Fire games
	'URF_BOT', # Ultra Rapid Fire games against AI
	'NIGHTMARE_BOT', # Nightmare bots
	'ASCENSION', # Ascension games
	'HEXAKILL', # Twisted Treeline 6x6 Hexakill
	'KING_PORO', # King Poro games
]
player_stat_summary_types = [
	'Unranked', # Summoner's Rift unranked games
	'Unranked3x3', # Twisted Treeline unranked games
	'OdinUnranked', # Dominion/Crystal Scar games
	'AramUnranked5x5', # ARAM / Howling Abyss games
	'CoopVsAI', # Summoner's Rift and Crystal Scar games played against AI
	'CoopVsAI3x3', # Twisted Treeline games played against AI
	'RankedSolo5x5', # Summoner's Rift ranked solo queue games
	'RankedTeams3x3', # Twisted Treeline ranked team games
	'RankedTeams5x5', # Summoner's Rift ranked team games
	'OneForAll5x5', # One for All games
	'FirstBlood1x1', # Snowdown Showdown 1x1 games
	'FirstBlood2x2', # Snowdown Showdown 2x2 games
	'SummonersRift6x6', # Hexakill games
	'CAP5x5', # Team Builder games
	'URF', # Ultra Rapid Fire games
	'URFBots', # Ultra Rapid Fire games played against AI
	'NightmareBot', # Summoner's Rift games played against Nightmare AI
	'Hexakill', # Twisted Treeline 6x6 Hexakill games
	'KingPoro', # King Poro games
]
solo_queue, ranked_5s, ranked_3s = 'RANKED_SOLO_5x5', 'RANKED_TEAM_5x5', 'RANKED_TEAM_3x3'



API_Versions = {

	'lolstats':'v1.0',
	'summoner':'v1.4', 
}
##Global Functions
