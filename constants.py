import datetime
import time

riotAPI = "RGAPI-ea484409-9ff3-4f05-977e-7e1f815e3ba5"

summonerName = input("Enter Summoner Name: ")
summonerName = summonerName.replace(" ", "%20")

timeLength = input("Enter time length in days: ")
timeLengthMil = int(int(timeLength)*86400000)
currentTime = time.time() * 1000
timeFilter = currentTime - timeLengthMil