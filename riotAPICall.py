import json
import requests
import constants
import datetime

getUserIDURL = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + constants.summonerName + "?api_key=" + constants.riotAPI
getUserID = requests.get(getUserIDURL)
if getUserID.status_code == 200:
    userIDInfo = json.loads(getUserID.text)
    accountId = userIDInfo["puuid"]
else:
    print("Error in getting userID! Response code " + str(getUserID.status_code))

getMatchesURL = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/" + accountId + "/ids" + "?startTime=" + str(constants.timeFilter) + "&api_key=" + constants.riotAPI
getMatches = requests.get(getMatchesURL)
if getMatches.status_code == 200:
    gameMatchesInfo = json.loads(getMatches.text)
else:
    print(f"Error in getting matches! Response code {getMatches.status_code}")


gameIdList = gameMatchesInfo
# n = 0

# while datetime.datetime.fromtimestamp(gameMatchesInfo["matches"][n]["timestamp"]/1000.0) > datetime.datetime.fromtimestamp(constants.timeFilter/1000.0):
#        gameIdList.append(gameMatchesInfo["matches"][n]["gameId"])
#        n += 1

gameTimeList = []

for gameId in gameIdList:
    getMatchInfoURL = "https://americas.api.riotgames.com/lol/match/v5/matches/" + str(gameId) + "?api_key=" + constants.riotAPI
    getMatchInfo = requests.get(getMatchInfoURL)
    if getMatchInfo.status_code == 200:
        getMatchInformation = json.loads(getMatchInfo.text)
        gameTimeList.append(getMatchInformation["info"]["gameDuration"])
    else:
        print("Error in getting match info! Response code " + str(getMatchInfo.status_code))