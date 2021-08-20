import tkinter as tk

window = tk.Tk()
window.geometry("300x150")

apiKeyInput = None
snInput = None

def retrieveInputs():
    apiKeyInput = apiKey.get()
    #snInput = sn.get()
    return apiKeyInput

apiTitle = tk.Label(text="Enter Riot API key")
apiTitle.pack()
apiKey = tk.Entry()
apiKey.pack()

snTitle = tk.Label(text="Enter Summoner Name")
snTitle.pack()
sn = tk.Entry()
sn.pack()

submitButton = tk.Button(text="Enter", activebackground="DarkOliveGreen1", command = retrieveInputs)
submitButton.pack()

window.title("Time Spent on League")
window.mainloop()