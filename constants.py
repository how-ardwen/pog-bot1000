import datetime
import time

riotAPI = "RGAPI-03105251-9602-4727-a1c5-c3d249234cd3"

summonerName = input("Enter Summoner Name: ")
summonerName = summonerName.replace(" ", "%20")

timeLength = input("Enter time length in days: ")
timeLengthMil = int(int(timeLength)*86400)
currentTime = time.time()
timeFilter = int(currentTime - timeLengthMil)