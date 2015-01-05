import library
import requests

API_key = "358969da-a891-4cbc-88d5-de39cdfa77ce"
default_region = "br"
default_summoner = "Unuzual"
number_of_servers = 10


class riotPythonAPI:
	def __init__(self,API_key,region=None,Summoner=None):
		self.key = API_key
		
		if region is None:
			self.default_region=Region

		else
			self.default_region=region

		self.default_summoner=Summoner


	#lolstatus-1.0		
	def request_server_status(self,region = None):
		if region is None:
			print '+'*30
			r = requests.get('http://status.leagueoflegends.com/shards/{url}'.format(url=default_region))
		else:
			print '-'*30
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

	def request_summoner_id(self,summoner = None):
		if summoner is None:
			region = self.default_region
			summoner= self.default_summoner

			r = requests.get('https://{region}.api.pvp.net/api/lol/{region}/v1.4/summoner/by-name/{summoner}?api_key={key}'.format(region=region,summoner=summoner,key=API_key))

		return r.json()


x = riotPythonAPI(API_key,'br','Doublelift')

print "Status servidor Br: ", x.request_server_status()['services'][0]['status']