import constants
import riotAPICall

timePlayed = 0

for length in riotAPICall.gameTimeList:
    timePlayed = length + timePlayed

timePlayedMinutes = int(timePlayed/60)

summonerName = constants.summonerName.replace("%20", " ")

if timePlayedMinutes == 0:
    print(f"Holy Shit! {summonerName} has played 0 minutes of league in the past {constants.timeLength} days!!! I bet " + summonerName + " gets bitches!")
elif 1 > timePlayedMinutes> 0:
    print(summonerName + " has played " + str(timePlayedMinutes) + " minutes of league in the past " + constants.timeLength + " days!")
else:
    print(summonerName + " has played " + str(timePlayedMinutes) + " minutes of league in the past " + constants.timeLength + " days!!")