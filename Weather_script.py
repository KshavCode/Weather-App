from tkinter import *
import requests
import time
from PIL import Image, ImageTk as imtk

root = Tk()
root.geometry("500x300")
root.title("Weather App")
root.wm_iconbitmap("C:\\Users\\PC\\Desktop\\Coding Tutorial\\Project\\Weather App\\photo\\icon.ico")
root.resizable(False, False)


def cel(far) : 
    b = (far - 32) * 5/9
    return int(b)

def req() : 
    global img1, img1lab
    query = place_name.get()
    timee = time.strftime("%y-%m-%d")
    timeee = time.strftime("%H:%M:%S")
    
    if query.lower() == "delhi" : 
        query = "New Delhi"
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{query}/20{timee}T{timeee}?key=H5976K629HDQX4BGJFTVZQRCN"
    r = requests.get(url)
    
    if int(r.status_code) == 404  : 
        today.set("Invalid Place")

    temperatureF = r.json()["days"][0]["temp"]
    maxtempF = r.json()["days"][0]["tempmax"]
    mintempF = r.json()["days"][0]["tempmin"]
    temperatureC = cel(int(temperatureF))
    mintempC = cel(int(mintempF))
    maxtempC = cel(int(maxtempF))
    precipitation = r.json()["days"][0]["precipprob"]
    cloudcover = r.json()["days"][0]["cloudcover"]
    
    today.set(f"{temperatureF}°F / {temperatureC}°C ")
    maxval.set(f"{maxtempF}°F / {maxtempC}°C ")
    minval.set(f"{mintempF}°F / {mintempC}°C ")
    precpit.set(f"{precipitation}%")
    cloud.set(f"{cloudcover}%")
    
    
def reset() : 
    place_name.set("")
    today.set("Enter Place first")
    maxval.set("")
    minval.set("")
    cloud.set("")
    precpit.set("")


place_name = StringVar()
today = StringVar()
maxval = StringVar()
minval = StringVar()
precpit = StringVar()
cloud = StringVar()
today.set("Enter Place first")


place_ask = Label(root, text = "Enter Place Name : ", font = "arial 12 bold")
result_lab = Label(root, text = "Current Weather : ", font = "arial 12 bold")
maxx = Label(root, text="Maximum Temperature : ", font = "arial 12 bold")
minn = Label(root, text="Minimum Temperature : ", font = "arial 12 bold")
prec = Label(root, text="Precipation Chances : ", font = "arial 12 bold")
cloudd = Label(root, text="Cloud Percentage : ", font = "arial 12 bold")

maxnum = Entry(root, textvariable = maxval, state=DISABLED,  font="comicssansms 12", justify=CENTER)
minum = Entry(root, textvariable = minval, state=DISABLED,  font="comicssansms 12", justify=CENTER)
place = Entry(root, textvariable = place_name, font="comicssansms 12",  justify=CENTER)
result = Entry(root, textvariable = today, state=DISABLED,  font="comicssansms 12", justify=CENTER)
precipitate = Entry(root, textvariable=precpit, state=DISABLED, font="comicssansms 12", justify=CENTER)
cloudcov = Entry(root, textvariable=cloud, state=DISABLED, font="comicssansms 12", justify=CENTER)

con = Button(root, text = "Confirm", command = req, justify=CENTER, width=8, bg="#ccffcc", cursor = "spider", relief=RAISED)
res = Button(root, text = "Reset", command = reset, justify=CENTER, width=7, bg="#ff6666", cursor="pirate", relief=RAISED)


place_ask.grid(row=0, column=0, pady=40, sticky=W)
place.grid(row=0, column=1, pady=40, sticky=W)
result_lab.grid(row=1, column=0, sticky=W)
result.grid(row=1, column=1, sticky=W)
maxx.grid(row=2, column=0, sticky=W)
maxnum.grid(row=2, column=1, sticky=W)
minn.grid(row=3, column=0, sticky=W)
minum.grid(row=3, column=1, sticky=W)
prec.grid(row=4, column=0, sticky=W)
precipitate.grid(row=4, column=1, sticky=W)
cloudd.grid(row=5, column=0, sticky=W)
cloudcov.grid(row=5, column=1, sticky=W)

con.grid(row=6, column=0, pady = 20)
res.grid(row=6, column=1, pady = 20)



root.mainloop()