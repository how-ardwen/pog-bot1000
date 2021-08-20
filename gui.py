import tkinter as tk

window = tk.Tk()
window.geometry("300x150")

def retrieveInputs():
    apiKeyInput = apiKey.get()
    snInput = sn.get()
    timeLengthInput = timeLength.get()

apiTitle = tk.Label(text="Enter Riot API key")
apiTitle.pack()
apiKey = tk.Entry()
apiKey.pack()

snTitle = tk.Label(text="Enter Summoner Name")
snTitle.pack()
sn = tk.Entry()
sn.pack()

lengthTitle = tk.Label(text="Enter time length")
lengthTitle.pack()
timeLength = tk.Entry()
timeLength.pack()

submitButton = tk.Button(text="Enter", activebackground="DarkOliveGreen1", command = retrieveInputs)
submitButton.pack()

window.title("Time Spent on League")
window.mainloop()