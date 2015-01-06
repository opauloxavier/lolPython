import library
import requests

API_key = "358969da-a891-4cbc-88d5-de39cdfa77ce"
default_region = "br"
default_summoner = "Unuzual"
number_of_servers = 10


API_Versions = {

	'lolstats':'v1.0',
	'summoner':'v1.4', 
}

def clean_name(name):
	return name.replace(' ','').lower()	


class serverException(Exception):
	def __init__(self,error):
		self.error=error
	def __str__(self):
		return self.error

error_400 = serverException("Bad request")
error_401 = serverException("Unauthorized")
error_404 = serverException("Game data not found")
error_429 = serverException("Too many requests")
error_500 = serverException("Internal server error")
error_503 = serverException("Service unavailable")

def raise_status(response):
    if response.status_code == 400:
        raise error_400
    elif response.status_code == 401:
        raise error_401
    elif response.status_code == 404:
        raise error_404
    elif response.status_code == 429:
        raise error_429
    elif response.status_code == 500:
        raise error_500
    elif response.status_code == 503:
        raise error_503
    else:
        response.raise_for_status()


class riotPythonAPI:
	def __init__(self,API_key,region=None,Summoner=None):
		self.key = API_key
		
		if region is None:
			self.default_region=Region

		else:
			self.default_region=region

		self.default_summoner=Summoner

	#lolstatus-1.0		
	def request_server_status(self,region = None):
		if region is None:
			#print '+'*30
			r = requests.get('http://status.leagueoflegends.com/shards/{url}'.format(url=default_region))
		else:
			#print '-'*30
			r = requests.get('http://status.leagueoflegends.com/shards/{url}'.format(url=region))

		return r.json()

	def request_server_list(self):
		r = requests.get('http://status.leagueoflegends.com/shards')

		return r.json()

	def server_list(self):
		serverList =[]

		for i in range(0,number_of_servers-1):
			serverList.append(self.request_server_list()[i]['slug']) 
		
		return serverList		

	#summoner-v1.4

	def request_summoner_id(self,new_summoner = None):
		if new_summoner is None:
			region = self.default_region
			summoner = clean_name(self.default_summoner)
			r = requests.get('https://{region}.api.pvp.net/api/lol/{region}/{version}/summoner/by-name/{summoner}?api_key={key}'.format(region=region,summoner=summoner,key=API_key,version=API_Versions['summoner']))
		
		else:
			summoner = clean_name(new_summoner)
			region = self.default_region
			r = requests.get('https://{region}.api.pvp.net/api/lol/{region}/{version}/summoner/by-name/{summoner}?api_key={key}'.format(region=region,summoner=summoner,key=API_key,version=API_Versions['summoner']))

		return r.json()[summoner]['id']
		

x = riotPythonAPI(API_key,'br','doublelift')

print x.request_summoner_id('unuzual') 