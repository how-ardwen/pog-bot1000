import constants
import riotAPICall
import tkinter

timePlayed = 0

for length in riotAPICall.gameTimeList:
    timePlayed = length + timePlayed

timePlayedHours = int(timePlayed/3600)
timePlayedMinutes = int((timePlayed/3600 - int(timePlayed/3600)) * 60)

summonerName = constants.summonerName.replace("%20", " ")

if timePlayedHours == 0:
    print("Holy Shit! " + summonerName + "has played 0 hours of league in the past " + constants.timeLength + " days!!! I bet " + summonerName + " gets bitches!")
elif 1 > timePlayedHours > 0:
    print(summonerName + " has played " + str(timePlayedHours) + " hours and " + str(timePlayedMinutes) + " minutes of league in the past " + constants.timeLength + " days!")
else:
    print(summonerName + " has played " + str(timePlayedHours) + " hours and " + str(timePlayedMinutes) + " minutes of league in the past " + constants.timeLength + " days!! Mf you need to get a life *o*")