import datetime
import time

riotAPI = input("Enter riotAPI key: ")

summonerName = input("Enter Summoner Name: ")
summonerName = summonerName.replace(" ", "%20")

timeLength = input("Enter time length: ")
timeLengthMil = int(int(timeLength)*86400000)
currentTime = time.time() * 1000
timeFilter = currentTime - timeLengthMil