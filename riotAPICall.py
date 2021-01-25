import json
import requests
import constants
import datetime

getUserIDURL = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + constants.summonerName + "?api_key=" + constants.riotAPI
getUserID = requests.get(getUserIDURL)
if getUserID.status_code == 200:
    userIDInfo = json.loads(getUserID.text)
    accountId = userIDInfo["accountId"]
else:
    print("Error in getting userID! Response code " + getUserID.status_code)

getMatchesURL = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountId +"?api_key=" + constants.riotAPI
getMatches = requests.get(getMatchesURL)
if getMatches.status_code == 200:
    gameMatchesInfo = json.loads(getMatches.text)
else:
    print("Error in getting matches! Response code " + getMatches.status_code)



gameIdList = []

for n in range(100):
    if datetime.datetime.fromtimestamp(gameMatchesInfo["matches"][n]["timestamp"]/1000.0) > datetime.datetime.fromtimestamp(constants.timeFilter/1000.0):
        gameIdList.append(gameMatchesInfo["matches"][n]["gameId"])

gameTimeList = []

for gameId in gameIdList:
    getMatchInfoURL = "https://na1.api.riotgames.com/lol/match/v4/matches/" + str(gameId) + "?api_key=" + constants.riotAPI
    getMatchInfo = requests.get(getMatchInfoURL)
    if getMatchInfo.status_code == 200:
        getMatchInformation = json.loads(getMatchInfo.text)
        gameTimeList.append(getMatchInformation["gameDuration"])
    else:
        print("Error in getting match info! Response code " + getMatchInfo.status_code)