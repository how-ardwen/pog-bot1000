import json
import requests
import constants

#summonerName = input("Enter summoner name: ")
#summonerName = summonerName.replace(" ", "%20")
summonerName = "newb slayer"

getUserIDURL = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + constants.riotAPI
getUserID = requests.get(getUserIDURL)
if getUserID.status_code == 200:
    userIDInfo = json.loads(getUserID.text)
else:
    print("Error! Response code " + getUserID.status_code)

accountId = userIDInfo["accountId"]

