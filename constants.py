import datetime
import time

riotAPI = "RGAPI-29b20258-8841-46c9-9fa1-ec6e0873a5fd"

summonerName = input("Enter summoner name: ")
summonerName = summonerName.replace(" ", "%20")

timeLength = input("Enter time length: ")
timeLengthMil = int(int(timeLength)*86400000)
currentTime = time.time() * 1000
timeFilter = currentTime - timeLengthMil